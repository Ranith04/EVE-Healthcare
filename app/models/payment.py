from sqlalchemy import String, DateTime, Numeric, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.db.base import Base
from datetime import datetime
from decimal import Decimal
import enum

class PaymentStatus(str, enum.Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

class PaymentSource(str, enum.Enum):
    API = "API"
    WEBHOOK = "WEBHOOK"

class IdempotencyOutcome(str, enum.Enum):
    APPLIED = "APPLIED"
    IGNORED = "IGNORED"

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.id"), index=True)
    transaction_id: Mapped[str] = mapped_column(String, unique=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus))
    source: Mapped[PaymentSource] = mapped_column(Enum(PaymentSource))
    payment_method: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

class PaymentIdempotency(Base):
    __tablename__ = "payment_idempotency"

    id: Mapped[int] = mapped_column(primary_key=True)
    transaction_id: Mapped[str] = mapped_column(String, unique=True)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.id"))
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus))
    outcome: Mapped[IdempotencyOutcome] = mapped_column(Enum(IdempotencyOutcome))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
