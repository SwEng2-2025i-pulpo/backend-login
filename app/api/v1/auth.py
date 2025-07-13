from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserLogin
from app.schemas.token import Token
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])
auth_service = AuthService()

@router.post("/register", response_model=dict, status_code=201)
def register(user_data: UserCreate):
    return auth_service.sign_up_user(user_data)

@router.post("/login", response_model=Token)
def login(credentials: UserLogin):
    return auth_service.login_user(credentials)
