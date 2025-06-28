import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Configura a API do Gemini
genai.configure(api_key="AIzaSyDjBuKx2GycGmJHvq9bZV1sR-lcVspP12A")

def ler_arquivo():
    try:
        with open('Arquivo/arquivo.csv', 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "Arquivo não encontrado."
    except Exception as e:
        return f"Erro ao ler arquivo: {str(e)}"

def fazer_busca(pergunta):

    try:
        modelo = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Você é um especialista em contabilidade, voltado para empresas, atuando na analise de informações, buscando a melhor maneira de resolver o problema e ainda retornando lucro ao cliente.
        com base nisso responda a seguinte pergunta : {pergunta}.        
        """
        
        # Gera a resposta
        resposta = modelo.generate_content(prompt)
        return resposta.text
    
    except Exception as e:
        return f"Erro ao processar a busca: {str(e)}"

def main():
    # Lê o conteúdo do arquivo
    conteudo = ler_arquivo()
    
    while True:
            # Solicita a pergunta ao usuário
            pergunta = input("\nDigite sua pergunta sobre o texto (ou 'sair' para encerrar): ")
            
            if pergunta.lower() == 'sair':
                break
                
            # Realiza a busca
            resposta = fazer_busca(conteudo, pergunta)
            print("\nResposta:", resposta)
            print("\n" + "-"*50)

if __name__ == "__main__":
    main()
