# class Pessoa():
#     def __init__(self, nome=None, idade=35):
#         self.nome = nome
#         self.idade = idade
#
#
#     def cumprimentar(self):
#         return f'Olá {id(self)}'
#
#
# if __name__ == '__main__':
#     p = Pessoa('Luciano')
#     print(Pessoa.cumprimentar(p))
#     print(id(p))
#     print(p.cumprimentar())
#     print(p.nome)
#     p.nome = 'charles'
#     print(p.nome)
#     print(p.idade)


# ATRIBUTOS COMPLEXO

class Pessoa():
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)





