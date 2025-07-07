# Biblioteca Python Profissional - Estrutura Completa

## 1. Estrutura de Diretórios

```
minha_biblioteca/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
├── docs/
│   ├── source/
│   │   ├── conf.py
│   │   ├── index.rst
│   │   ├── installation.rst
│   │   ├── quickstart.rst
│   │   └── api.rst
│   ├── Makefile
│   └── requirements.txt
├── src/
│   └── minha_biblioteca/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── data_processor.py
│       │   └── utils.py
│       ├── integrations/
│       │   ├── __init__.py
│       │   ├── django_integration.py
│       │   └── flask_integration.py
│       └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_core/
│   │   ├── __init__.py
│   │   ├── test_data_processor.py
│   │   └── test_utils.py
│   ├── test_integrations/
│   │   ├── __init__.py
│   │   ├── test_django_integration.py
│   │   └── test_flask_integration.py
│   └── fixtures/
│       └── sample_data.csv
├── examples/
│   ├── django_example/
│   │   ├── manage.py
│   │   └── example_app/
│   └── flask_example/
│       └── app.py
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── LICENSE
└── requirements-dev.txt
```

## 2. Comandos para Criar o Ambiente de Desenvolvimento

```bash
# 1. Criar diretório do projeto
mkdir minha_biblioteca
cd minha_biblioteca

# 2. Criar ambiente virtual (Python 3.13+)
python3.13 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Atualizar pip e instalar ferramentas básicas
pip install --upgrade pip
pip install build twine



# 4. Criar estrutura de diretórios
mkdir -p src/core
mkdir -p src/integrations
mkdir -p tests/test_integrations 
mkdir -p tests/test_core 
mkdir -p tests/fixtures
mkdir -p docs/source
mkdir -p examples/flask_example
mkdir -p examples/django_example
mkdir -p .github/workflows

# 5. Instalar salvar dependências de desenvolvimento
pip freeze > requirements.txt
# Depois, para instalar as mesmas dependências em outro ambiente:
pip install -r requirements-dev.txt

# 6. Instalar a biblioteca em modo de desenvolvimento
pip install -e .

# 7. Configurar pre-commit hooks
pre-commit install
```

## 3. Configuração pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "minha-biblioteca"
version = "0.1.0"
description = "Uma biblioteca Python para processamento de dados com pandas"
readme = "README.md"
license = {file = "LICENSE"}
authors = [
    {name = "Seu Nome", email = "seu.email@example.com"},
]
maintainers = [
    {name = "Seu Nome", email = "seu.email@example.com"},
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Framework :: Django",
    "Framework :: Flask",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Information Analysis",
]
keywords = ["pandas", "data-processing", "django", "flask"]
requires-python = ">=3.13"
dependencies = [
    "pandas>=2.1.0",
    "numpy>=1.24.0",
]

[project.optional-dependencies]
django = [
    "Django>=4.2",
]
flask = [
    "Flask>=2.3.0",
]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-mock>=3.11.0",
    "black>=23.7.0",
    "isort>=5.12.0",
    "flake8>=6.0.0",
    "mypy>=1.5.0",
    "pre-commit>=3.3.0",
    "sphinx>=7.1.0",
    "sphinx-rtd-theme>=1.3.0",
    "sphinx-autodoc-typehints>=1.24.0",
]
test = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-mock>=3.11.0",
]
docs = [
    "sphinx>=7.1.0",
    "sphinx-rtd-theme>=1.3.0",
    "sphinx-autodoc-typehints>=1.24.0",
]

[project.urls]
Homepage = "https://github.com/seuusuario/minha-biblioteca"
Documentation = "https://minha-biblioteca.readthedocs.io/"
Repository = "https://github.com/seuusuario/minha-biblioteca.git"
"Bug Tracker" = "https://github.com/seuusuario/minha-biblioteca/issues"
Changelog = "https://github.com/seuusuario/minha-biblioteca/blob/main/CHANGELOG.md"

[tool.hatch.build.targets.wheel]
packages = ["src/minha_biblioteca"]

[tool.hatch.build.targets.sdist]
include = [
    "/src",
    "/tests",
    "/docs",
    "/examples",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
]

# Configurações do Black
[tool.black]
line-length = 88
target-version = ['py313']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

# Configurações do isort
[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["minha_biblioteca"]

# Configurações do pytest
[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q --strict-markers --strict-config"
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]

[tool.coverage.run]
source = ["src/minha_biblioteca"]
omit = [
    "*/tests/*",
    "*/test_*",
    "setup.py",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]

# Configurações do mypy
[tool.mypy]
python_version = "3.13"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[[tool.mypy.overrides]]
module = ["pandas.*", "numpy.*"]
ignore_missing_imports = true
```

## 4. Arquivos __init__.py

### src/minha_biblioteca/__init__.py
```python
"""
Minha Biblioteca - Uma biblioteca Python para processamento de dados com pandas.

Esta biblioteca fornece ferramentas simplificadas para processamento de dados
usando pandas, com integrações específicas para Django e Flask.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("minha-biblioteca")
except PackageNotFoundError:
    # Pacote não instalado
    __version__ = "unknown"

# Imports principais
from .core.data_processor import DataProcessor
from .core.utils import validate_dataframe, clean_data
from .exceptions import (
    MinhaLibraryError,
    DataValidationError,
    ProcessingError,
)

# Imports condicionais para integrações
try:
    from .integrations.django_integration import DjangoDataProcessor
    HAS_DJANGO = True
except ImportError:
    HAS_DJANGO = False

try:
    from .integrations.flask_integration import FlaskDataProcessor
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False

# Definir __all__ para controlar imports com "from minha_biblioteca import *"
__all__ = [
    # Versão
    "__version__",
    # Core classes
    "DataProcessor",
    # Utilities
    "validate_dataframe",
    "clean_data",
    # Exceptions
    "MinhaLibraryError",
    "DataValidationError", 
    "ProcessingError",
    # Flags de disponibilidade
    "HAS_DJANGO",
    "HAS_FLASK",
]

# Adicionar integrações ao __all__ se disponíveis
if HAS_DJANGO:
    __all__.append("DjangoDataProcessor")

if HAS_FLASK:
    __all__.append("FlaskDataProcessor")

# Metadata
__author__ = "Seu Nome"
__email__ = "seu.email@example.com"
__license__ = "MIT"
__description__ = "Uma biblioteca Python para processamento de dados com pandas"
```

### src/minha_biblioteca/core/__init__.py
```python
"""Módulo core com funcionalidades principais da biblioteca."""

from .data_processor import DataProcessor
from .utils import validate_dataframe, clean_data

__all__ = [
    "DataProcessor",
    "validate_dataframe", 
    "clean_data",
]
```

### src/minha_biblioteca/integrations/__init__.py
```python
"""Integrações com frameworks web."""

# Imports condicionais
try:
    from .django_integration import DjangoDataProcessor
    HAS_DJANGO = True
except ImportError:
    HAS_DJANGO = False

try:
    from .flask_integration import FlaskDataProcessor
    HAS_FLASK = True
except ImportError:
    HAS_FLASK = False

__all__ = []

if HAS_DJANGO:
    __all__.append("DjangoDataProcessor")

if HAS_FLASK:
    __all__.append("FlaskDataProcessor")
```

## 5. Estrutura de Testes com pytest

### tests/conftest.py
```python
"""Configurações e fixtures compartilhadas para todos os testes."""

import pytest
import pandas as pd
from pathlib import Path

# Diretório de fixtures
FIXTURES_DIR = Path(__file__).parent / "fixtures"

@pytest.fixture
def sample_dataframe():
    """Fixture que fornece um DataFrame de exemplo para testes."""
    return pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [25, 30, 35, 28, 32],
        'salary': [50000, 60000, 70000, 55000, 65000]
    })

@pytest.fixture
def empty_dataframe():
    """Fixture que fornece um DataFrame vazio."""
    return pd.DataFrame()

@pytest.fixture
def sample_csv_path():
    """Fixture que fornece o caminho para um arquivo CSV de exemplo."""
    return FIXTURES_DIR / "sample_data.csv"

@pytest.fixture(scope="session")
def create_sample_csv():
    """Fixture de sessão que cria um arquivo CSV de exemplo."""
    FIXTURES_DIR.mkdir(exist_ok=True)
    csv_path = FIXTURES_DIR / "sample_data.csv"
    
    if not csv_path.exists():
        df = pd.DataFrame({
            'id': range(1, 101),
            'value': range(100, 200),
            'category': ['A', 'B', 'C'] * 33 + ['A']
        })
        df.to_csv(csv_path, index=False)
    
    yield csv_path
    
    # Cleanup após os testes (opcional)
    # csv_path.unlink(missing_ok=True)

class MockResponse:
    """Classe mock para simular respostas HTTP em testes."""
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

@pytest.fixture
def mock_api_response():
    """Fixture para simular resposta de API."""
    return MockResponse(
        json_data={'data': [{'id': 1, 'value': 'test'}]},
        status_code=200
    )
```

### tests/test_core/test_data_processor.py
```python
"""Testes para o módulo DataProcessor."""

import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

from minha_biblioteca.core.data_processor import DataProcessor
from minha_biblioteca.exceptions import DataValidationError, ProcessingError


class TestDataProcessor:
    """Testes para a classe DataProcessor."""

    def test_init_with_dataframe(self, sample_dataframe):
        """Testa inicialização com DataFrame."""
        processor = DataProcessor(sample_dataframe)
        assert processor.data is not None
        assert len(processor.data) == 5

    def test_init_with_empty_dataframe_raises_error(self, empty_dataframe):
        """Testa que DataFrame vazio levanta exceção."""
        with pytest.raises(DataValidationError):
            DataProcessor(empty_dataframe)

    def test_process_data_success(self, sample_dataframe):
        """Testa processamento bem-sucedido de dados."""
        processor = DataProcessor(sample_dataframe)
        result = processor.process()
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    @pytest.mark.parametrize("column,expected", [
        ("age", 30.0),
        ("salary", 60000.0),
    ])
    def test_calculate_mean(self, sample_dataframe, column, expected):
        """Testa cálculo de média para diferentes colunas."""
        processor = DataProcessor(sample_dataframe)
        mean_value = processor.calculate_mean(column)
        assert mean_value == expected

    def test_calculate_mean_invalid_column(self, sample_dataframe):
        """Testa cálculo de média com coluna inválida."""
        processor = DataProcessor(sample_dataframe)
        with pytest.raises(ProcessingError):
            processor.calculate_mean("invalid_column")

    @patch('minha_biblioteca.core.data_processor.pd.read_csv')
    def test_load_from_csv(self, mock_read_csv, sample_dataframe):
        """Testa carregamento de dados de CSV."""
        mock_read_csv.return_value = sample_dataframe
        
        processor = DataProcessor.from_csv("dummy_path.csv")
        
        assert processor.data is not None
        mock_read_csv.assert_called_once_with("dummy_path.csv")

    def test_filter_data(self, sample_dataframe):
        """Testa filtragem de dados."""
        processor = DataProcessor(sample_dataframe)
        filtered = processor.filter_data(age__gt=30)
        
        assert len(filtered) == 2  # Charlie (35) e Eve (32)
        assert all(filtered['age'] > 30)

    @pytest.mark.slow
    def test_complex_processing(self, sample_dataframe):
        """Teste mais complexo que demora mais tempo."""
        processor = DataProcessor(sample_dataframe)
        # Simular processamento pesado
        result = processor.complex_operation()
        assert result is not None

    @pytest.mark.integration
    def test_integration_with_pandas_operations(self, sample_dataframe):
        """Teste de integração com operações do pandas."""
        processor = DataProcessor(sample_dataframe)
        
        # Cadeia de operações
        result = (processor.data
                 .groupby('age')
                 .agg({'salary': 'mean'})
                 .reset_index())
        
        assert isinstance(result, pd.DataFrame)
        assert 'age' in result.columns
```

## 6. Configuração de Documentação (Sphinx)

### docs/source/conf.py
```python
"""Configuração do Sphinx para documentação."""

import os
import sys
from pathlib import Path

# Adicionar o diretório src ao path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "src"))

# -- Informações do projeto --
project = 'Minha Biblioteca'
copyright = '2024, Seu Nome'
author = 'Seu Nome'
release = '0.1.0'

# -- Configurações gerais --
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'pt_BR'

# -- Opções para saída HTML --
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Configurações de autodoc --
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# -- Configurações de Napoleon (para docstrings Google/NumPy) --
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# -- Intersphinx mapping --
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}

# -- Autosummary --
autosummary_generate = True
```

### docs/source/index.rst
```rst
Bem-vindo à documentação da Minha Biblioteca!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Conteúdo:

   installation
   quickstart
   api

Índices e tabelas
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

## 7. Arquivos de Configuração Adicionais

### .gitignore
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

### requirements-dev.txt
```txt
# Dependências de desenvolvimento

# Testes
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-mock>=3.11.0
pytest-xdist>=3.3.0  # Para execução paralela de testes

# Code quality
black>=23.7.0
isort>=5.12.0
flake8>=6.0.0
mypy>=1.5.0
pre-commit>=3.3.0

# Documentação
sphinx>=7.1.0
sphinx-rtd-theme>=1.3.0
sphinx-autodoc-typehints>=1.24.0

# Build e deploy
build>=0.10.0
twine>=4.0.2

# Integrações opcionais para desenvolvimento
Django>=4.2
Flask>=2.3.0

# Utilitários
ipython>=8.14.0
jupyter>=1.0.0
```

### .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict

  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3.13

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.0
    hooks:
      - id: mypy
        additional_dependencies: [pandas-stubs, types-requests]
```

## 8. GitHub Actions (CI/CD)

### .github/workflows/ci.yml
```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.13", "3.14"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev,test]

    - name: Lint with flake8
      run: |
        flake8 src tests --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 src tests --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

    - name: Check code formatting with black
      run: black --check src tests

    - name: Check import sorting with isort
      run: isort --check-only src tests

    - name: Type check with mypy
      run: mypy src

    - name: Test with pytest
      run: |
        pytest tests/ --cov=src/minha_biblioteca --cov-report=xml --cov-report=html

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
```

## 9. Comandos Úteis para Desenvolvimento

```bash
# Executar testes
pytest                              # Todos os testes
pytest -v                          # Verbose
pytest --cov=src/minha_biblioteca  # Com coverage
pytest -m "not slow"               # Excluir testes lentos
pytest -x                          # Parar no primeiro erro

# Formatação de código
black src tests                     # Formatar código
isort src tests                     # Organizar imports
flake8 src tests                    # Linting

# Type checking
mypy src                           # Verificação de tipos

# Documentação
cd docs
make html                          # Gerar documentação HTML
make clean                         # Limpar build anterior

# Build e deploy
python -m build                    # Criar distribuições
twine check dist/*                 # Verificar distribuições
twine upload dist/*                # Upload para PyPI (produção)
twine upload --repository testpypi dist/*  # Upload para TestPyPI

# Desenvolvimento
pip install -e .                   # Instalar em modo de desenvolvimento
pip install -e .[dev]              # Com dependências de desenvolvimento
```

## Propósito de Cada Diretório

- **src/**: Código fonte da biblioteca (layout src para evitar problemas de import)
- **tests/**: Todos os testes automatizados organizados por módulo
- **docs/**: Documentação usando Sphinx
- **examples/**: Exemplos de uso da biblioteca
- **.github/workflows/**: Automação CI/CD com GitHub Actions
- **fixtures/**: Dados de exemplo para testes

Esta estrutura garante uma biblioteca Python profissional, testável, documentada e pronta para distribuição no PyPI.