from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Lista de todos os filmes e suas categorias
filmes = {
    "O Poderoso Chefão": "acao",
    "Matrix": "acao",
    "Titanic": "romance",
    "Cidade de Deus": "acao",
    "Pulp Fiction": "acao",
    "Interestelar": "ficcao",
    "O Senhor dos Anéis: A Sociedade do Anel": "fantasia",
    "Vingadores: Ultimato": "acao",
    "A Origem": "ficcao",
    "Forrest Gump": "drama"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questionario')
def questionario():
    return render_template('questionario.html')

@app.route('/escolher_filme', methods=['POST'])
def escolher_filme():
    categoria = request.form['categoria']
    if categoria == 'todos':
        filmes_disponiveis = list(filmes.keys())
    else:
        filmes_disponiveis = [filme for filme, cat in filmes.items() if cat == categoria]

    filme_aleatorio = random.choice(filmes_disponiveis)
    return render_template('index.html', filme_aleatorio=filme_aleatorio)

if __name__ == '__main__':
    app.run(debug=True)
