# NOTE: importação de biblioteca
import random

# NOTE: cria a classe
class Pessoa:
    # os atributos são sempre definidos dentro do método construtor
    # método construtor
    def __init__(self, nome, humor):
        self.nome = nome
        self.humor = humor

    # método de ação
    def cumprimentar(self):
        if self.humor:
            print(f'Oi, meu nome é {self.nome}. E o seu?')
        else:
            print(f'Qual foi?? O que você quer?')
    
    class Pessoa:
        def responder(self,nome,humor):
            if humor:
                print(f'Salve {nome}, sou o {self.nome}. Satisfação!')
                self.humor = True
            else:
             print(f'Vai se lascar, infeliz.')
             self.humor = False
            return self.humor
# NOTE: programa principal
if __name__ == '__main__':
    humores = (True, False)
    nome1 = input('Informe o nome do 1º usuário: ')
    nome2 = input('Informe o nome do 2º usuário: ')

    # instancia dos objetos
    usuario1 = Pessoa(nome1, humores[random.randint(0,1)])
    usuario2 = Pessoa(nome2, humores[random.randint(0,1)])

    usuario1.cumprimentar()
    usuario1.humor = usuario2.responder(usuario1.nome, usuario2.humor)

    if usuario1.humor:
        print(f'{usuario1.nome} ficou feliz.')
    else:
        print(f'{usuario1.nome} ficou triste.')
        