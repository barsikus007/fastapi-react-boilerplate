from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, Params
from sqlmodel.ext.asyncio.session import AsyncSession

from src import crud
from src.api import deps
from src.core.config import settings
from src.models import User
from src.models.user import User
from src.schemas.user import IUserCreate, IUserRead, IUserUpdate
from src.schemas.common import (
    IGetResponseBase,
    IPostResponseBase,
    IPutResponseBase,
    IDeleteResponseBase,
)


router = APIRouter()


@router.get("/", response_model=IGetResponseBase[Page[IUserRead]])
async def read_users_list(
    *,
    params: Params = Depends(),
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    users = await crud.user.get_multi(db, params=params)
    return IGetResponseBase[Page[IUserRead]](data=users)


@router.post("/", response_model=IPostResponseBase[IUserRead])
async def create_user(
    *,
    new_user: IUserCreate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_superuser),
):
    user = await crud.user.get_by_email(db, email=new_user.email)
    if user:
        raise HTTPException(status_code=400, detail="There is already a user with same email")
    user = await crud.user.create(db, obj_in=new_user)
    return IPostResponseBase[IUserRead](data=user)


@router.get("/me", response_model=IGetResponseBase[IUserRead])
async def get_my_data(
    *,
    current_user: User = Depends(deps.get_current_active_user),
):
    return IGetResponseBase[IUserRead](data=IUserRead.from_orm(current_user))


@router.put("/me", response_model=IPutResponseBase[IUserRead])
def update_user_me(
    *,
    db: AsyncSession = Depends(deps.get_db),
    user_in: IUserUpdate,
    current_user: User = Depends(deps.get_current_active_user),
):
    if await crud.user.get_by_email(db, email=user_in.email):
        raise HTTPException(status_code=400, detail="There is already a user with same email")
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    print(user)
    return IPutResponseBase[IUserRead](data=user)


@router.delete("/{user_id}", response_model=IDeleteResponseBase[IUserRead])
async def remove_user(
    *,
    user_id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_superuser),
):
    if current_user.id == user_id:
        raise HTTPException(status_code=404, detail="Users can not delete theirselfs")

    user = await crud.user.get(db, id_=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User no found")

    user = await crud.user.remove(db, id_=user_id)
    return IDeleteResponseBase[IUserRead](
        data=user
    )


@router.get("/{user_id}", response_model=IGetResponseBase[IUserRead])
async def get_user_by_id(
    *,
    user_id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    if user_id == current_user.id:
        return current_user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    user = await crud.user.get(db, id_=user_id)
    return IGetResponseBase[IUserRead](data=user)


@router.put("/{user_id}", response_model=IPutResponseBase[IUserRead])
async def update_user(
    *,
    db: AsyncSession = Depends(deps.get_db),
    user_id: int,
    user_in: IUserUpdate,
    current_user: User = Depends(deps.get_current_active_superuser),
):
    if await crud.user.get_by_email(db, email=user_in.email):
        raise HTTPException(status_code=400, detail="There is already a user with same email")
    user = await crud.user.get(db, id_=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    user = await crud.user.update(db, obj_db=user, obj_in=user_in)
    return IPutResponseBase[IUserRead](data=user)
