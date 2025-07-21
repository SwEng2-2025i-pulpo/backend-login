from fastapi import HTTPException, status
from app.core.config import get_settings
from app.core.security import hash_password, create_access_token, verify_password
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin
from app.schemas.token import Token
from pymongo.errors import DuplicateKeyError

settings = get_settings()
user_repo = UserRepository()

class AuthService:
    def sign_up_user(self, user_data: UserCreate):
        existing_user = user_repo.find_by_email(user_data.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="El correo ya está registrado")

        hashed_password = hash_password(user_data.password)

        new_user = {
            "name": user_data.name,
            "last_name": user_data.last_name,
            "email": user_data.email,
            "passwordHash": hashed_password,
            "role": "cuidador"
        }

        try:
            user_repo.create_user(new_user)
        except DuplicateKeyError:
            raise HTTPException(status_code=400, detail="Error al registrar el usuario")

        return {"msg": "Usuario registrado correctamente"}

    def login_user(self, credentials: UserLogin) -> Token:
        user = user_repo.find_by_email(credentials.email)
        if not user or not verify_password(credentials.password, user["passwordHash"]):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        # token_data = {"sub": user["email"], "role": user["role"]}
        token_data = {
        "sub": str(user["_id"]),      # aquí guardamos el ID del cuidador
        "email": user["email"],
        "role": user["role"]
        }

        token = create_access_token(data=token_data)

        return Token(access_token=token, token_type="bearer")
