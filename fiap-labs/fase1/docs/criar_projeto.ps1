```powershell
param (
    [Parameter(Mandatory = $true)]
    [string]$projeto
)

if (-not $projeto) {
    Write-Host "Uso: .\criar_projeto.ps1 <nome_do_projeto>"
    exit 1
}

# 1. Criar diretório do projeto
if (-not (Test-Path $projeto)) {
    New-Item -ItemType Directory -Name $projeto | Out-Null
}
Set-Location $projeto

# 2. Criar ambiente virtual (Python 3.13+)
python3.13 -m venv venv

# 3. Ativar ambiente virtual (PowerShell)
& .\venv\Scripts\Activate.ps1

# 4. Atualizar pip e instalar ferramentas básicas
pip install --upgrade pip
pip install build twine pre-commit

# 5. Criar estrutura de diretórios
$dirs = @(
    "src/core",
    "src/integrations",
    "tests/test_integrations",
    "tests/test_core",
    "tests/fixtures",
    "docs/source",
    "examples/flask_example",
    "examples/django_example",
    ".github/workflows"
)
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}

# 6. Gerar requirements-dev.txt
pip freeze > requirements-dev.txt

# 7. Instalar biblioteca em modo desenvolvimento (se existir setup.py/pyproject.toml)
if (Test-Path "setup.py" -or Test-Path "pyproject.toml") {
    pip install -e .
}

# 8. Configurar pre-commit hooks
pre-commit install

Write-Host "Projeto '$projeto' criado com sucesso!"
```

