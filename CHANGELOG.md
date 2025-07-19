# Changelog

## [1.0.0] - 2025-07-13
### Added
- Servicio de **registro de usuarios** (`/auth/register`) con:
  - Validación de email único.
  - Hash de contraseñas con bcrypt.
  - Asignación automática de rol "cuidador".

- Servicio de **login de usuarios** (`/auth/login`) con:
  - Validación de credenciales.
  - Generación de token JWT incluyendo el email y el rol.
  - Duración configurable del token por variable de entorno.

- **Esquemas Pydantic** para validar:
  - Registro (`UserCreate`).
  - Login (`UserLogin`).
  - Token (`Token`).

- **Modelo de base de datos MongoDB**:
  - Conexión a la colección `caretaker` en la base `conectacare_caretaker`.
  - Funciones de consulta por email y creación de usuario.

- **Configuración centralizada**:
  - Archivo `config.py` para leer `.env` (Mongo URI, clave secreta JWT, algoritmo y expiración).
  - Variables de entorno documentadas en `.env.example`.

- **Seguridad JWT**:
  - Funciones para generar tokens (`create_access_token`), hashear y verificar contraseñas.
  - Algoritmo de encriptación: HS256.

- **Dependencia `get_current_user`**:
  - Archivo `app/dependencies/auth.py`.
  - Valida el token JWT recibido en el header Authorization.
  - Decodifica el token y retorna el id del usuario autenticado.

- **Observabilidad básica** con Prometheus:
  - Contadores de peticiones.
  - Tiempos de respuesta por endpoint.
  - Conteo de errores por endpoint.
  - Endpoint `/metrics` disponible para Prometheus.

- **Rulesets en GitHub configurados**:
  - Protección de ramas `main` y `develop`.
  - Revisión de PRs antes de merge.
  - GitGuardian configurado para escanear secretos.

### Fixed
- Problema de importaciones resuelto mediante la configuración de `PYTHONPATH` y ajuste en `settings.json` de VS Code.

### Security
- `.env` agregado a `.gitignore` para evitar exposición de claves sensibles.
- Rotación de la clave JWT tras detección de GitGuardian.

---

## [Unreleased]
- Implementación de endpoints de recuperación de contraseña.
- Login con OAuth providers (Google, etc).
