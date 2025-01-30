from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from src import crud
from src.api import deps
from src.core import security
from src.core.config import settings
from src.schemas.token import TokenRead

router = APIRouter()


@router.post("")
async def login(
    email: Annotated[EmailStr, Body()],
    password: Annotated[str, Body()],
    response: Response,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
) -> TokenRead:
    """
    Login for all users
    """
    user = await crud.user.authenticate(db, email=email, password=password)
    if not user:
        raise HTTPException(status_code=400, detail="Email or Password incorrect")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="User is inactive")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(user.id, expires_delta=access_token_expires)

    response.set_cookie(
        "Authorization",
        value=f"Bearer {access_token}",
        max_age=1800,  # TODO extract const
        expires=1800,
        **security.COOKIE_PARAMS,
    )

    return TokenRead(
        access_token=access_token,
        token_type="bearer",
    )


@router.post("/access-token")
async def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    response: Response,
    db: Annotated[AsyncSession, Depends(deps.get_db)],
) -> TokenRead:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    return await login(form_data.username, form_data.password, response, db)


@router.get("/logout")
async def route_logout_and_remove_cookie():
    response = Response(status_code=status.HTTP_204_NO_CONTENT)
    response.delete_cookie("Authorization", **security.COOKIE_PARAMS)
    return response
