param (
    [Parameter(Mandatory = $true)]
    [string]$projeto
)

if (-not $projeto) {
    Write-Host "Uso: .\criar_flask_api.ps1 <nome_do_projeto>"
    exit 1
}

# Estrutura de diretórios
$dirs = @(
    "$projeto/app/models",
    "$projeto/app/api/auth",
    "$projeto/app/api/users",
    "$projeto/app/api/products",
    "$projeto/app/services",
    "$projeto/app/utils",
    "$projeto/app/schemas",
    "$projeto/tests/fixtures",
    "$projeto/migrations",
    "$projeto/logs",
    "$projeto/docker",
    "$projeto/scripts",
    "$projeto/docs/source"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}

# Arquivos principais
$files = @{
    "$projeto/app/__init__.py" = ""
    "$projeto/app/config.py" = ""
    "$projeto/app/extensions.py" = ""
    "$projeto/app/models/__init__.py" = ""
    "$projeto/app/models/base.py" = ""
    "$projeto/app/models/user.py" = ""
    "$projeto/app/models/product.py" = ""
    "$projeto/app/api/__init__.py" = ""
    "$projeto/app/api/auth/__init__.py" = ""
    "$projeto/app/api/auth/routes.py" = ""
    "$projeto/app/api/users/__init__.py" = ""
    "$projeto/app/api/users/routes.py" = ""
    "$projeto/app/api/users/serializers.py" = ""
    "$projeto/app/api/products/__init__.py" = ""
    "$projeto/app/api/products/routes.py" = ""
    "$projeto/app/api/products/serializers.py" = ""
    "$projeto/app/services/__init__.py" = ""
    "$projeto/app/services/auth_service.py" = ""
    "$projeto/app/services/user_service.py" = ""
    "$projeto/app/services/external_api_service.py" = ""
    "$projeto/app/services/cache_service.py" = ""
    "$projeto/app/utils/__init__.py" = ""
    "$projeto/app/utils/decorators.py" = ""
    "$projeto/app/utils/validators.py" = ""
    "$projeto/app/utils/helpers.py" = ""
    "$projeto/app/utils/exceptions.py" = ""
    "$projeto/app/schemas/__init__.py" = ""
    "$projeto/app/schemas/user_schema.py" = ""
    "$projeto/app/schemas/product_schema.py" = ""
    "$projeto/tests/__init__.py" = ""
    "$projeto/tests/conftest.py" = ""
    "$projeto/tests/test_auth.py" = ""
    "$projeto/tests/test_users.py" = ""
    "$projeto/tests/test_products.py" = ""
    "$projeto/tests/fixtures/__init__.py" = ""
    "$projeto/tests/fixtures/sample_data.py" = ""
    "$projeto/docker/Dockerfile" = ""
    "$projeto/docker/docker-compose.yml" = ""
    "$projeto/docker/nginx.conf" = ""
    "$projeto/scripts/init_db.py" = ""
    "$projeto/scripts/seed_data.py" = ""
    "$projeto/requirements.txt" = @"
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
"@
    "$projeto/requirements-dev.txt" = @"
-r requirements.txt
pytest==7.4.3
pytest-flask==1.3.0
pytest-cov==4.1.0
pytest-mock==3.12.0
factory-boy==3.3.0
black==23.11.0
flake8==6.1.0
pre-commit==3.6.0
"@
    "$projeto/.env.example" = @"
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
"@
    "$projeto/.gitignore" = ""
    "$projeto/pytest.ini" = ""
    "$projeto/run.py" = ""
    "$projeto/README.md" = "# $projeto"
}

foreach ($file in $files.Keys) {
    if (-not (Test-Path $file)) {
        $content = $files[$file]
        New-Item -ItemType File -Path $file -Force | Out-Null
        if ($content -ne "") {
            Set-Content -Path $file -Value $content
        }
    }
}

Write-Host "Estrutura do projeto Flask '$projeto' criada com sucesso!"