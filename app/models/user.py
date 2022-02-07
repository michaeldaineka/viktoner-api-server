from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from ..db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True, nullable=False)
    is_superuser = Column(Boolean(), default=False)