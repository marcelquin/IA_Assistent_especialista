import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key="AIzaSyDjBuKx2GycGmJHvq9bZV1sR-lcVspP12A")



def fazer_busca(pergunta):
    """Realiza uma busca no texto usando o Gemini"""
    try:
        modelo = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Você é um especialista em contabilidade, voltado para empresas, atuando na analise de informações, buscando a melhor maneira de resolver o problema e ainda retornando lucro ao cliente.
 
        com base nisso responda a seguinte pergunta : {pergunta}.        
        """
        
        resposta = modelo.generate_content(prompt)
        return resposta.text
    
    except Exception as e:
        return f"Erro ao processar a busca: {str(e)}"

def main():  
    conteudo = ler_arquivo()
    
    while True:
            pergunta = input("\nDigite sua pergunta sobre o texto (ou 'sair' para encerrar): ")
            
            if pergunta.lower() == 'sair':
                break
                
            resposta = fazer_busca(conteudo, pergunta)
            print("\nResposta:", resposta)
            print("\n" + "-"*50)

if __name__ == "__main__":
    main()
