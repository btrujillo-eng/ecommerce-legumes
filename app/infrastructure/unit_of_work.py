from types import TracebackType
from typing import Self

from sqlalchemy.orm import Session, sessionmaker

from app.domain.ports import IUnitOfWork
from app.exceptions import UnitWorkIsInactiveError
from app.infrastructure.persistence.repositories.postgresql import UserRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self, session_factory: sessionmaker[Session]):
        self.session_factory = session_factory
        self.session: Session | None = None
        self._users: UserRepository | None = None
     
    @property
    def user(self) -> UserRepository | None:
        return self._users 
        
    def __aenter__(self) -> Self:
        self.session = self.session_factory()
        
        self._users = UserRepository(self.session)
        return self
        
    def __aexit__(
        self, 
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None, 
        exc_tb: TracebackType | None
        ) -> bool | None:
        try:
            if exc_type is not None:
                self.rollback()
        finally:
            if self.session is not None:
                self.session.close()
                self.session = None
                self._users = None
            
    def commit(self) -> None:
        if self.session is None:
            raise UnitWorkIsInactiveError("Unit work is not active")
        self.session.commit()
        
    def rollback(self) -> None:
        if self.session is not None:
           self.session.rollback()