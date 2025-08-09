## 1. Introdução ao Tema
O Protocolo de Contexto de Modelo (Model Context Protocol - MCP) é uma especificação técnica padronizada que define como Modelos de Linguagem (LLMs) podem interagir de forma segura e estruturada com sistemas externos, como APIs, bancos de dados e ferramentas de software. Seu principal objetivo é permitir que agentes de IA acessem e utilizem recursos externos para executar tarefas que vão além da simples geração de texto, como consultar informações em tempo real ou executar ações em outros aplicativos.

Atuando como uma ponte entre o modelo de IA e o ambiente digital, o MCP utiliza uma arquitetura cliente-servidor modular e independente de linguagem de programação. Esta abordagem permite que um modelo de linguagem, operando dentro de uma aplicação anfitriã (Host), solicite a execução de funções ou o acesso a dados providos por um servidor. O protocolo gerencia essa comunicação, garantindo que as interações sejam seguras, com mecanismos para consentimento do usuário, autenticação e controle de acesso, transformando o LLM de um sistema de conversação em um agente capaz de atuar no mundo digital.

## 2. Pré-requisitos por Nível
### 2.1 Conhecimentos Necessários
- **Básico:**
    - Lógica de programação (variáveis, funções, condicionais).
    - Conceitos básicos de Python (sintaxe, tipos de dados).
    - Familiaridade com o formato de dados JSON.

- **Intermediário:**
    - Conhecimento de arquitetura cliente-servidor.
    - Programação de APIs (conceitos de REST, endpoints).
    - Conceitos de Modelos de Linguagem (LLM), como prompts e inferência.

- **Avançado:**
    - Protocolos de comunicação em rede (WebSockets, RPC - Remote Procedure Call).
    - Tópicos de segurança em sistemas distribuídos (autenticação, autorização).
    - Desenvolvimento de aplicações com frameworks web (como Flask ou FastAPI em Python).

### 2.2 Glossário de Conceitos-Chave
- **Model Context Protocol (MCP):** Um padrão de comunicação que permite a LLMs interagir com ferramentas e fontes de dados externas.
- **Host:** A aplicação onde o usuário interage e o modelo de IA está sendo executado (ex: um editor de código como o VS Code, um ambiente de desktop na nuvem).
- **Cliente (Client):** O componente, dentro do Host, responsável por gerenciar a comunicação entre o modelo de IA e o servidor MCP.
- **Servidor (Server):** O componente que expõe funcionalidades ao modelo. Ele fornece as ferramentas, os recursos e os prompts que podem ser utilizados.
- **Ferramenta (Tool):** Uma função ou um programa executável que o modelo pode invocar através do servidor para realizar uma tarefa específica (ex: consultar uma API de meteorologia).
- **Recurso (Resource):** Uma fonte de dados que o modelo pode acessar, como arquivos locais, registros de um banco de dados ou o conteúdo de uma API externa.
- **JSON-RPC:** Um protocolo de chamada de procedimento remoto (RPC) que utiliza o formato JSON para codificar as mensagens, garantindo uma comunicação leve e estruturada entre cliente e servidor.
- Exfiltração de dados—também conhecida como extrusão de dados ou exportação de dados—**é o roubo de dados: a transferência intencional, não autorizada e oculta de dados de um computador ou outro dispositivo**.

## 3. Explicação Detalhada

### A Arquitetura do MCP: Host, Cliente e Servidor
Para que um modelo de IA possa, por exemplo, ler um arquivo do seu computador ou consultar uma API, ele precisa de uma forma padronizada de se comunicar com o "mundo exterior". O MCP estrutura essa interação em três papéis distintos que trabalham em conjunto.

A intuição é a de uma delegação de tarefas. O modelo de IA identifica uma necessidade (ex: "preciso saber o clima em São Paulo"), mas não sabe como obtê-la. Ele então utiliza o MCP para solicitar essa informação a um componente especializado.

Os três papéis principais são:
- **Host:** É o ambiente onde a interação com o usuário acontece. Pode ser um editor de código, um sistema operacional ou uma aplicação web. Ele gerencia a interface do usuário, as permissões e inicia a conexão com os servidores.
- **Cliente:** Reside dentro do Host e atua como o intermediário. Ele pega a intenção do modelo de IA e a traduz em uma requisição formal para o servidor. Depois, recebe a resposta do servidor e a entrega de volta ao modelo.
- **Servidor:** É o "faz-tudo". Ele expõe um conjunto de capacidades que o modelo pode utilizar. É o servidor que efetivamente executa o código, acessa o banco de dados ou chama a API externa.

### As Capacidades de um Servidor MCP
Um servidor MCP pode oferecer três tipos principais de funcionalidades para um modelo de IA:

1.  **Recursos:** São fontes de dados estáticos ou dinâmicos. O modelo pode solicitar acesso a um recurso para obter contexto. Por exemplo, o conteúdo de um arquivo local, uma entrada em um banco de dados de produtos ou a documentação de uma API.
2.  **Prompts:** São modelos de texto (templates) que guiam o comportamento do modelo. Um servidor pode oferecer um prompt para "resumir um documento técnico" ou "gerar código a partir de uma especificação", garantindo que a IA execute tarefas recorrentes de forma consistente.
3.  **Ferramentas (Tools):** São a capacidade mais poderosa. Ferramentas são funções executáveis que o modelo pode invocar. Diferente dos recursos, as ferramentas realizam ações. A definição da ferramenta inclui seu nome, uma descrição do que ela faz, e os parâmetros que ela espera.

#### Exemplo Prático: Definindo uma Ferramenta em Python
Vamos criar um exemplo de uma ferramenta `get_weather` que um modelo de IA poderia utilizar. O servidor definiria esta função e a tornaria disponível. O LLM receberia a descrição da ferramenta (no docstring) e aprenderia a chamá-la quando o usuário perguntasse sobre o clima.

```python
# Importação de bibliotecas necessárias para um servidor web simples (ex: Flask)
# e para manipulação de JSON.
from flask import Flask, jsonify, request
import json

# Definição da Ferramenta (Tool)
# Esta é a função que o servidor MCP executará quando o LLM a invocar.
def get_weather(location: str) -> str:
    """
    Obtém a previsão do tempo para uma localidade específica.

    Args:
        location (str): A cidade e o estado. Ex: "São Paulo, SP".

    Returns:
        str: Uma string em formato JSON com a temperatura e a condição do tempo.
    """
    # Em um cenário real, esta função faria uma chamada a uma API de meteorologia.
    # Aqui, usamos dados simulados (mock) para o exemplo.
    print(f"[Servidor MCP] Ferramenta 'get_weather' invocada para: {location}")
    if "são paulo" in location.lower():
        forecast = {"location": location, "temperature": "22°C", "condition": "Ensolarado"}
    elif "rio de janeiro" in location.lower():
        forecast = {"location": location, "temperature": "28°C", "condition": "Parcialmente Nublado"}
    else:
        forecast = {"location": location, "temperature": "não disponível", "condition": "não disponível"}
    
    # A ferramenta retorna os dados em um formato estruturado (JSON string).
    return json.dumps(forecast)

# Simulação de um Servidor MCP usando Flask
# Este código expõe a ferramenta 'get_weather' através de um endpoint de API.
app = Flask(__name__)

@app.route('/invoke-tool', methods=['POST'])
def invoke_tool():
    data = request.json
    tool_name = data.get('tool_name')
    params = data.get('parameters')

    if tool_name == 'get_weather':
        location = params.get('location')
        if location:
            # Executa a ferramenta e retorna o resultado
            result = get_weather(location)
            return jsonify({"status": "success", "result": result})
        else:
            return jsonify({"status": "error", "message": "Parâmetro 'location' ausente."}), 400
    else:
        return jsonify({"status": "error", "message": "Ferramenta não encontrada."}), 404

# Para executar este servidor:
# 1. Instale o Flask: pip install Flask
# 2. Salve o código como 'mcp_server.py'
# 3. No terminal, execute: python mcp_server.py
# O servidor estará rodando e pronto para receber invocações da ferramenta.
```

### O Fluxo de Comunicação e Segurança
A comunicação entre os componentes segue uma sequência lógica e segura, orquestrada pelo protocolo JSON-RPC.

1.  **Iniciação:** O usuário faz uma pergunta no Host (ex: "Qual o clima em São Paulo?").
2.  **Negociação:** O Cliente se conecta ao Servidor e ambos "negociam" as capacidades disponíveis. O Servidor informa quais ferramentas, como a `get_weather`, estão disponíveis.
3.  **Invocação:** O LLM, percebendo a intenção do usuário, decide usar a ferramenta. O Cliente envia uma requisição ao Servidor para invocar `get_weather` com o parâmetro `location="São Paulo, SP"`.
4.  **Consentimento:** Um pilar do MCP é a segurança. Antes de executar a ferramenta, o Host pode solicitar a confirmação do usuário (ex: "A IA deseja acessar a API de meteorologia. Permitir?").
5.  **Execução e Resultado:** Após o consentimento, o Servidor executa a função `get_weather` e envia o resultado (o JSON com a previsão do tempo) de volta para o Cliente.
6.  **Integração:** O Cliente entrega o resultado ao LLM, que o utiliza para formular a resposta final ao usuário (ex: "O tempo em São Paulo está ensolarado, com temperatura de 22°C.").

Este fluxo garante que o modelo não execute ações arbitrárias. Cada passo é controlado, e a segurança, centrada no consentimento do usuário, é um componente integral do projeto do protocolo.


---

## Definição

O Protocolo de Contexto de Modelo (MCP) é um **padrão aberto e uma interface** que permite que aplicações e agentes de Inteligência Artificial (IA) se conectem e **trabalhem com suas fontes de dados e ferramentas externas**. Ele é descrito como um "adaptador universal" para aplicações de IA, similar ao USB-C para dispositivos físicos, que unifica como os modelos acessam ferramentas e dados.

**Propósito e Importância do MCP:** O objetivo principal do MCP é resolver desafios de escalabilidade e manutenção em aplicações de IA complexas, onde integrações personalizadas se tornam impraticáveis.

- **Para usuários de aplicações de IA**: O MCP torna as aplicações de IA mais úteis e contextualmente relevantes, permitindo que acessem informações e ferramentas que você usa diariamente, como documentos pessoais, dados de código ou calendários. Por exemplo, um assistente de IA pode ler notas de reunião do Google Drive e agendar acompanhamentos via um servidor MCP.
- **Para desenvolvedores**: O MCP **reduz significativamente o tempo e a complexidade de desenvolvimento** ao construir aplicações de IA que precisam interagir com diversas fontes de dados. Ele permite que os desenvolvedores criem servidores MCP reutilizáveis para fontes de dados (como Google Drive ou Slack) que podem ser aproveitados por várias aplicações, fomentando um ecossistema de código aberto.

**Como o MCP Funciona (Arquitetura e Conceitos Principais):** O MCP segue um **modelo cliente-servidor**, com três participantes principais:

- **Host MCP (Aplicação de IA)**: É a aplicação de IA (ex: Claude Desktop, Visual Studio Code) com a qual o usuário interage. Ele coordena e gerencia um ou múltiplos **clientes MCP**.
- **Cliente MCP**: É um componente de nível de protocolo instanciado pelo host, que mantém uma conexão dedicada e **um-para-um** com um **servidor MCP** específico. O cliente obtém contexto do servidor para o host usar.
- **Servidor MCP**: É um programa que expõe capacidades específicas aos clientes MCP através de interfaces de protocolo padronizadas. Os servidores podem ser executados **localmente ou remotamente**.

**Camadas do MCP:** O protocolo é dividido em duas camadas principais:

1. **Camada de Dados**: Implementa um protocolo de troca baseado em **JSON-RPC 2.0**, que define a estrutura e a semântica das mensagens. Esta camada inclui gerenciamento do ciclo de vida (inicialização, negociação de capacidade, término da conexão) e define as **primitivas** que servidores e clientes podem expor.
2. **Camada de Transporte**: Gerencia os canais de comunicação e a autenticação entre clientes e servidores. Os dois mecanismos de transporte suportados são:
    - **Stdio transport**: Utiliza fluxos de entrada/saída padrão para comunicação direta de processo, ideal para servidores locais na mesma máquina, sem sobrecarga de rede. É crucial **nunca escrever para a saída padrão (stdout)** em servidores STDIO, pois isso corromperia as mensagens JSON-RPC.
    - **Streamable HTTP transport**: Utiliza HTTP POST para mensagens cliente-servidor e, opcionalmente, Server-Sent Events (SSE) para streaming. É usado para comunicação com servidores remotos e suporta métodos de autenticação HTTP padrão, como tokens de portador e API keys (OAuth é recomendado para obtenção de tokens).

**Primitivas do MCP:** As primitivas definem o que clientes e servidores podem oferecer um ao outro.

- **Primitivas que os servidores podem expor (Servidor MCP)**:
    
    - **Ferramentas (Tools)**: Funções executáveis que os modelos de IA podem invocar para realizar ações (ex: buscar voos, enviar e-mails, criar eventos de calendário, operações de arquivo, consultas de banco de dados). A execução de ferramentas **exige aprovação explícita do usuário**.
    - **Recursos (Resources)**: Expõem dados estruturados (ex: arquivos, respostas de API, registros de banco de dados) que a IA precisa para entender o contexto. Eles usam identificação baseada em URI e suportam recursos diretos (URIs fixas) e modelos de recursos (URIs parametrizadas).
    - **Prompts (Prompts)**: Modelos estruturados e reutilizáveis que definem entradas esperadas e padrões de interação, guiando o comportamento da IA. São controlados pelo usuário e exigem invocação explícita.
- **Primitivas que os clientes podem expor (Cliente MCP)**:
    
    - **Amostragem (Sampling)**: Permite que os servidores solicitem conclusões do modelo de linguagem através do cliente, mantendo o controle e a segurança do usuário. Isso é útil para servidores que precisam de assistência de LLM sem integrar um SDK de LLM diretamente. O fluxo de amostragem envolve múltiplos pontos de controle humano-em-loop para revisão e aprovação pelo usuário.
    - **Elicitação (Elicitation)**: Permite que os servidores solicitem informações específicas adicionais dos usuários durante as interações. Não solicita senhas ou chaves API.
    - **Raízes (Roots)**: Definem limites do sistema de arquivos para operações do servidor, especificando quais diretórios o servidor pode acessar. Isso guia os servidores para diretórios relevantes enquanto mantém limites de segurança.
    - **Registro (Logging)**: Permite que os servidores enviem mensagens de log aos clientes para depuração e monitoramento.

**Negociação de Versão:** O MCP utiliza identificadores de versão baseados em strings no formato `YYYY-MM-DD`, indicando a última data em que foram feitas alterações incompatíveis com versões anteriores. Durante a inicialização da conexão, clientes e servidores negociam uma **única versão compatível** para usar na sessão, mesmo que ambos suportem múltiplas versões.

**Linguagens e Ferramentas Suportadas:** O MCP é flexível e projetado para funcionar com qualquer linguagem de programação. Existem SDKs oficiais e exemplos disponíveis para:

- Python
- JavaScript/TypeScript
- Java (incluindo Spring AI)
- C# (.NET)
- Kotlin

Ferramentas de desenvolvimento como o **MCP Inspector** (uma ferramenta interativa para testar e depurar servidores MCP) e o **AI Toolkit para Visual Studio Code** (que oferece um ambiente completo de desenvolvimento de IA no VS Code) ajudam na construção e teste de aplicações MCP.

Em resumo, o MCP visa ser a "USB-C da IA", proporcionando uma maneira padronizada, segura e escalável para que os modelos de IA acessem e interajam com o mundo exterior, permitindo a construção de **sistemas mais inteligentes, consistentes e capazes de agir**.

O **Protocolo de Contexto de Modelo (MCP)** é definido como um **padrão aberto e uma interface** que permite que aplicações e agentes de Inteligência Artificial (IA) se **conectem e trabalhem com suas fontes de dados e ferramentas externas**. A maneira mais intuitiva de entender o MCP é pensá-lo como um **"adaptador universal" para aplicações de IA**, de forma muito **similar ao que o USB-C é para dispositivos físicos**.

**A Analogia com o USB-C:**

Assim como o USB-C atua como um adaptador universal para conectar dispositivos a vários periféricos e acessórios, unificando a forma como os dispositivos físicos se conectam, o MCP faz o mesmo para a IA: ele **unifica a forma como os modelos de IA acessam ferramentas e dados**.

Antes do USB-C, você precisava de cabos diferentes para conexões diferentes. Da mesma forma, antes do MCP, os desenvolvedores tinham que construir **conexões personalizadas e únicas para cada fonte de dados ou ferramenta** que desejavam que sua aplicação de IA utilizasse. Esse processo era **demorado e muitas vezes resultava em funcionalidade limitada**.

**Por que essa analogia é crucial e o que ela significa para o MCP?**

1. **Simplificação e Redução da Complexidade**: Com o MCP, os desenvolvedores podem **adicionar facilmente conexões às suas aplicações de IA**, tornando-as **muito mais poderosas desde o primeiro dia**. Ele atua como uma **camada universal** para que o modelo possa interagir com qualquer ferramenta ou recurso de forma consistente.
2. **Interoperabilidade e Reusabilidade**: A padronização que o MCP traz abre a porta para a construção de sistemas mais inteligentes e "agentic" (autônomos). Ferramentas e fontes de dados podem ser **plugadas uma única vez e reutilizadas em vários modelos ou projetos**, facilitando a extensão de funcionalidades no futuro. Isso significa que, uma vez que algo "fala MCP", seu agente de IA pode usá-lo sem a necessidade de instruções personalizadas.
3. **Escalabilidade**: O MCP foi projetado para resolver os desafios de **escalabilidade e manutenibilidade** que surgem ao construir aplicações de IA generativas mais complexas, especialmente quando elas precisam se conectar a dados em tempo real e chamar ferramentas. A arquitetura modular do MCP permite que novas capacidades sejam adicionadas sem alterar as próprias aplicações de IA, assim como adicionar novos acessórios a um computador sem precisar de uma atualização completa do sistema. Você pode escalar um modelo com muitos servidores, cada um com diferentes capacidades, e o agente automaticamente reconhece as ferramentas disponíveis sem necessidade de "fiação" extra.
4. **Benefícios para Usuários e Desenvolvedores**:
    - **Para usuários de aplicações de IA**: O MCP permite que suas aplicações de IA **acessem as informações e ferramentas que você usa diariamente** (como documentos pessoais do Google Drive ou dados do GitHub). Isso torna a IA **muito mais útil e contextualmente relevante**, pois ela pode entender seus documentos e contexto de trabalho específicos, em vez de se limitar ao seu conhecimento pré-existente.
    - **Para desenvolvedores**: O MCP **reduz drasticamente o tempo e a complexidade de desenvolvimento** ao construir aplicações de IA que precisam acessar várias fontes de dados. Em vez de criar conectores personalizados duplicados, os desenvolvedores podem construir **servidores MCP reutilizáveis** para fontes de dados, o que promove um ecossistema de código aberto e permite o aproveitamento de trabalho existente.

Em resumo, a analogia do "USB-C da IA" é fundamental para a Introdução do MCP porque ela comunica de forma eficaz a missão principal do protocolo: **padronizar e simplificar a integração de capacidades externas para a IA**, tornando-a mais poderosa, flexível e acessível tanto para quem desenvolve quanto para quem usa.

## Objetivo

 O objetivo fundamental do MCP é resolver um desafio crítico na construção de aplicações de IA generativas que vão além de simples chatbots. Antes do MCP, ao tentar criar aplicações de IA mais complexas que precisavam interagir com o "mundo exterior" – seja acessando dados em tempo real ou chamando ferramentas externas – os desenvolvedores se deparavam com a necessidade de construir **integrações personalizadas e "one-off"** para cada fonte de dados ou ferramenta. Esse processo era **demorado, resultava em funcionalidade limitada e era difícil de escalar e manter**.

### O Problema: Aplicações de IA Isoladas

Tradicionalmente, os modelos de IA eram limitados ao conhecimento com o qual foram treinados ou às informações diretamente fornecidas a eles. Eles não tinham uma maneira padronizada e eficiente de:

- Acessar **dados em tempo real**.
- Chamar **ferramentas externas** como calculadoras, motores de busca, sistemas de CRM ou APIs.
- Integrar-se com **fontes de dados pessoais ou empresariais**, como arquivos locais, documentos em nuvem (Google Drive), bases de dados ou repositórios de código (GitHub).

Essa falta de conectividade tornava as aplicações de IA menos úteis e contextualmente relevantes para as necessidades diárias dos usuários e os fluxos de trabalho empresariais.

### A Solução do MCP: Um "Adaptador Universal para IA"

O MCP foi concebido para ser a ponte que supera essa limitação. Seu objetivo é ser um **padrão aberto e uma interface padronizada** que permite que aplicações e agentes de IA se **conectem e trabalhem com suas fontes de dados e ferramentas externas** de forma consistente.

A analogia frequentemente utilizada é a de um **"adaptador universal" para aplicações de IA, similar ao que o USB-C é para dispositivos físicos**. Assim como o USB-C unificou a forma como os dispositivos se conectam a periféricos, o MCP unifica a forma como os modelos de IA acessam ferramentas e dados.

### Benefícios e Resultados do Objetivo do MCP:

Ao atingir esse objetivo de conectividade universal, o MCP oferece benefícios significativos para diferentes públicos:

### Para Usuários de Aplicações de IA

 **Aplicações Mais Úteis e Contextualmente Relevantes**: O MCP permite que a IA acesse **informações e ferramentas que os usuários usam diariamente**, como documentos do Google Drive, dados do GitHub ou calendários. Isso significa que a IA pode entender o contexto de trabalho específico do usuário, em vez de se limitar ao seu conhecimento pré-existente.
**Habilidade de Tomar Ação**: A IA não apenas responde inteligentemente, mas também pode **tomar ações no mundo real** através de ferramentas, como agendar reuniões, enviar mensagens ou criar documentos.
### Para Desenvolvedores:

**Redução do Tempo e Complexidade de Desenvolvimento**: Em vez de construir conexões personalizadas para cada fonte de dados e aplicação, os desenvolvedores podem construir **servidores MCP reutilizáveis**.
**Reusabilidade e Consistência**: Uma vez que uma ferramenta ou fonte de dados "fala MCP", ela pode ser plugada e reutilizada em vários modelos ou projetos, facilitando a extensão de funcionalidades futuras.
**Ecossistema Open Source**: O MCP fomenta um ecossistema onde o trabalho existente pode ser alavancado, resultando em um desenvolvimento mais rápido e consistente.
**Escalabilidade e Manutenibilidade**: A arquitetura modular do MCP permite que novas capacidades sejam adicionadas sem alterar as próprias aplicações de IA, promovendo a escalabilidade e a manutenibilidade de aplicações de IA generativas complexas.
### Interoperabilidade

A interoperabilidade é um dos benefícios mais fundamentais e transformadores do Protocolo de Contexto de Modelo (MCP), especialmente no contexto da sua introdução e conceitos principais.
Em sua essência, o MCP foi projetado para ser um **padrão aberto e uma interface** que permite que aplicações e agentes de Inteligência Artificial (IA) se **conectem e trabalhem com suas fontes de dados e ferramentas externas**. Ele atua como um **"adaptador universal" para aplicações de IA**, de forma muito **similar ao que o USB-C é para dispositivos físicos**, unificando a maneira como os modelos de IA acessam ferramentas e dados.
Aqui estão os pontos-chave sobre a interoperabilidade proporcionada pelo MCP e seus benefícios:
- **Eliminação de Integrações Customizadas**: Antes do MCP, os desenvolvedores precisavam criar conexões personalizadas e únicas para cada fonte de dados ou ferramenta que uma aplicação de IA deveria usar. Esse processo era demorado e limitava a funcionalidade. O MCP resolve isso fornecendo uma **camada universal** que permite aos modelos de IA interagir com qualquer ferramenta ou recurso de forma **consistente**.    
- **Trabalho entre Diferentes Fornecedores e Plataformas**: O MCP explicitamente permite que se **trabalhe em diferentes fornecedores e plataformas**. Essa padronização possibilita que aplicações de IA e servidores MCP sejam construídos em diversas linguagens de programação, incluindo Python, Java, JavaScript, TypeScript, C# e Kotlin. Isso significa que, independentemente da _stack_ de tecnologia, os componentes podem "falar MCP" e funcionar juntos.
- **Reusabilidade de Componentes**: A padronização do MCP permite que **ferramentas e fontes de dados sejam "plugadas" uma única vez e reutilizadas em vários modelos ou projetos**. Por exemplo, um servidor MCP de código aberto para o Google Drive pode ser usado por diversas aplicações compatíveis com MCP, eliminando a necessidade de cada desenvolvedor construir sua própria conexão. Isso promove um **ecossistema de código aberto** onde o trabalho existente pode ser alavancado.		    
- **Escalabilidade e Flexibilidade**: A arquitetura modular do MCP, com seus participantes (Host, Cliente, Servidor) e camadas de dados e transporte, contribui para a interoperabilidade e escalabilidade. Novas capacidades podem ser adicionadas conectando novos servidores MCP, sem a necessidade de alterar as próprias aplicações de IA. Isso permite que um modelo seja escalado com múltiplos servidores, cada um com diferentes capacidades, e o agente de IA automaticamente reconhece as ferramentas disponíveis sem necessidade de "fiação" extra.    
- **Comunicação Padronizada**: O MCP utiliza o **JSON-RPC 2.0** como protocolo subjacente para a troca de dados, e sua camada de transporte abstrai os detalhes de comunicação, permitindo o mesmo formato de mensagem JSON-RPC 2.0 em todos os mecanismos de transporte (Stdio e HTTP Transmitível). Isso garante uma comunicação clara e previsível entre clientes e servidores, independentemente do tipo de conexão. Além disso, a **negociação de versão** durante a inicialização da conexão garante que clientes e servidores concordem em uma única versão compatível do protocolo a ser usada, mantendo a interoperabilidade ao longo do tempo.
Em resumo, a interoperabilidade proporcionada pelo MCP é um benefício chave que se traduz em **consistência** no comportamento dos modelos, **desenvolvimento mais rápido** e menos complexo para os desenvolvedores, e a capacidade de construir aplicações de IA que se **integram perfeitamente** com as ferramentas e dados do mundo real.

Em suma, o objetivo central do MCP é **libertar a IA do seu "silobanking" de dados e funcionalidades**, permitindo que ela se integre de forma segura e padronizada com a vasta gama de informações e capacidades disponíveis no mundo real. Isso leva a aplicações de IA mais poderosas, adaptáveis e genuinamente úteis.

### Consistência

A **consistência**, no sentido de **modelos de IA se comportarem de maneira uniforme** ao interagir com ferramentas e dados, é um dos principais benefícios e um pilar fundamental do Model Context Protocol (MCP).

O MCP foi concebido como um **padrão aberto e uma interface padronizada** que permite que aplicações e agentes de IA se **conectem e trabalhem com suas fontes de dados e ferramentas externas**. Essa padronização é a chave para alcançar a consistência.

Vamos detalhar como o MCP proporciona essa consistência e quais são os seus benefícios:

- **Comportamento Uniforme em Diversas Ferramentas e Fontes de Dados**:
    
    - O MCP atua como uma **camada universal**, similar ao USB-C para dispositivos físicos. Assim como um dispositivo USB-C pode se conectar a qualquer periférico compatível, um modelo de IA que "fala MCP" pode **interagir com qualquer ferramenta ou recurso de forma consistente**, independentemente de sua implementação subjacente ou da plataforma onde o servidor MCP está sendo executado.
    - Antes do MCP, os desenvolvedores precisavam criar integrações personalizadas para cada fonte de dados ou ferramenta, o que resultava em funcionalidades limitadas e difícil escalabilidade. O MCP elimina essa necessidade, garantindo que o comportamento seja previsível em diversas integrações.
    
- **Reusabilidade e Consistência para Desenvolvedores**:
    
    - Um dos grandes benefícios para os desenvolvedores é a **reusabilidade**. Uma vez que um servidor MCP ou uma ferramenta é construída para "falar MCP", ela pode ser **plugada e reutilizada em vários modelos ou projetos**. Isso significa que a lógica e o comportamento definidos para uma ferramenta (por exemplo, `get_alerts` ou `get_forecast` de um servidor de clima) serão consistentes, não importa qual aplicação de IA ou modelo esteja usando-a.
    - Essa capacidade de reutilização reduz significativamente o tempo de desenvolvimento e a complexidade, pois os desenvolvedores não precisam mais "começar do zero" para cada nova conexão. Ao invés disso, eles podem aproveitar um ecossistema de servidores MCP existentes de código aberto.
- **Experiência do Usuário Aprimorada**:
    
    - Para os usuários de aplicações de IA, a consistência se traduz em uma **experiência mais útil e confiável**. As aplicações de IA podem acessar informações e ferramentas que os usuários usam diariamente (como Google Drive ou GitHub). Isso significa que a IA não está limitada ao seu conhecimento pré-existente, mas pode entender o contexto de trabalho específico do usuário de maneira **uniforme e previsível**.
    - A padronização permite que a IA não apenas responda inteligentemente, mas também **tome ações no mundo real** de forma consistente, como agendar reuniões ou criar documentos, porque ela interage com as ferramentas de uma maneira padronizada.

Em suma, a consistência promovida pelo MCP assegura que os **modelos de IA se comportem de maneira uniforme** ao interagir com o "mundo real" através de ferramentas e dados. Isso é alcançado pela sua arquitetura padronizada e modular, que permite a reutilização de componentes e simplifica a integração, beneficiando tanto os desenvolvedores (com maior agilidade e menos retrabalho) quanto os usuários (com aplicações de IA mais confiáveis, úteis e contextualmente relevantes).

### Reutilização

A **reutilização** — a capacidade de "construir uma vez e usar em qualquer lugar" — é um dos principais benefícios e um conceito central do Protocolo de Contexto de Modelo (MCP), que visa transformar a forma como as aplicações de IA generativas interagem com o mundo real.

### O Problema Antes do MCP

Antes da existência do MCP, o desenvolvimento de aplicações de IA que precisavam interagir com dados externos ou ferramentas era um processo **demorado e complexo**. Para cada nova fonte de dados ou ferramenta (como Google Drive, Slack, calculadoras ou motores de busca), os desenvolvedores tinham que criar **integrações personalizadas e "one-off"**. Isso resultava em:

- **Funcionalidade limitada**: As integrações eram muitas vezes específicas para uma única aplicação ou caso de uso.
- **Dificuldade de escalabilidade e manutenção**: Alterações em uma ferramenta ou dados exigiam modificações em múltiplas integrações customizadas, tornando o código frágil e caro de manter.
- **Trabalho duplicado**: Cada desenvolvedor que quisesse conectar sua aplicação de IA a uma ferramenta comum (como o Google Drive) precisava construir sua própria conexão, repetindo o esforço.

### A Solução do MCP: Reutilização Habilitada pela Padronização

O MCP resolve esse problema atuando como um **"adaptador universal" para aplicações de IA**, similar ao que o USB-C é para dispositivos físicos. Ele é um **padrão aberto e uma interface padronizada** que permite que aplicações e agentes de IA se conectem e trabalhem com suas fontes de dados e ferramentas externas de forma consistente.

Veja como o MCP possibilita a reutilização e os benefícios associados:

- **Construa uma Vez, Use em Qualquer Lugar**:    
    - Com o MCP, uma vez que uma **ferramenta ou fonte de dados "fala MCP"**, ela pode ser "plugada" e **reutilizada em vários modelos ou projetos**. Isso significa que, ao invés de construir uma nova conexão para cada aplicação, os desenvolvedores podem construir **servidores MCP reutilizáveis** para fontes de dados.
    - Por exemplo, um servidor MCP de código aberto para o Google Drive pode ser utilizado por muitas aplicações diferentes que são compatíveis com o MCP, eliminando a necessidade de cada desenvolvedor criar sua própria conexão personalizada.
- **Consistência e Interoperabilidade**:
    - A padronização do MCP garante que **modelos de IA se comportem de maneira uniforme** com qualquer ferramenta. Essa consistência é um benefício direto da capacidade de reutilização, pois o comportamento de uma ferramenta é definido uma vez no servidor MCP e mantido em todas as integrações.
    - Além disso, o MCP permite trabalhar **"across different vendors and platforms"** (em diferentes fornecedores e plataformas), aumentando a interoperabilidade de todo o ecossistema de IA.
- **Desenvolvimento Mais Rápido**:    
    - A reutilização de servidores e ferramentas MCP existentes **reduz significativamente o tempo de desenvolvimento e a complexidade**. Os desenvolvedores não precisam mais "começar do zero" para cada nova integração.
    - Isso permite que os desenvolvedores se concentrem em construir **excelentes experiências de IA**, em vez de se preocuparem repetidamente com a criação de conectores personalizados.
- **Ecossistema de Código Aberto Crescente**:    
    - O MCP fomenta um **ecossistema de código aberto** de servidores e ferramentas. Isso significa que o trabalho já feito pode ser alavancado por outros, acelerando a inovação e o desenvolvimento de novas capacidades.
    - Desenvolvedores da Anthropic, contribuidores de código aberto, equipes de desenvolvimento empresarial e fornecedores de software estão todos criando e mantendo servidores MCP, enriquecendo o ecossistema de ferramentas reutilizáveis.
- **Extensibilidade e Manutenibilidade**:    
    - O sistema modular do MCP permite que **novas capacidades sejam adicionadas sem alterar as próprias aplicações de IA**. É como adicionar novos acessórios a um computador sem precisar atualizar o sistema inteiro.
    - Isso torna as aplicações de IA mais **escaláveis, flexíveis e fáceis de manter** a longo prazo, pois novas ferramentas podem ser "plugadas" e o agente de IA automaticamente reconhece as novas funcionalidades sem "fiação" extra.

Em resumo, a **reutilização é um benefício-chave do MCP que transforma a paisagem do desenvolvimento de IA**, permitindo que as ferramentas e fontes de dados sejam desenvolvidas uma única vez e aplicadas de forma consistente e eficiente em diversas aplicações e modelos de IA, impulsionando o desenvolvimento e a inovação.

### Desenvolvimento Rápido
O **desenvolvimento mais rápido**, com a capacidade de **"construir uma vez, usar em qualquer lugar"** e **"sem começar do zero"**, é um dos benefícios mais significativos e um pilar fundamental do Model Context Protocol (MCP).

Antes do MCP, os desenvolvedores de aplicações de IA generativas que precisavam interagir com dados externos ou ferramentas enfrentavam um desafio considerável: a necessidade de criar **integrações personalizadas e únicas** para cada nova fonte de dados ou ferramenta (como Google Drive, Slack, calculadoras, motores de busca, etc.). Esse processo era **demorado e complexo**, resultando em funcionalidades limitadas e dificuldade de escalabilidade e manutenção. Havia um trabalho duplicado significativo, pois cada desenvolvedor que desejava conectar sua aplicação de IA a uma ferramenta comum precisava construir sua própria conexão.

O MCP foi criado para solucionar esses problemas, agindo como um **"adaptador universal" para aplicações de IA**, similar ao USB-C para dispositivos físicos. Ele é um **padrão aberto e uma interface padronizada** que permite que aplicações e agentes de IA se conectem e trabalhem com suas fontes de dados e ferramentas externas de forma consistente.

Veja como o MCP acelera o desenvolvimento, permitindo que você **não precise começar do zero**:

- **Eliminação de Integrações Customizadas**: O MCP simplifica o processo ao permitir que os desenvolvedores **adicionem conexões facilmente** às suas aplicações de IA, tornando-as muito mais poderosas desde o primeiro dia. Isso elimina a necessidade de construir continuamente conectores personalizados.
- **Reusabilidade de Servidores MCP**: Com o MCP, uma vez que um servidor é construído para "falar MCP", ele pode ser **"plugado" e reutilizado em vários modelos ou projetos**. Por exemplo, um servidor MCP de código aberto para o Google Drive pode ser utilizado por muitas aplicações diferentes que são compatíveis com o MCP, eliminando a necessidade de cada desenvolvedor construir sua própria conexão personalizada. Essa capacidade de reutilização reduz significativamente o tempo de desenvolvimento e a complexidade.
- **Foco na Experiência de IA**: Ao terceirizar a complexidade da integração para o protocolo, os desenvolvedores podem **se concentrar em construir excelentes experiências de IA**, em vez de se preocuparem repetidamente com a criação de conectores personalizados.
- **Ecossistema de Código Aberto**: O MCP fomenta um **ecossistema de código aberto de servidores e ferramentas**. Isso significa que o trabalho já feito pode ser aproveitado por outros, acelerando a inovação e o desenvolvimento de novas capacidades. Desenvolvedores da Anthropic, contribuidores de código aberto, equipes de desenvolvimento empresarial e fornecedores de software estão todos criando e mantendo servidores MCP, enriquecendo o ecossistema de ferramentas reutilizáveis.
- **Extensibilidade Modular**: O sistema modular do MCP permite que **novas capacidades sejam adicionadas sem alterar as próprias aplicações de IA**. É como adicionar novos acessórios a um computador sem precisar atualizar o sistema inteiro. Isso torna as aplicações de IA mais escaláveis, flexíveis e fáceis de manter a longo prazo, pois novas ferramentas podem ser "plugadas" e o agente de IA automaticamente reconhece as novas funcionalidades sem "fiação" extra.

Em resumo, o MCP acelera o desenvolvimento porque transforma a integração de IA de um processo de "construir do zero" para cada conexão em um modelo de **"construir uma vez, usar em qualquer lugar"**, aproveitando a padronização e um crescente ecossistema de servidores reutilizáveis.

### Reduções de Alucinações 

A **redução de alucinações**, através da **base em dados reais**, é um dos benefícios cruciais proporcionados pelo Model Context Protocol (MCP).

Tradicionalmente, os modelos de IA generativa são limitados ao conhecimento contido nos seus dados de treino. Quando confrontados com perguntas que exigem informações atualizadas, específicas do utilizador ou não presentes nos seus dados de formação, os modelos podem "alucinar", ou seja, gerar respostas plausíveis, mas incorretas ou inventadas.

O MCP aborda este problema fundamental da seguinte forma:

- **Acesso a Dados do Mundo Real**: O MCP atua como um "adaptador universal" para aplicações de IA, permitindo que estas se conectem a **fontes de dados e ferramentas externas**. Isso significa que, em vez de depender apenas do seu conhecimento pré-treinado, o modelo de IA pode aceder a **informações em tempo real** e dados específicos do contexto do utilizador.
- **Fundamentação em Contexto Específico**: Com os servidores MCP, as aplicações de IA podem aceder a **documentos pessoais, dados e contexto de trabalho** do utilizador, como ficheiros no Google Drive ou informações sobre uma base de código no GitHub. Isso garante que a assistência fornecida seja **personalizada e contextualmente relevante**, minimizando a necessidade de o modelo "inventar" informações.
- **Capacidade de Ação e Recuperação de Informação**: Quando um modelo de IA precisa de ajuda para responder a uma pergunta ou realizar uma tarefa que exija dados externos (como pesquisar na web ou realizar cálculos), ele pode **comunicar-se com o servidor MCP**. O servidor executa a ferramenta necessária (como um motor de busca ou uma calculadora) e retorna o resultado. Este processo de **recuperação de dados verificáveis** e a capacidade de **tomar ações no mundo real** diretamente com base nesses dados ajuda a **reduzir as alucinações** ao fundamentar o modelo em informações concretas e atuais.

Em suma, o MCP permite que os modelos de IA "vejam" o mundo real através das ferramentas e dados a que se conectam, capacitando-os a fornecer respostas mais precisas, relevantes e confiáveis, em vez de recorrer a informações imaginadas.

### Segurança 

A segurança das informações sensíveis é um **benefício fundamental** e uma prioridade central no design do Model Context Protocol (MCP), que visa estender as capacidades das aplicações de IA ao interagir com dados e ferramentas externas.

O MCP foi desenvolvido com mecanismos robustos para **proteger dados confidenciais** e garantir que as interações com a IA sejam controladas e transparentes.

Aqui estão os principais aspectos de como o MCP aborda a segurança de informações sensíveis:

- **Controle e Consentimento do Usuário (Human-in-the-Loop)**:    
    - O MCP enfatiza que **cada chamada de ferramenta e acesso a dados deve ser aprovado pelo usuário**, garantindo que os usuários mantenham controle total sobre o que é compartilhado e executado pelo modelo de IA.
    - As aplicações devem **exibir claramente as ferramentas disponíveis** e fornecer indicadores visuais quando as ferramentas estão sendo consideradas ou usadas.
    - Antes de qualquer execução de ferramenta, os usuários devem ser apresentados a **diálogos de aprovação claros que expliquem exatamente o que a ferramenta fará**.
    - No contexto de "amostragem" (sampling), onde servidores solicitam conclusões de modelos de linguagem através do cliente, há **múltiplos pontos de controle humano-em-loop**. Os usuários revisam e podem modificar tanto a solicitação inicial quanto a resposta gerada antes que ela retorne ao servidor. Esse design "human-in-the-loop" assegura que as interações de IA iniciadas pelo servidor não comprometam a segurança sem o consentimento explícito do usuário.
    - Para a "elicitação", que permite a servidores solicitarem informações adicionais dos usuários, a privacidade é uma consideração chave: **elicitação nunca solicita senhas ou chaves de API**, e os clientes devem avisar sobre solicitações suspeitas e permitir que os usuários revisem os dados antes de enviá-los.
- **Gerenciamento Seguro de Chaves de API e Segredos**:    
    - As fontes enfatizam a necessidade de **manter as chaves de API seguras**, recomendando o armazenamento em arquivos `.env`, `user-secrets`, variáveis de ambiente ou gerenciadores de segredos.
- **Gerenciamento de Permissões (Princípio do Menor Privilégio)**:
    - Os servidores MCP devem operar sob o **princípio do menor privilégio**, tendo acesso apenas aos dados e diretórios estritamente necessários para suas funções.
    - Os usuários podem **controlar quais ferramentas o Claude tem permissão para usar** através das configurações do conector, habilitando ou desabilitando ferramentas específicas e configurando limites de uso.
    - Para servidores de sistema de arquivos, as configurações determinam explicitamente quais diretórios o servidor pode acessar, e os desenvolvedores são aconselhados a conceder acesso apenas a diretórios com os quais se sintam confortáveis para que a IA leia e modifique.
    - É importante **validar todas as respostas externas** para evitar o uso de dados inesperados ou inseguros e ter cautela com as permissões das ferramentas.
- **Mecanismos de Autenticação Seguros**:    
    - Servidores MCP remotos frequentemente exigem **autenticação segura** (OAuth, chaves de API, nome de usuário/senha) para acesso aos recursos. O MCP recomenda o uso de OAuth para obter tokens de autenticação.
    - A especificação MCP **proíbe explicitamente o "token pass-through"** (quando o cliente passa seu token diretamente para o recurso downstream), pois isso contorna controles de segurança críticos, confunde a trilha de auditoria e quebra os limites de confiança entre os serviços. A regra é aceitar apenas tokens emitidos especificamente para o servidor MCP.
    - Desde abril de 2025, os servidores MCP podem delegar a provedores de identidade externos, como o Microsoft Entra ID, o que melhora significativamente a autenticação.
- **Isolamento e Redação de Dados**:    
    - As solicitações de amostragem são **isoladas do contexto principal da conversa por padrão**, o que significa que os servidores não podem acessar as conversas dos usuários diretamente.
    - Os clientes podem oferecer opções para **redigir informações sensíveis**.
    - Se uma ferramenta puder expor dados sensíveis, ela deve **redigi-los por padrão**, a menos que solicitado explicitamente e o usuário esteja autorizado .
- **Registro (Logging) e Monitoramento**:    
    - O protocolo permite que os servidores enviem **mensagens de log aos clientes para depuração e monitoramento**.
    - Os logs relacionados ao MCP no Claude Desktop, por exemplo, contêm informações sobre conexões e falhas, incluindo logs de erro (stderr) dos servidores nomeados, o que é vital para auditoria e segurança.
    - É essencial **habilitar o log e o monitoramento** como parte de uma postura de segurança robusta.
- **Postura de Segurança do Ambiente Geral**    
    - O MCP **herda a postura de segurança do ambiente** em que é implementado. Portanto, um ambiente mais seguro resulta em uma implementação MCP mais segura.
    - Isso inclui a adesão a **práticas de codificação seguras** (como as diretrizes OWASP), o **endurecimento de servidores**, o uso de **autenticação multifator (MFA)** e **aplicação regular de patches**.
    - É recomendado projetar com uma **arquitetura de confiança zero** em mente.
- **Mitigação de Ameaças Específicas da IA**    
    - O MCP reconhece e busca mitigar riscos como **injeção de prompt**, **envenenamento de ferramentas** e **modificação dinâmica de ferramentas**, que podem levar à exfiltração de dados ou ações não intencionais.
    - **Injeção Indireta de Prompt**: Ocorre quando instruções maliciosas são ocultadas em contextos externos (e-mail, web, PDF), levando a ações não intencionais. Soluções como **Prompt Shields da Microsoft** (que incluem detecção, filtragem, "spotlighting" e delimitação de dados) são cruciais para proteger contra esses ataques.
    - **Envenenamento de Ferramentas**: Consiste na adulteração dos metadados de uma ferramenta MCP para induzir o LLM a comportamentos perigosos, representando um risco significativo em ambientes hospedados (o "rugpull").
    - **Segurança da Cadeia de Suprimentos**: É vital verificar a fonte de todos os componentes (modelos, APIs) e usar pipelines de implantação seguros, varreduras de vulnerabilidade e monitoramento contínuo.

Em suma, a segurança das informações sensíveis é um **benefício intrínseco e conscientemente projetado no MCP**, permitindo que as aplicações de IA utilizem dados do mundo real de forma confiável e controlada, minimizando os riscos associados à interação com sistemas externos.

### Novas Capacidades para Modelos

O Model Context Protocol (MCP) proporciona às aplicações e modelos de IA, especialmente os Large Language Models (LLMs), a capacidade de adquirir **novas funcionalidades que não foram originalmente treinadas para realizar**. Isto é conseguido ao permitir que se **conectem e interajam com o "mundo exterior"** através de uma interface padronizada e aberta.

Estas novas capacidades podem ser categorizadas da seguinte forma:

- **Acesso a Dados em Tempo Real e Informações Externas**:
    
    - Os modelos deixam de estar limitados ao conhecimento contido nos seus dados de pré-treino.
    - Ganham a capacidade de aceder a **informações em tempo real**, a **documentos, dados e contexto de trabalho específicos do utilizador** (como ficheiros no Google Drive ou informações sobre bases de código no GitHub).
    - Isso resulta numa **assistência mais personalizada e contextualmente relevante** e ajuda a **reduzir as alucinações**, fundamentando as respostas em dados concretos e atuais [Sua resposta anterior sobre "Redução de Alucinações", 260].
    - Podem recuperar **documentação** em tempo real e aceder a dados de diversas fontes, como **ficheiros, APIs e bases de dados**.
- **Habilidade de Realizar Ações no Mundo Real (Ferramentas)**:    
    - O MCP permite que os modelos não apenas respondam inteligentemente, mas também **"tomem ações"**.
    - Estas ações são executadas através de **"Ferramentas"** expostas pelos servidores MCP.
    - Exemplos específicos de ações que os modelos podem agora realizar incluem:
        - **Pesquisar na web ou em serviços específicos** (ex: Brave Search, APIs de clima), como obter alertas meteorológicos (`get_alerts`) e previsões (`get_forecast`).
        - **Operações no sistema de ficheiros**: ler, criar, mover, renomear e pesquisar ficheiros/diretórios no computador do utilizador.
        - **Gestão de calendário**: agendar reuniões, criar eventos.
        - **Operações de email**: enviar notificações de ausência.
        - **Automatizar fluxos de trabalho**: atualizar itens do Azure DevOps com base em dados do YouTube.
        - **Automação de navegador**: abrir páginas web, clicar em botões, extrair conteúdo, tirar capturas de ecrã, e executar fluxos de teste completos.
        - **Automação para desenvolvedores**: clonar repositórios, criar diretórios e abrir projetos no VS Code.
        - **Utilizar uma calculadora ou realizar operações matemáticas**.
        - Interagir com **APIs gerais**.
- **Capacidades Aprimoradas de Interação e Fluxo de Trabalho**:    
    - **Comportamentos agentivos**: Os servidores podem solicitar ao modelo de linguagem do cliente para gerar conclusões (**amostragem**), permitindo tarefas dependentes de IA e avaliações complexas de cenários.
    - **Coleta dinâmica de informações**: Os modelos podem solicitar informações específicas aos utilizadores (**elicitação**) para completar tarefas ou confirmar ações.
    - **Fluxos de trabalho estruturados**: Os modelos podem seguir modelos pré-definidos (**prompts**) para guiar interações e alcançar resultados consistentes (ex: o prompt "Planear umas férias").
    - **Capacidades multimodais**: Integrações futuras preveem que os modelos possam compreender e processar **imagens, áudio e vídeo**, resultando em interações mais ricas.
    - **Projetos complexos e de várias etapas**: Os modelos podem orquestrar ações em múltiplos servidores e fontes de dados, combinando várias ferramentas e recursos para atingir objetivos sofisticados (ex: planeamento completo de viagens usando servidores de calendário, clima e viagens).
    - **Interação em linguagem natural com sistemas externos**: Os utilizadores podem interagir com sistemas complexos usando linguagem quotidiana, e o modelo traduz isso em chamadas de ferramentas e acesso a dados.
- **Integração com Sistemas Empresariais**:
    
    - Os modelos podem ser integrados com **ferramentas empresariais internas, sistemas CRM**, ferramentas de gestão de projetos, sistemas de documentação, repositórios de código, serviços Azure e Microsoft AI Foundry. Isto expande a sua utilidade para contextos de negócio específicos.

A natureza modular do MCP significa que **novas capacidades podem ser adicionadas sem alterar as próprias aplicações de IA**, semelhante a adicionar novos acessórios a um computador. Além disso, o agente pode **descobrir automaticamente** quais novas ferramentas estão disponíveis quando um novo servidor é adicionado, sem necessidade de "fiação" extra.