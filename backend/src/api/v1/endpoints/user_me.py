# pyright: reportReturnType=false
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import crud
from src.api import deps
from src.models import User
from src.schemas.user import IUserRead, IUserUpdate

router = APIRouter(dependencies=[Depends(deps.get_current_active_user)])


@router.get("")
async def get_my_data(
    *,
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
) -> IUserRead:
    return current_user


@router.put("")
async def update_user_me(
    *,
    user_in: IUserUpdate,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
) -> IUserRead:
    if user_in.email and await crud.user.get_by_email(db, email=user_in.email):
        raise HTTPException(status_code=400, detail="There is already a user with same email")
    return await crud.user.update(db, obj_db=current_user, obj_in=user_in)
