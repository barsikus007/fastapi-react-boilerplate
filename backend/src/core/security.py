from datetime import UTC, datetime, timedelta
from typing import Any

import bcrypt
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
