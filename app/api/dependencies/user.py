from fastapi import Depends

from app.application import RegisterUserUseCase
from app.infrastructure.password_hasher import PasswordHasher
from app.infrastructure.persistence.database.engine import SessionLocal
from app.infrastructure.persistence.repositories import UserRepository
from app.infrastructure.unit_of_work import UnitOfWork


def get_unit_of_work() -> UnitOfWork:
    return UnitOfWork(SessionLocal)

def get_password_hasher() -> PasswordHasher:
    return PasswordHasher()

def get_user_repository() -> UserRepository:
    return UserRepository(SessionLocal())

def get_register_user(
        uow: UnitOfWork = Depends(get_unit_of_work),
        password_hasher: PasswordHasher = Depends(get_password_hasher)
    ) -> RegisterUserUseCase:
    return RegisterUserUseCase(uow, password_hasher)