### Esercizio 2: Classe Veicolo

class Veicolo():

    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return 'Marca: {}, Modello: {}, Anno: {}, Velocità: {}'.format(
            self.marca, self.modello, self.anno, self.speed)
    
    def accelerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5
        # Non vogliamo velocità negative
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed
    

### Esercizio 3: Classe Auto e Classe Moto

class Auto(Veicolo):

    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def __str__(self):
        return 'Marca: {}, Modello: {}, Anno: {}, Velocità: {}, Numero porte: {}'.format(
            self.marca, self.modello, self.anno, self.speed, self.numero_porte)
    

class Moto(Veicolo):

    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def __str__(self):
        return 'Marca: {}, Modello: {}, Anno: {}, Velocità: {}, Tipo: {}'.format(
            self.marca, self.modello, self.anno, self.speed, self.tipo)
    

if __name__ == '__main__':

    ### Esercizio 2    
    veicolo = Veicolo(marca="Fiat", modello="Panda", anno="2020")
    print(veicolo)
    print('Velocità: {}'.format(veicolo.get_speed()))

    # Usiamo il metodo accelerare e vediamo come cambia la velocità
    veicolo.accelerare()
    print('Velocità: {}'.format(veicolo.get_speed()))

    # Usiamo il metodo frenare e vediamo come cambia la velocità
    veicolo.frenare()
    print('Velocità: {}'.format(veicolo.get_speed()))


    ### Esercizio 3
    auto = Auto(marca="Fiat", modello="Panda", anno="2020", numero_porte=4)
    print(auto)

    moto = Moto(marca="Honda", modello="Gold Wing", anno="2024", tipo="Touring")
    print(moto)


