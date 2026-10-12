from app.api.schemas import UserCreateRequest, UserResponse
from app.domain import IPasswordHasher, IUnitOfWork
from app.exceptions import RepositoryNotInitializedError


class RegisterUserUseCase:
    def __init__(self, uow: IUnitOfWork, password_hasher: IPasswordHasher):
        self.uow = uow
        self.password_hasher = password_hasher
        
    def register(self, user_data: UserCreateRequest) -> UserResponse:
        password_hash = self.password_hasher.apply_hash(user_data.password)
        with self.uow as uow:
            if uow.user is None:
                raise RepositoryNotInitializedError("The user repository is not initialized")
            
            user = uow.user.add_user(user_data, password_hash.get_secret_value())
            uow.commit()
            return user
        