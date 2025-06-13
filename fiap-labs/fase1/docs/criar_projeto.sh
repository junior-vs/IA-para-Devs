#!/bin/bash

if [ -z "$1" ]; then
  echo "Uso: $0 <nome_do_projeto>"
  exit 1
fi

PROJETO="$1"

mkdir "$PROJETO"
cd "$PROJETO"


# 2. Criar ambiente virtual (Python 3.13+)
python3.13 -m venv venv

venv\Scripts\activate  # Windows
# ou
#source venv/bin/activate  # Linux/Mac

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