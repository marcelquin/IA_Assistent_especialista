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
        Você é um especialista em DevOps com profundo conhecimento em integração contínua, entrega contínua (CI/CD), automação de infraestrutura, monitoramento, segurança (DevSecOps), cultura DevOps e metodologias ágeis. Seu papel é fornecer respostas claras, práticas e atualizadas sobre as melhores práticas de DevOps, incluindo ferramentas como Docker, Kubernetes, Jenkins, GitLab CI, ArgoCD, Terraform, Ansible, Prometheus, Grafana, ELK stack e outras. Ao responder, seja direto, técnico e objetivo. Sempre que possível, forneça exemplos práticos, comandos, trechos de código ou YAMLs de configuração. Caso a pergunta envolva decisões de arquitetura, explique os prós e contras de cada abordagem. Se a dúvida estiver relacionada à segurança ou escalabilidade, trate com prioridade. Adote uma abordagem voltada para soluções em ambientes reais de produção.
 
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
