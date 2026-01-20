from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    auth: str
    created_at: datetime | None = Field(default_factory=datetime.now)
    banned: bool = False

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    author: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    expires_at: datetime | None = None
    is_private: bool | None = False
    url: str