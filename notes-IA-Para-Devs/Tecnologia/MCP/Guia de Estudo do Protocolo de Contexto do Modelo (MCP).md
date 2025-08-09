# Guia de Estudo do Protocolo de Contexto do Modelo (MCP)

Este guia de estudo foi concebido para testar a sua compreensão do Model Context Protocol (MCP), dos seus componentes, funcionalidades e melhores práticas.

## I. [[Conceitos básicos do MCP]]

- **O que é o MCP?**
	- Um protocolo padrão aberto para aplicações de IA e agentes interagirem com fontes de dados e ferramentas externas.
	- Um "adaptador universal" para aplicações de IA, similar ao USB-C para dispositivos físicos.
- **Por que o MCP é importante?**
	- **Para usuários de aplicações de IA:** Permite que aplicações de IA acessem informações e ferramentas diárias (ex: Google Drive, GitHub), tornando-as mais úteis e contextualmente relevantes.
	- **Para desenvolvedores:** Reduz o tempo de desenvolvimento e a complexidade, permitindo a reutilização de servidores MCP para várias aplicações, promovendo um ecossistema de código aberto.
- **Como o MCP funciona?**
	- **Servidores MCP:** Conectam-se a fontes de dados e ferramentas (ex: Google Drive, Slack).
	- **Clientes MCP:** Executados por aplicações de IA (ex: Claude Desktop) para conectar-se a servidores.
	- **Fluxo:** O aplicativo de IA descobre servidores disponíveis (com permissão), e o modelo de IA usa essas conexões para ler informações e agir.
	- Sistema modular que permite adicionar novas capacidades sem alterar as aplicações de IA.

## II. [[Arquitetura do MCP]]

- **Participantes:** 
	- **Host MCP (Aplicação de IA):** Coordena e gerencia um ou vários clientes MCP (ex: Visual Studio Code, Claude Desktop).
	- **Cliente MCP:** Mantém uma conexão um-para-um com um servidor MCP e obtém contexto para o host MCP.
	- **Servidor MCP:** Um programa que fornece contexto aos clientes MCP, podendo ser executado localmente ou remotamente.
- **Camadas do MCP:**
	- **Camada de Dados:** Implementa um protocolo de troca baseado em JSON-RPC 2.0.
	- Inclui gerenciamento de ciclo de vida (inicialização, negociação de capacidade, término).
	- Define as primitivas do servidor (Ferramentas, Recursos, Prompts) e do cliente (Amostragem, Elicitação, Registro).
	- Suporta notificações para atualizações em tempo real (ex: tools/list_changed).
- **Camada de Transporte:**
	- Gerencia canais de comunicação e autenticação.
	- **Transporte Stdio:** Usa fluxos de entrada/saída padrão para comunicação direta de processo (servidores locais).
	- **Transporte HTTP Transmitível:** Usa HTTP POST e Server-Sent Events (SSE) para comunicação de servidor remoto, suportando métodos de autenticação HTTP padrão (tokens de portador, chaves de API, OAuth).

## III. Primitivas do Servidor MCP

- **Ferramentas (AI Actions):**Funções implementadas pelo servidor que LLMs podem invocar para realizar ações (ex: procurar voos, enviar e-mails).
- Definem operações com entradas e saídas tipadas, usando JSON Schema para validação.
- Exigem aprovação explícita do usuário para execução.
- **Operações do Protocolo:** tools/list (descobrir ferramentas), tools/call (executar ferramenta).
- **Recursos (Context Data):**Exponham dados de arquivos, APIs, bancos de dados ou outras fontes que a IA precisa para entender o contexto.
- Identificação baseada em URI (ex: file:///path/to/document.md).
- Declarar tipos MIME para manuseio apropriado do conteúdo.
- Suportam **recursos diretos** (URIs fixas) e **modelos de recursos** (URIs parametrizadas).
- **Operações do Protocolo:** resources/list, resources/templates/list, resources/read, resources/subscribe (monitorar alterações).
- **Prompts (Interaction Templates):**Modelos estruturados que definem entradas esperadas e padrões de interação.
- Controlados pelo usuário, exigindo invocação explícita.
- Podem ser sensíveis ao contexto, referenciando recursos e ferramentas.
- Suportam preenchimento de parâmetros.
- **Operações do Protocolo:** prompts/list, prompts/get.

## IV. Primitivas do Cliente MCP

- **Amostragem (Sampling):**Permite que os servidores solicitem conclusões do modelo de linguagem através do cliente, mantendo a segurança e o controle do usuário.
- **Fluxo:** O servidor inicia o sampling/createMessage, o cliente apresenta a solicitação para aprovação do usuário, o cliente encaminha a solicitação aprovada para o LLM, o LLM retorna a geração, o cliente apresenta a resposta para aprovação do usuário, e o cliente retorna a resposta aprovada para o servidor.
- Destinado ao controle humano-em-loop (HUMAN-IN-THE-LOOP): controles de aprovação, recursos de transparência, opções de configuração (aprovação automática/manual), isolamento do contexto da conversa principal.
- **Elicitação (Elicitation):**Permite que os servidores solicitem informações específicas dos usuários durante as interações.
- **Fluxo:** O servidor inicia o elicitation/create, o cliente apresenta a interface do usuário de elicitação, o usuário fornece as informações solicitadas, e o cliente retorna a resposta do usuário para o servidor.
- Apresentação clara da solicitação, opções de resposta (fornecer, recusar, cancelar), considerações de privacidade (nunca solicitar senhas/chaves API).
- **Registro (Logging):**Permite que os servidores enviem mensagens de log aos clientes para depuração e monitoramento.

## V. Fluxo de Trabalho do Cliente MCP (Exemplos de Python/TypeScript/C#/Kotlin)

- **Requisitos do Sistema:** Mac/Windows, Python/Node.js/Java/.NET mais recente, uv/npm/gradle/dotnet instalados, chave API Anthropic.
- **Configuração do Ambiente:** Criar diretório do projeto, configurar ambiente virtual/npm/gradle, instalar pacotes necessários (mcp, anthropic, python-dotenv/@anthropic-ai/sdk, etc.).
- **Configuração da Chave API:** Criar arquivo .env para armazenar a chave API (ex: ANTHROPIC_API_KEY). Manter a chave segura.
- **Estrutura Básica do Cliente:** Inicializar sessão, objetos do cliente e cliente Anthropic. Usar AsyncExitStack (Python) ou mecanismos de fechamento (Kotlin/TypeScript) para gerenciamento de recursos.
- **Gerenciamento de Conexão com o Servidor:**Conectar-se a um servidor MCP (Python, Node.js, .NET, Java).
- Validar o tipo de script do servidor (.py, .js, .csproj, .jar).
- Estabelecer canais de comunicação (stdio).
- Inicializar a sessão e listar as ferramentas disponíveis.
- **Lógica de Processamento de Consultas:**Manter o contexto da conversa.
- Lidar com respostas do Claude e chamadas de ferramentas.
- Gerenciar o fluxo de mensagens entre o Claude e as ferramentas.
- Combinar resultados em uma resposta coerente.
- **Fluxo:** Cliente lista ferramentas -> consulta enviada ao Claude com descrições de ferramentas -> Claude decide o uso de ferramentas -> cliente executa chamadas de ferramentas via servidor -> resultados enviados de volta ao Claude -> Claude fornece resposta em linguagem natural -> resposta exibida ao usuário.
- **Interface de Chat Interativa:** Loop de chat para entrada do usuário, processamento de consulta e exibição de resposta. Inclui tratamento básico de erros e saída graciosa.
- **Ponto de Entrada Principal:** Lógica de execução para conectar ao servidor, iniciar o loop de chat e limpar recursos.
- **Componentes Chave Explicados:** Inicialização do cliente, conexão do servidor, processamento de consultas, interface interativa, gerenciamento de recursos.
- **Pontos de Personalização Comuns:** Tratamento de ferramentas, processamento de respostas, interface do usuário.
- **Executando o Cliente:** Exemplos de linha de comando para diferentes linguagens.
- **Melhores Práticas:** Tratamento de erros (try-catch), gerenciamento de recursos (AsyncExitStack/close), segurança (API keys em .env).
- **Solução de Problemas:** Problemas de caminho do servidor, tempo de resposta (primeira resposta pode levar até 30s), mensagens de erro comuns.

## VI. Fluxo de Trabalho do Servidor MCP (Exemplos de Python/TypeScript/Java/C#/Kotlin)

- **O que construir:** Um servidor de clima simples que expõe ferramentas como get_alerts e get_forecast e se conecta a um host (ex: Claude for Desktop).
- **Conceitos Essenciais do MCP (Servidor):** Recursos, Ferramentas, Prompts. Este tutorial foca em ferramentas.
- **Conhecimento Prévio:** Familiaridade com a linguagem de programação escolhida e LLMs como Claude.
- **Registro em Servidores MCP:Servidores baseados em STDIO:** NUNCA escreva para a saída padrão (stdout) para evitar corrupção de mensagens JSON-RPC. Use stderr ou arquivos para log.
- **Servidores baseados em HTTP:** O log da saída padrão é aceitável.
- **Requisitos do Sistema e Configuração do Ambiente:** Ferramentas de gerenciamento de pacotes (uv, npm, Maven/Gradle, dotnet), dependências do SDK MCP e bibliotecas HTTP.
- **Construindo o Servidor:Importando Pacotes e Configurando a Instância:** Inicializar a classe FastMCP (Python), McpServer (TypeScript), Spring AI MCP Server (Java), AddMcpServer (C#), Server (Kotlin).
- **Funções Auxiliares:** Funções para consultar APIs externas (ex: NWS API) e formatar dados.
- **Implementando a Execução da Ferramenta:**Decoradores (@mcp.tool() em Python, @Tool em Java) ou métodos de registro (server.tool() em TypeScript, server.addTool em Kotlin, atributos C#).
- Definir nome da ferramenta, descrição e esquema de entrada (parâmetros tipados).
- Lógica para fazer chamadas HTTP, processar dados e retornar resultados formatados.
- **Executando o Servidor:** Comando para iniciar o servidor (ex: uv run weather.py, npm run build && node build/index.js, ./mvnw clean install && java -jar ...jar, dotnet run, ./gradlew build && java -jar ...jar).
- **Testando o Servidor com Claude for Desktop:**Instalar e atualizar o Claude for Desktop.
- Configurar claude_desktop_config.json para adicionar o servidor MCP, especificando o comando e os argumentos (caminho absoluto, / ou \\ para Windows).
- Reiniciar o Claude for Desktop.
- Verificar o indicador do servidor MCP e as ferramentas disponíveis.
- Testar com consultas de linguagem natural.
- **Como Funciona (Servidor):** Consulta enviada ao Claude -> Claude analisa ferramentas disponíveis -> cliente executa ferramentas via servidor -> resultados enviados de volta ao Claude -> Claude formula resposta.
- **Solução de Problemas do Servidor:**Logs do Claude for Desktop (mcp.log, mcp-server-SERVERNAME.log).
- Sintaxe do arquivo de configuração, caminhos absolutos, reinício do Claude.
- Falha nas chamadas de ferramentas, erros de tempo de execução do servidor.
- Error: Failed to retrieve grid point data (coordenadas fora dos EUA, problemas da API NWS).
- No active alerts for [STATE] (não é um erro).

## VII. Segurança do MCP

- **Desafios de Segurança:** Injeção de prompt, envenenamento de ferramentas, modificação dinâmica de ferramentas, exfiltração de dados, violações de privacidade, ações não intencionais.
- **Autenticação e Gerenciamento de Token:**Delegar a provedores de identidade externos (ex: Microsoft Entra ID) é preferível.
- **Token pass-through:** Explicitamente PROIBIDO na especificação MCP, pois ignora controles de segurança e confunde a trilha de auditoria.
- Aceitar apenas tokens emitidos especificamente para o servidor MCP.
- **Permissões (Princípio do Menor Privilégio):**Servidores MCP devem ter acesso mínimo necessário aos dados.
- Usar RBAC (Role-Based Access Control) e auditoria de funções.
- **Injeção Indireta de Prompt:**Instruções maliciosas escondidas em contexto externo (e-mail, web, PDF).
- **Escudos de Prompt (Prompt Shields - Microsoft):** Detecção e filtragem, destaque (spotlighting), delimitadores e marcação de dados, atualizações contínuas, integração com Azure Content Safety.
- **Envenenamento de Ferramentas (Tool Poisoning):**Metadados de ferramentas MCP adulterados (descrições, parâmetros) para induzir comportamento perigoso.
- Risco de "rugpull" em ambientes hospedados (ferramentas alteradas após aprovação do usuário).
- **Segurança da Cadeia de Suprimentos:**Verificar a fonte de componentes (modelos, embeddings, APIs, provedores de contexto).
- Pipelines de implantação seguros, varredura de vulnerabilidades, monitoramento contínuo.
- **Postura de Segurança do Ambiente:** MCP herda a postura de segurança do ambiente.
- Práticas de codificação seguras (OWASP Top 10, OWASP para LLMs).
- Endurecer servidores, MFA, patching regular.
- Habilitar log e monitoramento.
- Projetar com arquitetura zero trust.

## VIII. Desenvolvimento, Teste e Implantação

- **Fluxo de Desenvolvimento:** Iniciar o Inspector, testar conectividade, negociação de capacidade, teste iterativo, casos de uso extremos.
- **Melhores Práticas de Desenvolvimento:Arquitetura:** Responsabilidade única, injeção de dependência, composabilidade.
- **Esquema:** Descrições claras, validação, estruturas de retorno consistentes.
- **Tratamento de Erros:** Captura em nível apropriado, mensagens estruturadas, lógica de repetição.
- **Desempenho:** Cache, padrões assíncronos, limitação de uso.
- **Segurança:** Validar entradas, autorização, redação de dados sensíveis.
- **Teste:** Testes de unidade, testes de validação de esquema, testes de integração, testes ponta a ponta, testes de desempenho.
- **Padrões de Ferramentas:** Cadeia de ferramentas, roteador, processamento paralelo, recuperação de erros, composição.
- **Implantação:** Azure Functions, Azure API Management (rate limiting, auth, monitoring, load balancing, security).

## IX. Aplicações do Mundo Real e Estudos de Caso

- **Casos de Uso:** Suporte ao cliente, integração de saúde, padronização de modelos de risco financeiro, automação de navegador (Playwright), documentação em tempo real, planejamento de estudo web, integração do editor VS Code, walkthrough do servidor APIM MCP.
- **Tendências Futuras:** Suporte multimodal (imagens, áudio, vídeo), infraestrutura federada, suporte a edge computing, marketplaces de modelos e ferramentas.
- **Projetos de Código Aberto:** Servidor Playwright MCP, Azure MCP, Playground Foundry MCP, NL web.

## X. Ferramentas de Desenvolvimento MCP

- **MCP Inspector:** Ferramenta interativa para testar e depurar servidores MCP.
- **Instalação/Uso:** npx @modelcontextprotocol/inspector (para NPM/PyPi/servidores locais).
- **Recursos:** Painel de conexão do servidor, guias de recursos/prompts/ferramentas, painel de notificações (logs, notificações).
- **SDKs MCP:** Disponíveis em Python, JavaScript/TypeScript, Java, C#.
- **AI Toolkit para Visual Studio Code:**Extensão que fornece um ambiente completo de desenvolvimento de IA no VS Code.
- Catálogo de modelos, playground (testar prompts, ajustar parâmetros), construtor de agentes (definir função, personalidade, ferramentas).
- Permite construir e testar servidores MCP personalizados, integrar com GitHub Copilot.

## Quiz: Protocolo de Contexto do Modelo (MCP)

Responda a cada pergunta em 2-3 frases.

1. O que é o Model Context Protocol (MCP) e qual é o seu principal objetivo?
2. Descreva a distinção entre um "host MCP" e um "cliente MCP" na arquitetura do protocolo.
3. Quais são os três principais tipos de capacidades que os servidores MCP podem fornecer? Dê um breve exemplo de cada.
4. Explique por que é crucial que os servidores MCP baseados em STDIO não escrevam para a saída padrão (stdout).
5. O que é a "amostragem" (sampling) no contexto das primitivas do cliente MCP e qual é a sua finalidade principal?
6. Como as "raízes" (roots) contribuem para a segurança e o escopo das operações do servidor no sistema de arquivos?
7. Por que o "token pass-through" é explicitamente proibido na especificação MCP para autenticação?
8. Quais são os dois principais mecanismos de transporte suportados pelo MCP e quando cada um é normalmente usado?
9. Descreva brevemente o processo de "negociação de versão" no MCP.
10. O que é o "MCP Inspector" e qual é a sua função principal no ciclo de desenvolvimento do MCP?

## Chave de Respostas do Quiz

1. O Model Context Protocol (MCP) é um padrão aberto que permite que aplicações e agentes de IA se conectem e trabalhem com fontes de dados e ferramentas externas. Seu principal objetivo é fornecer uma maneira padronizada e escalável para os modelos de IA interagirem com o mundo exterior, agindo como um "adaptador universal".
2. Um "host MCP" é o aplicativo de IA que o usuário interage, gerenciando a experiência geral do usuário e coordenando múltiplos clientes. Por outro lado, um "cliente MCP" é um componente de nível de protocolo instanciado pelo host, que mantém uma conexão direta e um-para-um com um servidor MCP específico para obter contexto.
3. Os servidores MCP podem fornecer **Recursos**, que são dados semelhantes a arquivos que os clientes podem ler (ex: conteúdo de documentos). Eles também fornecem **Ferramentas**, que são funções executáveis que o LLM pode chamar para ações (ex: obter a previsão do tempo). Por fim, eles oferecem **Prompts**, que são modelos pré-escritos para ajudar os usuários a realizar tarefas específicas (ex: "Planejar férias").
4. É crucial que os servidores MCP baseados em STDIO não escrevam para a saída padrão (stdout) porque isso corromperia as mensagens JSON-RPC. O stdout é usado para a comunicação do protocolo em si, e qualquer saída não relacionada interferiria e quebraria a capacidade do servidor de se comunicar corretamente com o cliente.
5. A "amostragem" (sampling) é uma primitiva do cliente que permite aos servidores solicitar conclusões de modelo de linguagem através do cliente, em vez de integrar diretamente um modelo de IA. Sua finalidade principal é permitir que os servidores realizem tarefas dependentes de IA enquanto o cliente mantém controle total sobre as permissões do usuário e as medidas de segurança, com revisão humana-em-loop.
6. As "raízes" (roots) definem limites do sistema de arquivos para as operações do servidor, especificando quais diretórios o servidor pode acessar. Isso contribui para a segurança ao orientar os servidores para diretórios de trabalho relevantes, impedindo o acesso irrestrito ao sistema de arquivos e garantindo que as operações do servidor permaneçam dentro dos limites de permissão pretendidos.
7. O "token pass-through" é explicitamente proibido na especificação MCP porque ele permite que os clientes ignorem controles de segurança críticos. Isso confunde a trilha de auditoria e quebra os limites de confiança entre os serviços, tornando a gestão de segurança e a responsabilização muito mais complexas.
8. Os dois principais mecanismos de transporte suportados pelo MCP são o **Stdio transport** e o **Streamable HTTP transport**. O transporte Stdio é normalmente usado para comunicação direta entre processos locais na mesma máquina (servidores locais), enquanto o transporte HTTP Transmitível é usado para comunicação de servidor remoto, suportando métodos de autenticação HTTP padrão.
9. A negociação de versão no MCP ocorre durante a fase de inicialização da conexão. Clientes e servidores podem suportar várias versões do protocolo, mas devem concordar em uma única versão para usar durante a sessão. O protocolo fornece tratamento de erros se a negociação falhar, permitindo que as conexões sejam encerradas.
10. O "MCP Inspector" é uma ferramenta interativa de desenvolvedor projetada para testar e depurar servidores MCP. Sua função principal é fornecer uma interface para inspecionar o comportamento do servidor ao vivo, listar recursos, prompts e ferramentas disponíveis, e permitir o teste de ferramentas com entradas personalizadas, além de exibir logs e notificações.

## Perguntas em Formato de Redação

1. Compare e contraste as primitivas de "Ferramentas", "Recursos" e "Prompts" do servidor MCP. Discuta seus propósitos, como são controlados e forneça exemplos de como um aplicativo de IA os utilizaria em um cenário de planejamento de viagens.
2. Explique o fluxo detalhado de "amostragem" (sampling) como uma primitiva do cliente MCP, incluindo os participantes e os pontos de controle humano-em-loop. Por que esse design é fundamental para a segurança e o controle do usuário?
3. Discuta as principais considerações de segurança ao construir servidores MCP, com foco em autenticação, gerenciamento de permissões e mitigação de ataques como injeção de prompt e envenenamento de ferramentas. Como as "melhores práticas" abordam esses riscos?
4. Descreva o ciclo de vida de uma interação cliente-servidor MCP, desde a inicialização até a execução da ferramenta e as notificações. Use exemplos de mensagens JSON-RPC para ilustrar a negociação de capacidade e a invocação da ferramenta.
5. Explique como a arquitetura do MCP, incluindo seus participantes e camadas, permite a escalabilidade, a interoperabilidade e a facilidade de manutenção para aplicações de IA. Dê exemplos de como a modularidade do MCP se manifesta na prática.

## Glossário de Termos Chave

- **Model Context Protocol (MCP):** Um padrão aberto e uma interface para aplicações de IA e agentes conectarem-se e interagirem com fontes de dados e ferramentas externas, funcionando como um adaptador universal.
- **Host MCP:** O aplicativo de IA (ex: Claude Desktop, Visual Studio Code) que coordena e gerencia um ou vários clientes MCP, fornecendo a interface do usuário.
- **Cliente MCP:** Um componente dentro do host MCP que estabelece e mantém uma conexão um-para-um com um servidor MCP, obtendo contexto e facilitando a comunicação para o host.
- **Servidor MCP:** Um programa que expõe capacidades específicas (ferramentas, recursos, prompts) a clientes MCP através de interfaces de protocolo padronizadas, podendo ser executado localmente ou remotamente.
- **Ferramentas (Tools):** Funções implementadas por um servidor MCP que LLMs podem invocar para realizar ações no mundo real. Elas têm esquemas de entrada/saída definidos e geralmente exigem aprovação do usuário.
- **Recursos (Resources):** Dados estruturados (ex: arquivos, entradas de banco de dados, respostas de API) expostos por um servidor MCP, fornecendo contexto e informações para o aplicativo de IA. Podem ser diretos ou baseados em modelos.
- **Prompts:** Modelos estruturados e reutilizáveis fornecidos por um servidor MCP que definem entradas esperadas e padrões de interação, guiando o comportamento da IA.
- **Amostragem (Sampling):** Uma capacidade do cliente MCP que permite que os servidores solicitem conclusões do modelo de linguagem através do cliente, mantendo o controle e a segurança do usuário.
- **Elicitação (Elicitation):** Uma capacidade do cliente MCP que permite que os servidores solicitem informações específicas adicionais dos usuários durante as interações, através de uma interface de usuário.
- **Registro (Logging - Cliente):** Uma capacidade do cliente MCP que permite que os servidores enviem mensagens de log para os clientes para fins de depuração e monitoramento.
- **Raízes (Roots):** Um mecanismo pelo qual os clientes MCP comunicam limites do sistema de arquivos aos servidores, indicando quais diretórios os servidores devem focar suas operações, aumentando a segurança.
- **JSON-RPC 2.0:** O protocolo RPC subjacente usado pela camada de dados do MCP para comunicação cliente-servidor, definindo estruturas e semânticas de mensagem.
- **Stdio Transport:** Um mecanismo de transporte do MCP que usa fluxos de entrada/saída padrão para comunicação direta de processo entre processos locais na mesma máquina.
- **Streamable HTTP Transport:** Um mecanismo de transporte do MCP que usa HTTP POST e Server-Sent Events (SSE) para comunicação de servidor remoto, suportando métodos de autenticação HTTP padrão.
- **Negociação de Versão:** Um processo durante a inicialização da conexão MCP onde cliente e servidor concordam em uma única versão compatível do protocolo a ser usada para a sessão.
- **Injeção de Prompt Indireta:** Um ataque de segurança onde instruções maliciosas são escondidas em contexto externo (ex: e-mail, página da web) que o AI lê, levando a ações não intencionais.
- **Envenenamento de Ferramentas (Tool Poisoning):** Um ataque onde os metadados de uma ferramenta MCP (descrições, parâmetros) são adulterados para induzir o LLM a realizar comportamentos perigosos.
- **Prompt Shields:** Uma solução (da Microsoft) projetada para proteger contra ataques de injeção de prompt, incluindo detecção, filtragem, destaque e delimitação de dados.
- **AsyncExitStack (Python):** Uma ferramenta de gerenciamento de contexto assíncrono em Python usada para garantir o uso e a limpeza adequados dos recursos.
- **uv:** Um gerenciador de pacotes e ambiente Python usado para criar e gerenciar projetos e ambientes virtuais.
- **npx:** Uma ferramenta de execução de pacotes Node.js que permite executar comandos de pacotes sem instalá-los globalmente.
- **MCP Inspector:** Uma ferramenta de desenvolvedor interativa para testar e depurar servidores MCP, permitindo a inspeção de ferramentas, recursos e prompts disponíveis, bem como logs.
- **Claude for Desktop:** Um aplicativo cliente MCP para macOS e Windows que pode se conectar a servidores MCP locais ou remotos para estender suas capacidades de IA.
- **claude_desktop_config.json:** O arquivo de configuração usado pelo Claude for Desktop para especificar quais servidores MCP conectar e como iniciá-los.