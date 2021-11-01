class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome


if __name__ == '__main__':
    p = Pessoa(nome='Joao')
    p.idade = 27
    print(p.nome, p.idade)
