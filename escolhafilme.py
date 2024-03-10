import random

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

print("Filme escolhido para assistir:", filme_aleatorio)