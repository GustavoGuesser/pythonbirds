class Pessoa:
    def __init__(self ,*filhos, nome=None, idade=35) -> object:
        self.idade = idade
        self.nome = nome
        self.filhos = list[filhos]


    def comprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    gustavo = Pessoa(nome='Luciano')
    luciano = Pessoa(gustavo, nome='Luciano')

    print(Pessoa.comprimentar(luciano))
    print(id(luciano))
    print(luciano.comprimentar())


    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
