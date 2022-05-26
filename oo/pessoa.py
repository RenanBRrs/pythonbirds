class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

    def cumprimentar(self):
        return 'Ola mundo'

if __name__ == '__main__':
    p = Pessoa('Renan')
    print(p.cumprimentar() + f' e Oi {p.nome}')