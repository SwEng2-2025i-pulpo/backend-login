# Changelog

## [Unreleased]
- Endpoints de pacientes protegidos con JWT
- Creación de pacientes asociados al cuidador autenticado

## [v0.1.0] - 2025-07-12
### Added
- Endpoint `/auth/register`: Registro de cuidadores con validaciones (nombre, apellido, correo, contraseña y confirmación).
- Endpoint `/auth/login`: Autenticación de usuarios y generación de JWT con email, rol y expiración.
- Validación de contraseñas con mínimo 8 caracteres y confirmación igual.
- Configuración de seguridad JWT en `core/security.py`.
- Conexión a MongoDB configurada vía `.env`.
