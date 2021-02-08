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

# class Pessoa():
#     def __init__(self, *filhos, nome=None, idade=35):
#         self.nome = nome
#         self.idade = idade
#         self.filhos = list(filhos)
#
#
#     def cumprimentar(self):
#         return f'Olá {id(self)}'
#
#
# if __name__ == '__main__':
#     renzo = Pessoa(nome='Renzo')
#     luciano = Pessoa(renzo, nome='Luciano')
#     print(Pessoa.cumprimentar(luciano))
#     print(id(luciano))
#     print(luciano.cumprimentar())
#     print(luciano.nome)
#     print(luciano.idade)
#     for filho in luciano.filhos:
#         print(filho.nome)


# ATRIBUTO DINAMICO

# class Pessoa():
#     def __init__(self, *filhos, nome=None, idade=35):
#         self.nome = nome
#         self.idade = idade
#         self.filhos = list(filhos)
#
#
#     def cumprimentar(self):
#         return f'Olá {id(self)}'
#
#
# if __name__ == '__main__':
#     renzo = Pessoa(nome='Renzo')
#     luciano = Pessoa(renzo, nome='Luciano')
#     print(Pessoa.cumprimentar(luciano))
#     print(id(luciano))
#     print(luciano.cumprimentar())
#     print(luciano.nome)
#     print(luciano.idade)
#     for filho in luciano.filhos:
#         print(filho.nome)
#     luciano.sobrenome = 'Ramanlho' # Criação do atributo dinâmico fazendo a atribuição
#     del luciano.filhos             # Remoção do atributo
#     print(luciano.__dict__)        # Os atributos de instancia ficam presentes no __dict__
#     print(renzo.__dict__)

#  ATRIBUTO DE CLASSE

# class Pessoa():
#     olhos = 2  # criado atributo de classe olhos
#
#     def __init__(self, *filhos, nome=None, idade=35):
#         self.nome = nome
#         self.idade = idade
#         self.filhos = list(filhos)
#
#     def cumprimentar(self):
#         return f'Olá {id(self)}'
#
#
# if __name__ == '__main__':
#     renzo = Pessoa(nome='Renzo')
#     luciano = Pessoa(renzo, nome='Luciano')
#     print(Pessoa.cumprimentar(luciano))
#     print(id(luciano))
#     print(luciano.cumprimentar())
#     print(luciano.nome)
#     print(luciano.idade)
#     for filho in luciano.filhos:
#         print(filho.nome)
#     luciano.sobrenome = 'Ramanlho'
#     del luciano.filhos
#     luciano.olhos = 1
#     del luciano.olhos
#     print(luciano.__dict__)
#     print(renzo.__dict__)
#     Pessoa.olhos = 3
#     print(Pessoa.olhos)
#     print(luciano.olhos)
#     print(renzo.olhos)
#     print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))

# MÉTODO DE CLASSE

class Pessoa():
    olhos = 2  # criado atributo de classe olhos

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'



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
    luciano.sobrenome = 'Ramanlho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.nome_e_atributo_de_classe(), luciano.metodo_estatico())



