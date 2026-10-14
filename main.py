from fastapi import FastAPI

from app.api.v1.routers import health, payment, user

app = FastAPI(
    title="Payment Processor API",
    version="1.0.1"
)

app.include_router(payment.router)
app.include_router(health.router)
app.include_router(user.router)