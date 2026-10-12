from abc import ABC, abstractmethod
from types import TracebackType
from typing import Self

from app.domain.ports import IUserRepository


class IUnitOfWork(ABC):
    # The property decorator allows the function to be treated as an entity. 
    @property
    @abstractmethod
    def user(self) -> IUserRepository | None: ...
    
    @abstractmethod
    def commit(self) -> None: ...
    
    @abstractmethod
    def rollback(self) -> None: ...
    
    @abstractmethod
    def __aenter__(self) -> Self: ...
    
    @abstractmethod
    def __aexit__(self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_tb: TracebackType | None
    ) -> bool | None: ...