
# BizSearch - Sistema de Pesquisa de Informações de Empresas

BizSearch é uma ferramenta para realizar pesquisas automatizadas de informações sobre empresas e gerar relatórios úteis para preparar usuários para reuniões. O sistema utiliza tecnologias como GPT4All e LangChain para gerar prompts inteligentes e DuckDuckGo para fazer buscas na web.

## Funcionalidades
- Pesquisa de informações sobre empresas com base em um prompt fornecido pelo usuário.
- Geração automática de relatórios de pesquisa para uso em reuniões.
- Interface em linha de comando (CLI) para entrada de dados e visualização de resultados.

## Tecnologias Utilizadas
- **GPT4All**: Modelo de linguagem local utilizado para gerar prompts e interpretar os resultados da pesquisa.
- **LangChain**: Framework para criação de cadeias de LLMs (Large Language Models), usado para conectar o modelo GPT4All à lógica de geração de prompts.
- **DuckDuckGo Search**: Ferramenta de busca na web usada para obter informações relevantes sem rastreamento.
- **Python**: Linguagem principal usada para desenvolvimento do sistema.

## Pré-requisitos
Antes de instalar e rodar o projeto, certifique-se de ter os seguintes itens instalados:

- **Python 3.8 ou superior**: [Instalação do Python](https://www.python.org/downloads/)
- **GPT4All**: Baixe o modelo e coloque-o no diretório especificado. [Instruções para download](https://github.com/nomic-ai/gpt4all)
- **Git**: Para versionamento e clonagem do repositório. [Instalação do Git](https://git-scm.com/downloads)

## Instalação
1. **Clone o repositório**

   ```bash
   git clone https://github.com/usuario/bizsearch.git
   cd bizsearch
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

   Certifique-se de que o arquivo `requirements.txt` contenha as seguintes dependências:

   ```plaintext
   langchain
   gpt4all
   duckduckgo-search
   asyncio
   ```

4. **Baixe o modelo GPT4All**

   Coloque o arquivo de modelo `.gguf` do GPT4All no caminho especificado no código (por exemplo, `C:/Users/Flaviano/AppData/Local/nomic.ai/GPT4All/Meta-Llama-3-8B-Instruct.Q4_0.gguf`). Certifique-se de atualizar o caminho no código se ele estiver diferente.

## Como Executar o Projeto
1. **Execute o arquivo principal**

   ```bash
   python main.py
   ```

2. **Digite o que deseja pesquisar quando solicitado**

   O sistema irá gerar um prompt baseado na entrada do usuário e realizará uma pesquisa na web para encontrar informações relevantes sobre a empresa ou assunto especificado.

### Resultados
Os resultados da pesquisa serão exibidos no terminal, mostrando os títulos e links das páginas encontradas.

## Estrutura do Código
- `main.py`: Arquivo principal contendo a lógica para entrada do usuário, geração de prompts e execução de buscas.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Arquivo com instruções para instalação e uso do projeto.

## Contribuição
Contribuições são bem-vindas! Para contribuir, siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma nova branch para suas mudanças: `git checkout -b minha-nova-feature`
3. Faça commit das suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`
4. Faça push para a branch: `git push origin minha-nova-feature`
5. Envie um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
