from datetime import UTC, datetime, timedelta
from typing import Any

import bcrypt
from fastapi import HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt

from src.core.config import settings

ALGORITHM = "HS256"


def create_access_token(
    subject: str | Any,
    expires_delta: timedelta,
) -> str:
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expire, "sub": str(subject), "type": "access"}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password_enc = plain_password.encode("utf-8")
    hashed_password_enc = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password=plain_password_enc, hashed_password=hashed_password_enc)


def get_password_hash(password: str) -> str:
    password_enc = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=password_enc, salt=salt)
    return hashed_password.decode("utf-8")


class OAuth2PasswordBearerCookie(OAuth2PasswordBearer):
    """
    Modified OAuth2PasswordBearer to accept token from cookie too
    Based on https://gist.github.com/nilsdebruin/b0b97d1a2e9048645d72cd8bff64d5f4
    """

    async def __call__(self, request: Request) -> str | None:
        header_authorization = request.headers.get("Authorization")
        cookie_authorization = request.cookies.get("Authorization")
        scheme, param = get_authorization_scheme_param(header_authorization)

        header_scheme, header_param = get_authorization_scheme_param(
            header_authorization,
        )
        cookie_scheme, cookie_param = get_authorization_scheme_param(
            cookie_authorization,
        )

        if header_scheme.lower() == "bearer":
            authorization = True
            scheme = header_scheme
            param = header_param

        elif cookie_scheme.lower() == "bearer":
            authorization = True
            scheme = cookie_scheme
            param = cookie_param

        else:
            authorization = False

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return None
        return param
