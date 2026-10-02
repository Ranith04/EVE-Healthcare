from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass
