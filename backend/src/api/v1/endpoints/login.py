from datetime import timedelta

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from src import crud
from src.api import deps
from src.core import security
from src.core.config import settings
from src.schemas.token import Token, TokenRead


router = APIRouter()


@router.post("/", status_code=201)
async def login(
    email: EmailStr = Body(...),
    password: str = Body(...),
    db_session: AsyncSession = Depends(deps.get_db),
) -> Token:
    """
    Login for all users
    """
    user = await crud.user.authenticate(db_session, email=email, password=password)
    if not user:
        raise HTTPException(status_code=400, detail="Email or Password incorrect")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="User is inactive")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(user.id, expires_delta=access_token_expires)
    return Token(
        access_token=access_token,
        token_type="bearer",
    )


@router.post("/access-token")
async def login_access_token(
    db_session: AsyncSession = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> TokenRead:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = await crud.user.authenticate(
        db_session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(user.id, expires_delta=access_token_expires)
    return TokenRead(
        access_token=access_token,
        token_type="bearer",
    )
