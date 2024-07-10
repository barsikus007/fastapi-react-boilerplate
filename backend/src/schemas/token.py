from src.schemas.base import BaseSchema


class Token(BaseSchema):
    access_token: str
    token_type: str


class TokenRead(BaseSchema):
    access_token: str
    token_type: str
