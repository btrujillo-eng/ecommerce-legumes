import logging
from datetime import UTC, datetime
from uuid import uuid4

from app.core import IPaymentGateway, PaymentMethods
from app.schemas import PaymentResponse
from app.schemas.payment import BasePaymentData, CashPaymentResponse

logger = logging.getLogger(__name__)

class CashGateway(IPaymentGateway):
    def process_payment(self, payment_data: BasePaymentData) -> PaymentResponse:
        transaction_id = str(uuid4())
        logger.info("Payment processed successfully | Transaction ID: %s", transaction_id)
        
        return PaymentResponse(
            currency=payment_data.currency,
            transaction_amount=payment_data.transaction_amount,
            transaction_id=transaction_id,
            payment_status="succeeded",
            message="Pago exitoso",
            created_at=datetime.now(tz=UTC),
            payment_method=CashPaymentResponse(
                method=PaymentMethods.CASH
            )
        )