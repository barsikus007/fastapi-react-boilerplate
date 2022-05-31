from typing import Any
from datetime import timedelta

from jose import jwt
from pydantic import EmailStr
from pydantic import ValidationError
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel.ext.asyncio.session import AsyncSession

from src import crud
from src.api import deps
from src.core import security
from src.core.config import settings
# from src.schemas.token import TokenRead, RefreshToken
from src.schemas.token import TokenRead, Token
# from src.schemas.common import IMetaGeneral
from src.schemas.common import IPostResponseBase


router = APIRouter()


@router.post("/login", response_model=IPostResponseBase[Token], status_code=201)
async def login(
    email: EmailStr = Body(...),
    password: str = Body(...),
    db_session: AsyncSession = Depends(deps.get_db),
    # meta_data: IMetaGeneral = Depends(deps.get_general_meta)
) -> Any:
    """
    Login for all users
    """
    user = await crud.user.authenticate(db_session, email=email, password=password)
    if not user:
        raise HTTPException(status_code=400, detail="Email or Password incorrect")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="User is inactive")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # refresh_token_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(user.id, expires_delta=access_token_expires)
    # refresh_token = security.create_refresh_token(user.id, expires_delta=refresh_token_expires)
    data = Token(
        access_token=access_token,
        token_type="bearer",
        # refresh_token=refresh_token,
        # user=user
    )
    return IPostResponseBase[Token](data=data, message="Login correctly")
    # return IPostResponseBase[Token](meta=meta_data, data=data, message="Login correctly")


# @router.post("/login/refresh_token", response_model=IPostResponseBase[TokenRead], status_code=201)
# async def get_refresh_token(
#     body: RefreshToken = Body(...),
#     db_session: AsyncSession = Depends(deps.get_db),
# ) -> Any:
#     """
#     Get Refresh token
#     """
#     try:
#         payload = jwt.decode(body.refresh_token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
#     except (jwt.JWTError, ValidationError):
#         raise HTTPException(status_code=403,detail="Refresh token invalid")

#     if payload['type'] != 'refresh':
#         raise HTTPException(status_code=404,detail="Incorrect token")
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     user = await crud.user.get(db_session, obj_id=int(payload['sub']))
#     if not user:
#         raise HTTPException(status_code=500,detail="!!!Incorrect token!!!")
#     if user.is_active:
#         access_token = security.create_access_token( int(payload['sub']), expires_delta=access_token_expires)         
#         return IPostResponseBase[TokenRead](data=TokenRead(access_token=access_token,token_type= "bearer"), message="Access token generated correctly")
#     else:
#         raise HTTPException(status_code=404,detail="User inactive")


@router.post("/login/access-token", response_model=TokenRead)
async def login_access_token(
    db_session: AsyncSession = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """    
    user = await crud.user.authenticate(
        db_session, email=EmailStr(form_data.username), password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
