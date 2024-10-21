import asyncio
from duckduckgo_search import AsyncDDGS
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import GPT4All
from langchain.agents import Tool, AgentExecutor, ZeroShotAgent

async def aget_results(query):
    # Realiza a busca assíncrona usando DuckDuckGo
    results = await AsyncDDGS(proxy=None).atext(query, max_results=5)
    return results

def create_summary(llm, search_results):
    # Configura um template para resumir as informações encontradas
    prompt_template = PromptTemplate(
        input_variables=["info"],
        template="Faça um resumo dos seguintes dados sobre a empresa: {info}"
    )
    
    # Cria uma cadeia de LLM com o modelo e o template de prompt
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    # Formata os dados dos resultados de pesquisa para o resumo
    formatted_info = "\n".join([f"{result['title']}: {result['body']}" for result in search_results])
    summary = chain.run(info=formatted_info)
    
    return summary

async def main():
    # Solicita ao usuário que digite o nome da empresa ou o tópico a ser pesquisado
    user_input = input("Digite o nome da empresa ou o tópico que deseja pesquisar: ")

    # Configura o modelo GPT4All
    llm = GPT4All(model="C:/Users/Flaviano/AppData/Local/nomic.ai/GPT4All/Meta-Llama-3-8B-Instruct.Q4_0.gguf")

    # Realiza a pesquisa usando DuckDuckGo
    search_results = await aget_results(user_input)
    
    # Exibe os resultados brutos da pesquisa
    print("\nResultados da pesquisa:")
    for i, result in enumerate(search_results):
        print(f"{i+1}. {result['title']} - {result['href']}")

    # Gera um resumo dos resultados encontrados
    summary = create_summary(llm, search_results)
    
    # Exibe o resumo gerado pelo GPT4All
    print("\nResumo das informações coletadas:")
    print(summary)

if __name__ == "__main__":
    asyncio.run(main())
