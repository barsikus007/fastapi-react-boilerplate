from pydantic import BaseModel

# from .user import IUserRead


class Token(BaseModel):
    access_token: str
    token_type: str
    # refresh_token: str
    # user: IUserRead


class TokenRead(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):  #DEL
    sub: int | None = None  #DEL


# class RefreshToken(BaseModel):
#     refresh_token: str
