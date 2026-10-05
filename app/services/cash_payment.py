from app.core import IPaymentGateway, IPaymentProcessor
from app.schemas import BasePaymentData, PaymentResponse


class CashPaymentProcessor(IPaymentProcessor):
    
    def __init__(self, cash_gateway: IPaymentGateway):
        self.cash_gateway = cash_gateway
    
    def process(self, payment_data: BasePaymentData) -> PaymentResponse:
        response = self.cash_gateway.process_payment(payment_data)
        
        return response