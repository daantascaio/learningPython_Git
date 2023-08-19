# Mantendo estados dentro da classe

class Camera:

    def __init__(self, name, filmando=False):

        self.name = name
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.name} já está filmando...') #
            return
        
        print(f'{self.name} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.name} não está filmando...') #
            return
    
        print(f'{self.name} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.name} não pode fotografar filmando!') #
            return
        
        print(f'{self.name} está fotografando!')
        

c1 = Camera('Canon')
c2 = Camera('Sony')

# c1.filmar()
# c1.filmar() #
# c1.fotografar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
# c1.fotografar()
# c1.fotografar()
# c1.parar_filmar()
# c1.filmar()
# c1.filmar() #
# c1.parar_filmar()
# c1.parar_filmar()
# c1.fotografar()
# c1.fotografar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
c2.filmar()
c1.filmar()
c1.fotografar()
c2.fotografar()
c1.parar_filmar()
c1.fotografar()
c1.fotografar()
c1.fotografar()
c1.fotografar()
c2.parar_filmar()
c2.parar_filmar()
c2.fotografar()
c2.fotografar()
c2.fotografar()
# print(c1.filmando)
# print(c2.filmando)

