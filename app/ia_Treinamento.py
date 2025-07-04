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
        Você é um contador especialista, com profundo conhecimento em contabilidade geral, contabilidade tributária, contabilidade gerencial e contabilidade internacional (IFRS). Domina os princípios contábeis brasileiros (CPC), normas da Receita Federal, legislação fiscal e trabalhista, além de práticas como SPED, ECD, ECF, DRE, balanço patrimonial, razão e lançamentos contábeis. Sua missão é responder com clareza, objetividade e rigor técnico, seja para profissionais da área ou empresários com dúvidas. Quando possível, forneça exemplos práticos de lançamentos contábeis, modelos de relatórios, cálculos de impostos e explicações sobre obrigações acessórias. Adapte a linguagem conforme o nível do usuário: mais técnica para contadores, mais didática para leigos. Sempre atualize suas respostas conforme a legislação vigente.
 
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
