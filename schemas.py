from decimal import Decimal
from re import fullmatch
from typing import *
from datetime import datetime

from annotated_types import *
from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    PositiveInt,
    ConfigDict,
    field_validator,
    model_validator,
    validate_call,
    SecretStr,
    PostgresDsn
)
from pydantic.alias_generators import to_camel
from pydantic_settings import BaseSettings, SettingsConfigDict

PasswordStr = Annotated[
    str,
    MinLen(8),
    MaxLen(72),
    Predicate(
        func=lambda x: fullmatch(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,72}$", x) is not None
    )
]


class RegisterForm(BaseModel):
    email: Optional[EmailStr] = Field(default=None, validate_default=True)
    password: PasswordStr
    confirm_password: PasswordStr = Field(alias="confirmPassword", validate_default=True)
    age: int = Field(
        default=...,
        ge=18,
        lt=100
    )

    @model_validator(mode="before")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("пароли не совпадают")
        return self


class DTO(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        ser_json_bytes="base64",
        ser_json_timedelta="float",
        allow_inf_nan=False,
        from_attributes=True,
        str_strip_whitespace=True,
        alias_generator=to_camel
    )


class ProductDTO(DTO):
    model_config = ConfigDict()

    id: PositiveInt
    article: str = Field()
    price: Decimal = Field(max_digits=8, decimal_places=2)
    status: Literal[
        "new",
        "old"
    ]


class CategoryDTO(DTO):
    id: PositiveInt = Field(alias="pk")
    name: str = Field(min_length=2)
    products: Optional[list[ProductDTO]] = Field(default=None, min_length=1)
    parent_category: Optional["CategoryDTO"] = Field(default=None)

    @field_validator("surname", "name", mode="before", check_fields=False)
    def validator(cls, value):
        return value

data = {
    "pk": 1,
    "name": "Coffee",
    "products": [
        {
            "id": 1,
            "article": "Latte",
            "price": 5.5
        },
        {
            "id": 2,
            "article": "Cappuccino",
            "price": 4.45
        }
    ],
    "parent_category": {
        "pk": 2,
        "name": "Hot Drinks"
    }
}
# c = CategoryDTO.model_construct(**data)
# print(c)
# print(
#     c.model_dump_json(
#         indent=2,
#         exclude_none=True,
#         exclude_defaults=True,
#         exclude={"price"},
#         by_alias=True
#     )
# )


# @validate_call()
# def foo(a: int, b):
#     pass
#
#
# foo("343434fdf", [])
# from aiogram.types import Message


class A(BaseModel):
    date: datetime
    key: SecretStr
    dsn: PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        extra="ignore"
    )

    database_url: PostgresDsn


# s = Settings()
# print(s)
