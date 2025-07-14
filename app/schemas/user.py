from pydantic import BaseModel, EmailStr, Field, field_validator, FieldValidationInfo

# Modelo para login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Modelo para registro
class UserCreate(BaseModel):
    name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, confirm_password: str, info: FieldValidationInfo):
        if confirm_password != info.data.get("password"):
            raise ValueError("Las contraseñas no coinciden")
        return confirm_password

# Modelo para usuario almacenado o retornado
class User(BaseModel):
    id: str
    name: str
    last_name: str
    email: EmailStr
    role: str