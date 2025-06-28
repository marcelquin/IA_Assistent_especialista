from flask import Flask, request, jsonify, render_template
from ia_Treinamento import fazer_busca

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota da API
@app.route('/api/busca', methods=['POST'])
def busca_api():
    data = request.get_json()
    pergunta = data.get('pergunta')
    resultado = fazer_busca(pergunta)
    return jsonify({'resposta': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)