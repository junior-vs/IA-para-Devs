# API RESTful Flask - Estrutura Completa

## 1. Estrutura de Pastas

```shell
  $ tree

flask-api/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   └── product.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── users/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── serializers.py
│   │   └── products/
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       └── serializers.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── external_api_service.py
│   │   └── cache_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   ├── validators.py
│   │   ├── helpers.py
│   │   └── exceptions.py
│   └── schemas/
│       ├── __init__.py
│       ├── user_schema.py
│       └── product_schema.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_products.py
│   └── fixtures/
│       ├── __init__.py
│       └── sample_data.py
├── migrations/
├── logs/
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── nginx.conf
├── scripts/
│   ├── init_db.py
│   └── seed_data.py
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── .gitignore
├── pytest.ini
├── run.py
└── README.md
```

## 2. Configuração do Ambiente

### requirements.txt
```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.5
Flask-JWT-Extended==4.6.0
Flask-RESTX==1.3.0
Flask-Cors==4.0.0
Flask-Limiter==3.5.0
psycopg2-binary==2.9.9
redis==5.0.1
celery==5.3.4
requests==2.31.0
python-dotenv==1.0.0
marshmallow==3.20.1
bcrypt==4.1.2
gunicorn==21.2.0
```

### requirements-dev.txt
```txt
-r requirements.txt
pytest==7.4.3
pytest-flask==1.3.0
pytest-cov==4.1.0
pytest-mock==3.12.0
factory-boy==3.3.0
black==23.11.0
flake8==6.1.0
pre-commit==3.6.0
```

### .env.example
```env
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/flask_api
TEST_DATABASE_URL=postgresql://user:password@localhost:5432/flask_api_test

# Redis
REDIS_URL=redis://localhost:6379/0

# External APIs
EXTERNAL_API_BASE_URL=https://api.example.com
EXTERNAL_API_KEY=your-api-key

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# Rate Limiting
RATELIMIT_STORAGE_URL=redis://localhost:6379/1
```

## 3. Configuração Principal

### app/config.py
```python
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    # Rate Limiting
    RATELIMIT_STORAGE_URL = os.environ.get('RATELIMIT_STORAGE_URL')
    RATELIMIT_DEFAULT = "1000 per day, 100 per hour"
    
    # External APIs
    EXTERNAL_API_BASE_URL = os.environ.get('EXTERNAL_API_BASE_URL')
    EXTERNAL_API_KEY = os.environ.get('EXTERNAL_API_KEY')
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FILE = os.environ.get('LOG_FILE', 'logs/app.log')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://user:password@localhost:5432/flask_api'

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'postgresql://user:password@localhost:5432/flask_api_test'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

### app/extensions.py
```python
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis

# Extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()
redis_client = redis.Redis()

# Rate Limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["1000 per day", "100 per hour"]
)

# API Documentation
authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api = Api(
    title='Flask API',
    version='1.0',
    description='Uma API RESTful robusta com Flask',
    doc='/docs/',
    authorizations=authorizations,
    security='Bearer Auth'
)
```

### app/__init__.py
```python
import logging
import os
from flask import Flask
from app.config import config
from app.extensions import db, migrate, jwt, cors, limiter, api, redis_client
from app.utils.exceptions import register_error_handlers

def create_app(config_name=None):
    """Application factory pattern."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)
    limiter.init_app(app)
    api.init_app(app)
    
    # Setup Redis
    redis_client.from_url(app.config['REDIS_URL'])
    
    # Setup logging
    setup_logging(app)
    
    # Register blueprints
    register_blueprints(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # JWT callbacks
    setup_jwt_callbacks(app)
    
    return app

def register_blueprints(app):
    """Register all blueprints."""
    from app.api.auth import auth_bp
    from app.api.users import users_bp
    from app.api.products import products_bp
    
    api.add_namespace(auth_bp, path='/api/auth')
    api.add_namespace(users_bp, path='/api/users')
    api.add_namespace(products_bp, path='/api/products')

def setup_logging(app):
    """Setup application logging."""
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        file_handler = logging.FileHandler(app.config['LOG_FILE'])
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(getattr(logging, app.config['LOG_LEVEL']))
        app.logger.addHandler(file_handler)
        app.logger.setLevel(getattr(logging, app.config['LOG_LEVEL']))

def setup_jwt_callbacks(app):
    """Setup JWT callbacks."""
    from flask_jwt_extended import get_jwt_identity
    from app.models.user import User
    
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()
```

## 4. Models

### app/models/base.py
```python
from datetime import datetime
from app.extensions import db

class BaseModel(db.Model):
    """Base model with common fields."""
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def save(self):
        """Save instance to database."""
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        """Delete instance from database."""
        db.session.delete(self)
        db.session.commit()
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
```

### app/models/user.py
```python
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.models.base import BaseModel

class User(BaseModel):
    """User model."""
    __tablename__ = 'users'
    
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    
    def set_password(self, password):
        """Set password hash."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password against hash."""
        return check_password_hash(self.password_hash, password)
    
    @property
    def full_name(self):
        """Get full name."""
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f'<User {self.username}>'
```

### app/models/product.py
```python
from app.extensions import db
from app.models.base import BaseModel

class Product(BaseModel):
    """Product model."""
    __tablename__ = 'products'
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    
    # Relationship
    category = db.relationship('Category', backref='products')
    
    def __repr__(self):
        return f'<Product {self.name}>'

class Category(BaseModel):
    """Category model."""
    __tablename__ = 'categories'
    
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Category {self.name}>'
```

## 5. Schemas/Serializers

### app/schemas/user_schema.py
```python
from marshmallow import Schema, fields, validate, post_load
from app.models.user import User

class UserSchema(Schema):
    """User serialization schema."""
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True, validate=validate.Length(max=120))
    username = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    first_name = fields.Str(required=True, validate=validate.Length(max=50))
    last_name = fields.Str(required=True, validate=validate.Length(max=50))
    full_name = fields.Str(dump_only=True)
    is_active = fields.Bool(dump_only=True)
    is_admin = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UserUpdateSchema(Schema):
    """User update schema."""
    email = fields.Email(validate=validate.Length(max=120))
    username = fields.Str(validate=validate.Length(min=3, max=80))
    first_name = fields.Str(validate=validate.Length(max=50))
    last_name = fields.Str(validate=validate.Length(max=50))
    password = fields.Str(load_only=True, validate=validate.Length(min=6))

class LoginSchema(Schema):
    """Login schema."""
    email = fields.Email(required=True)
    password = fields.Str(required=True)

# Schema instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_update_schema = UserUpdateSchema()
login_schema = LoginSchema()
```

## 6. Services

### app/services/auth_service.py
```python
from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from app.models.user import User
from app.extensions import db
from app.utils.exceptions import AuthenticationError, ValidationError

class AuthService:
    """Authentication service."""
    
    @staticmethod
    def authenticate_user(email, password):
        """Authenticate user with email and password."""
        user = User.query.filter_by(email=email, is_active=True).first()
        
        if not user or not user.check_password(password):
            raise AuthenticationError("Invalid credentials")
        
        return user
    
    @staticmethod
    def generate_tokens(user):
        """Generate access and refresh tokens."""
        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)
        
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_type': 'Bearer'
        }
    
    @staticmethod
    def register_user(user_data):
        """Register new user."""
        # Check if user already exists
        existing_user = User.query.filter(
            (User.email == user_data['email']) | 
            (User.username == user_data['username'])
        ).first()
        
        if existing_user:
            raise ValidationError("User already exists")
        
        # Create new user
        user = User(**user_data)
        user.set_password(user_data['password'])
        
        db.session.add(user)
        db.session.commit()
        
        return user
```

### app/services/external_api_service.py
```python
import requests
from flask import current_app
from typing import Dict, Any, Optional
from app.utils.exceptions import ExternalAPIError

class ExternalAPIService:
    """Service for consuming external APIs."""
    
    def __init__(self):
        self.base_url = current_app.config['EXTERNAL_API_BASE_URL']
        self.api_key = current_app.config['EXTERNAL_API_KEY']
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[Any, Any]:
        """Make HTTP request to external API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                timeout=30,
                **kwargs
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout:
            raise ExternalAPIError("Request timeout")
        except requests.exceptions.ConnectionError:
            raise ExternalAPIError("Connection error")
        except requests.exceptions.HTTPError as e:
            raise ExternalAPIError(f"HTTP error: {e.response.status_code}")
        except Exception as e:
            raise ExternalAPIError(f"Unexpected error: {str(e)}")
    
    def get_external_data(self, resource_id: str) -> Dict[Any, Any]:
        """Get data from external API."""
        return self._make_request('GET', f'/resources/{resource_id}')
    
    def post_external_data(self, data: Dict[Any, Any]) -> Dict[Any, Any]:
        """Post data to external API."""
        return self._make_request('POST', '/resources', json=data)
    
    def update_external_data(self, resource_id: str, data: Dict[Any, Any]) -> Dict[Any, Any]:
        """Update data in external API."""
        return self._make_request('PUT', f'/resources/{resource_id}', json=data)
```

## 7. Utilities

### app/utils/exceptions.py
```python
class APIException(Exception):
    """Base API exception."""
    status_code = 500
    message = "Internal server error"
    
    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__()
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

class ValidationError(APIException):
    status_code = 400
    message = "Validation error"

class AuthenticationError(APIException):
    status_code = 401
    message = "Authentication required"

class AuthorizationError(APIException):
    status_code = 403
    message = "Insufficient permissions"

class NotFoundError(APIException):
    status_code = 404
    message = "Resource not found"

class ExternalAPIError(APIException):
    status_code = 502
    message = "External API error"

def register_error_handlers(app):
    """Register global error handlers."""
    
    @app.errorhandler(APIException)
    def handle_api_exception(error):
        response = {
            'error': error.message,
            'status_code': error.status_code
        }
        if error.payload:
            response.update(error.payload)
        return response, error.status_code
    
    @app.errorhandler(404)
    def handle_not_found(error):
        return {'error': 'Endpoint not found'}, 404
    
    @app.errorhandler(500)
    def handle_internal_error(error):
        return {'error': 'Internal server error'}, 500
```

### app/utils/decorators.py
```python
from functools import wraps
from flask import request, current_app
from flask_jwt_extended import jwt_required, get_current_user
from app.utils.exceptions import AuthorizationError, ValidationError

def admin_required(f):
    """Decorator to require admin privileges."""
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        current_user = get_current_user()
        if not current_user.is_admin:
            raise AuthorizationError("Admin privileges required")
        return f(*args, **kwargs)
    return decorated_function

def validate_json(schema):
    """Decorator to validate JSON input."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                validated_data = schema.load(request.json or {})
                request.validated_data = validated_data
                return f(*args, **kwargs)
            except Exception as e:
                raise ValidationError(str(e))
        return decorated_function
    return decorator
```

Continuando na próxima parte com os endpoints, testes e Docker...
