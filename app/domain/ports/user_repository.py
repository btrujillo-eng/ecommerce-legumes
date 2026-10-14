from abc import ABC, abstractmethod

from pydantic import EmailStr

from app.api.schemas import UserCreateRequest, UserResponse
from app.infrastructure.models.users import User


class IUserRepository(ABC):
    """
    Interface for user repository.
    
    Any class that impelement this interface must define 'get_user_by_email', 'add_user' methods.
    """
    @abstractmethod
    async def get_user_by_email(self, email: EmailStr) -> User | None: ...
    
    @abstractmethod
    async def add_user(self, user_data: UserCreateRequest, password_hash: str) -> UserResponse: ...