from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dicionário onde as chaves são as categorias e os valores são listas de filmes correspondentes
categorias_filmes = {
    "acao": ["O Profissional (Léon: The Professional) (1994)", "Matrix", "Mulan (1998)", "Pulp Fiction", "Vingadores: Ultimato", "Velozes e Furiosos (The Fast and the Furious) (2001)", "Duro de Matar (Die Hard) (1988)", "Jurassic Park (1993)", "Caça-Fantasmas (Ghostbusters) (1984)"],
    "romance": ["A Casa do Lago (2006)", "Meia-Noite em Paris (2011)", "Um Homem de Sorte (2012)", "Como Eu Era Antes de Você (2016)", "Amor a Toda Prova (2011)", "La La Land: Cantando Estações (La La Land) (2016)", "Brilho Eterno de uma Mente sem Lembranças (Eternal Sunshine of the Spotless Mind) (2004)", "Um Lugar Chamado Notting Hill (Notting Hill) (1999)", ""],
    "drama": ["O Lado Bom da Vida (2012)", "O Resgate do Soldado Ryan (1998)", "À Procura da Felicidade (2006)", "O Náufrago (2000)"],
    "ficcao": ["Interestelar", "A Origem", "A Viagem de Chihiro (2001)", "A Chegada (2016)", "O Labirinto do Fauno (2006)", "Duna", "De Volta para o Futuro (1985)", "Blade Runner 2049 (2017)", "Eu, Robô (I, Robot) (2004)", "O Gigante de Ferro (The Iron Giant) (1999)", "Os 12 Macacos (12 Monkeys) (1995)"],
    "fantasia": ["O Senhor dos Anéis: A Sociedade do Anel", "Harry Potter e a Pedra Filosofal (Harry Potter and the Philosopher's Stone) (2001)", "A Fantástica Fábrica de Chocolate (Charlie and the Chocolate Factory) (2005)", "A História Sem Fim (The NeverEnding Story) (1984)", "Os Fantasmas se Divertem (Beetlejuice) (1988)", "Gigantes de Aço (Real Steel) (2011)"],
    "comedia": ["Forrest Gump", "O Âncora: A Lenda de Ron Burgundy (Anchorman: The Legend of Ron Burgundy) - 2004", "As Branquelas (White Chicks) (2004)", "A Vida Secreta de Walter Mitty (The Secret Life of Walter Mitty) (2013)", "MIB: Homens de Preto (Men in Black) (1997)", ""],
    "animacao": ["Shrek (2001)", "Procurando Nemo (2003)", "Monstros S.A. (2001)", "Toy Story (1995)", "Shrek (2001)", "O Estranho Mundo de Jack (1993)", "Aladdin (1992)", "Homem-Aranha no Aranhaverso (Spider-Man: Into the Spider-Verse) (2018)"],
}

@app.route('/')
def index():
    filme_aleatorio = escolher_filme_aleatorio()
    return render_template('index.html', filme_aleatorio=filme_aleatorio)

@app.route('/escolher_filme', methods=['POST'])
def escolher_filme():
    categoria = request.form['categoria']
    filmes_disponiveis = categorias_filmes.get(categoria.lower())
    if not filmes_disponiveis:
        filme_aleatorio = "Nenhum filme disponível nesta categoria"
    else:
        filme_aleatorio = random.choice(filmes_disponiveis)
    return render_template('index.html', filme_aleatorio=filme_aleatorio)

def escolher_filme_aleatorio():
    todas_as_categorias = list(categorias_filmes.keys())
    todas_os_filmes = [filme for filmes in categorias_filmes.values() for filme in filmes]
    return random.choice(todas_os_filmes)

if __name__ == '__main__':
    app.run(debug=True)
