from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from sqlalchemy import DateTime, ForeignKey, Identity, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.models.base import DeclarativeBase

if TYPE_CHECKING:
    from app.infrastructure.models.orders import Order
    from app.infrastructure.models.products import Product

class OrderItem(DeclarativeBase):
    __tablename__ = 'order_items'
    
    id: Mapped[int] = mapped_column(Integer, Identity(always=True), primary_key=True)
    order_id: Mapped[Order] = mapped_column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id: Mapped[Product] = mapped_column(Integer, ForeignKey('products.id'), nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=datetime.now(ZoneInfo('America/Bogota'))
    )
    
    order: Mapped[Order] = relationship(back_populates='order_items')
    product: Mapped[Product] = relationship(back_populates='order_items')