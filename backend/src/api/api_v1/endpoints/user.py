from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, Params
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from src import crud
from src.api import deps
from src.models import User
from src.api.deps import get_db
from src.models.user import User, UserRead, UserCreate
from src.schemas.user import IUserCreate, IUserRead, IUserReadWithoutGroups
from app.schemas.common import (
    IDeleteResponseBase,
    IGetResponseBase,
    IPostResponseBase,
)


router = APIRouter()


@router.get("/user", response_model=IGetResponseBase[Page[IUserReadWithoutGroups]])
async def read_users_list(    
    params: Params = Depends(),
    db_session: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    """
    Retrieve users.
    """    
    users = await crud.user.get_multi_paginated(db_session, params=params)
    return IGetResponseBase[Page[IUserReadWithoutGroups]](data=users)

@router.get("/user/order_by_created_at", response_model=IGetResponseBase[Page[IUserReadWithoutGroups]])
async def get_hero_list_order_by_created_at(
    params: Params = Depends(),
    db_session: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user)
):
    query = select(User).order_by(User.created_at)
    users = await crud.user.get_multi_paginated(db_session, query=query, params=params)
    return IGetResponseBase[Page[IUserReadWithoutGroups]](data=users)

@router.get("/user/{user_id}", response_model=IGetResponseBase[IUserRead])
async def get_user_by_id(
    user_id: int,
    db_session: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user),
):
    user = await crud.user.get_user_by_id(db_session, id=user_id)
    return IGetResponseBase[IUserRead](data=user)

@router.get("/user", response_model=IGetResponseBase[IUserRead])
async def get_my_data(
    current_user: User = Depends(deps.get_current_active_user),
):
    return IGetResponseBase[IUserRead](data=current_user)

@router.post("/user", response_model=IPostResponseBase[IUserRead])
async def create_user(
    new_user: IUserCreate,
    db_session: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_superuser),
):    
    user = await crud.user.get_by_email(db_session, email=new_user.email)
    if user:
        raise HTTPException(status_code=404, detail="There is already a user with same email")
    user = await crud.user.create(db_session, obj_in=new_user)
    return IPostResponseBase[IUserRead](data=user)


@router.delete("/user/{user_id}", response_model=IDeleteResponseBase[IUserRead])
async def remove_user(
    user_id: int,
    db_session: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_superuser),
):
    if current_user.id == user_id:
        raise HTTPException(status_code=404, detail="Users can not delete theirselfs")

    user = await crud.user.get_user_by_id(db_session=db_session, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User no found")    
    user = await crud.user.remove(db_session, id=user_id)
    return IDeleteResponseBase[IUserRead](
        data=user
    )





@router.patch("/user/{user_id}", response_model=UserRead)
async def year_user(user_id: int, year: int, session: AsyncSession = Depends(get_db)) -> UserRead:
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Student not found")
    user.year = year
    await session.commit()
    print(user)
    return user


@router.get("/user/{user_id}", response_model=UserRead)
async def get_user(user_id: int, session: AsyncSession = Depends(get_db)) -> UserRead:
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Student not found")
    return user


@router.get("/users", response_model=list[UserRead])
async def get_users(
        offset: int = 0, limit: int = Query(default=100, lte=100),
        session: AsyncSession = Depends(get_session)) -> list[UserRead]:
    result = await session.exec(select(User).offset(offset).limit(limit))
    return result.all()


@router.post("/user", response_model=UserRead)
async def add_user(user: UserCreate, session: AsyncSession = Depends(get_db)) -> UserRead:
    user = User(**user.dict())
    session.add(user)
    await session.commit()
    # Seems, that refreshing is not necessary
    # await session.refresh(user)
    return user
