
## Padrões de Desenvolvimento Python

### Versão e Ambiente
- **Python**: 3.13+ obrigatório
- **Ambiente virtual**: Sempre usar `venv` (não conda, poetry, etc.)
- **Gerenciador de pacotes**: pip com pyproject.toml

### Estrutura de Código
- **Layout**: Usar estrutura `src/` layout para evitar problemas de import
- **Organização**: Separar core, integrações e utilitários em módulos distintos
- **Imports**: Sempre usar imports absolutos a partir do pacote raiz

### Boas Práticas de Codificação

#### Type Hints
- Sempre usar type hints em todas as funções e métodos
- Usar `typing` e `typing_extensions` quando necessário
- Para pandas: `pd.DataFrame`, `pd.Series`, etc.

#### Docstrings
- Formato Google style docstrings
- Incluir Args, Returns, Raises e Examples
- Documentar todos os métodos públicos

#### Error Handling
- Criar exceções customizadas específicas (herdar de classe base personalizada)
- Sempre validar inputs de DataFrames
- Usar logging apropriado para debugging

#### Testes
- pytest como framework principal
- Fixtures compartilhadas em conftest.py
- Coverage mínimo de 90%
- Separar testes unitários, de integração e lentos com markers

### Convenções de Naming

#### Arquivos e Módulos
- snake_case para todos os arquivos Python
- Módulos core: `data_processor.py`, `utils.py`
- Integrações: `django_integration.py`, `flask_integration.py`

#### Classes e Funções
- PascalCase para classes: `DataProcessor`, `DjangoDataProcessor`
- snake_case para funções e métodos: `process_data()`, `validate_dataframe()`
- Private methods com underscore: `_validate_data()`

#### Constantes
- UPPER_SNAKE_CASE: `MAX_ROWS`, `DEFAULT_ENCODING`
