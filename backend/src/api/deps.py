from typing import AsyncGenerator

from jose import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel.ext.asyncio.session import AsyncSession

from src import crud
from src.db.session import SessionLocal
from src.core import security
from src.core.config import settings
from src.models import User
# from src.schemas.common import IMetaGeneral


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


# async def get_general_meta(
#     db_session: AsyncSession = Depends(get_db)
# ) -> IMetaGeneral:
#     current_roles = await crud.role.get_multi(db_session, skip=0, limit=100)
#     return IMetaGeneral(roles=current_roles)


async def get_current_user(
    db: AsyncSession = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )  # Pylance(reportGeneralTypeIssues)
    except jwt.JWTError as e:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        ) from e
    user = await crud.user.get(db, id_=int(payload["sub"]))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: User = Depends(get_current_active_user),
) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
