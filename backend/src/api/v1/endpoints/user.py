# ruff: noqa: RET504
# pyright: reportReturnType=false
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, Params
from sqlalchemy.ext.asyncio import AsyncSession

from src import crud
from src.api import deps
from src.models import User
from src.schemas.user import IUserCreate, IUserRead, IUserUpdate, IUserUpdateAdmin

router = APIRouter()


@router.get("/")
async def read_users_list(
    *,
    params: Annotated[Params, Depends()],
    db: Annotated[AsyncSession, Depends(deps.get_db)],
    _: Annotated[User, Depends(deps.get_current_active_user)],
) -> Page[IUserRead]:
    # sourcery skip: inline-immediately-returned-variable
    users = await crud.user.get_multi(db, params=params)
    return users


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    *,
    new_user: IUserCreate,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
    _: Annotated[User, Depends(deps.get_current_active_superuser)],
) -> IUserRead:
    user = await crud.user.get_by_email(db, email=new_user.email)
    if user:
        raise HTTPException(status_code=400, detail="There is already a user with same email")
    user = await crud.user.create(db, obj_in=new_user)
    return user


@router.get("/me")
async def get_my_data(
    *,
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
) -> IUserRead:
    return current_user


@router.get("/{user_id}")
async def get_user_by_id(
    *,
    user_id: int,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
    _: Annotated[User, Depends(deps.get_current_active_superuser)],
) -> IUserRead:
    user = await crud.user.get(db, id_=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/me")
async def update_user_me(
    *,
    user_in: IUserUpdate,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
    current_user: Annotated[User, Depends(deps.get_current_active_user)],
) -> IUserRead:
    if user_in.email and await crud.user.get_by_email(db, email=user_in.email):
        raise HTTPException(status_code=400, detail="There is already a user with same email")
    return await crud.user.update(db, obj_db=current_user, obj_in=user_in)


@router.put("/{user_id}")
async def update_user(
    *,
    user_id: int,
    user_in: IUserUpdateAdmin,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
    _: Annotated[User, Depends(deps.get_current_active_superuser)],
) -> IUserRead:
    user = await crud.user.get(db, id_=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user_in.email and (user_db := await crud.user.get_by_email(db, email=user_in.email)) and user.id != user_db.id:
        raise HTTPException(status_code=400, detail="There is already a user with same email")
    return await crud.user.update(db, obj_db=user, obj_in=user_in)


@router.delete("/{user_id}")
async def delete_user(
    *,
    user_id: int,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
    current_superuser: Annotated[User, Depends(deps.get_current_active_superuser)],
) -> IUserRead:
    if current_superuser.id == user_id:
        raise HTTPException(status_code=400, detail="Users can't delete themself")

    user = await crud.user.get(db, id_=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return await crud.user.remove(db, id_=user_id)
