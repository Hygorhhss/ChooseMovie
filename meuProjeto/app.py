from flask import Flask, render_template
import random

app = Flask(__name__)

def escolher_filme(lista_filmes):
    """Função para escolher um filme aleatório da lista."""
    filme_escolhido = random.choice(lista_filmes)
    return filme_escolhido

# Lista de filmes
lista_de_filmes = [
    "O Poderoso Chefão",
    "Matrix",
    "Titanic",
    "Cidade de Deus",
    "Pulp Fiction",
    "Interestelar",
    "O Senhor dos Anéis: A Sociedade do Anel",
    "Vingadores: Ultimato",
    "A Origem",
    "Forrest Gump"
]

# Escolhendo um filme aleatório
filme_aleatorio = escolher_filme(lista_de_filmes)

@app.route('/')
def index():
    return render_template('index.html', filme_aleatorio=filme_aleatorio)

if __name__ == '__main__':
    app.run(debug=True)
