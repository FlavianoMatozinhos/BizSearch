import asyncio
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from duckduckgo_search import AsyncDDGS
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import GPT4All
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

cache = {}

async def aget_results(query):
    # Realiza a busca assíncrona usando DuckDuckGo
    results = await AsyncDDGS(proxy=None).atext(query, max_results=1)  # Reduzido para 3 resultados
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

def run_search(query):
    try:
        if query in cache:
            summary = cache[query]
            app.after(0, update_results, [], summary)  # Passa lista vazia para search_results
            return

        # Configura o modelo GPT4All usando o caminho do .env
        model_path = os.getenv("GPT4ALL_MODEL_PATH")
        llm = GPT4All(model=model_path)

        # Realiza a pesquisa
        search_results = asyncio.run(aget_results(query))

        # Gera um resumo dos resultados encontrados
        summary = create_summary(llm, search_results)
        cache[query] = summary  # Armazena no cache

        # Atualiza a área de texto com os resultados na thread principal
        app.after(0, update_results, search_results, summary)
    except Exception as e:
        app.after(0, lambda: messagebox.showerror("Erro", f"Ocorreu um erro ao realizar a pesquisa: {e}"))
    finally:
        # Reabilita o botão após a pesquisa
        app.after(0, lambda: search_button.config(state=tk.NORMAL))

def update_results(search_results, summary):
    results_text.delete(1.0, tk.END)  # Limpa a área de resultados
    results_text.insert(tk.END, "Resumo das informações coletadas:\n")
    results_text.insert(tk.END, summary)

def search_and_display():
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Aviso", "Por favor, insira um termo para pesquisa.")
        return
    
    # Desabilita o botão enquanto a pesquisa é feita
    search_button.config(state=tk.DISABLED)
    
    # Inicia a pesquisa em uma nova thread
    threading.Thread(target=run_search, args=(query,), daemon=True).start()

# Configurações da interface gráfica com tkinter
app = tk.Tk()
app.title("Agente de Pesquisa")
app.geometry("600x400")

# Campo de entrada para a pesquisa
search_label = tk.Label(app, text="Digite o nome da empresa ou tópico para pesquisa:")
search_label.pack(pady=5)
search_entry = tk.Entry(app, width=50)
search_entry.pack(pady=5)

# Botão para realizar a pesquisa
search_button = tk.Button(app, text="Pesquisar", command=search_and_display)
search_button.pack(pady=5)

# Área de texto para mostrar os resultados
results_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=15)
results_text.pack(padx=10, pady=10)

# Inicia o loop da interface gráfica
app.mainloop()
