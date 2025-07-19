# ConectaCare - Servicio de Login & Registro

Servicio backend para la autenticación de cuidadores en ConectaCare. Permite el registro y login de usuarios con protección JWT, así como observabilidad con Prometheus.

## 🗂️ Estructura
app/
│
├── api/v1/ # Endpoints: login, registro
├── core/ # Configuración, seguridad JWT
├── config/ # Conexión MongoDB
├── repositories/ # Acceso a datos (Mongo)
├── schemas/ # Validaciones Pydantic
├── services/ # Lógica de negocio auth
├── dependencies/ # Dependencias como get_current_user
└── main.py # Punto de entrada FastAPI

## ⚙️ Configuración

### Variables de entorno (.env)

Crea un archivo `.env` en la raíz del proyecto basado en el `.env.example`:

MONGO_URI=<URI de conexión MongoDB>
JWT_SECRET_KEY=<Clave secreta segura>
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

### Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar entorno:
```bash
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución del servidor
Para correr la aplicación en modo desarrollo:
```bash
uvicorn app.main:app --reload --port 3003
```

Accede a la documentación Swagger:
```arduino
http://127.0.0.1:3003/docs
```

## Endpoints principales
POST /auth/register: Registrar un nuevo cuidador.

POST /auth/login: Login con email y contraseña. Retorna un token JWT.

GET /metrics: Exposición de métricas para Prometheus.

📊 Observabilidad
Incluye instrumentación básica con Prometheus:

Conteo de peticiones.

Tiempos de respuesta.

Excepciones por endpoint.

Para visualizar métricas:
```arduino
http://127.0.0.1:3003/metrics
```

Si deseas integrar un dashboard Prometheus, agrega en tu archivo prometheus.yml:

```yaml
scrape_configs:
  - job_name: 'fastapi-backend-login'
    static_configs:
      - targets: ['localhost:3003']
```

🔒 Seguridad
Contraseñas encriptadas con bcrypt.

Autenticación vía JWT.

.env protegido en .gitignore.

🧩 Extensiones futuras
Recuperación de contraseña.

Soporte OAuth con Google.

Tests unitarios y de integración en repositorio dedicado.


🛠️ Desarrollado por el equipo **ConectaCare**.