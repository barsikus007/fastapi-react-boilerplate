from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from src import crud
from src.core import security
from src.core.config import settings
from src.db.session import SessionLocal
from src.models import User

reusable_oauth2 = security.OAuth2PasswordBearerCookie(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token",
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


async def get_current_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    token: Annotated[str, Depends(reusable_oauth2)],
) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[security.ALGORITHM],
        )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        ) from e
    user = await crud.user.get(db, id_=int(payload["sub"]))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have enough privileges",
        )
    return current_user
