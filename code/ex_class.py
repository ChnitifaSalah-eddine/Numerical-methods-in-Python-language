class MaClasse:
    def __init__(self,nom='',prenom=''):
        self.nom=nom
        self.prenom=prenom
    def say_hello(self):
        print('Hello {}!'.format(self.prenom))

wc=MaClasse('Churchill','Winston')
print(wc)
print(wc.nom)
wc.say_hello()
MaClasse().say_hello()