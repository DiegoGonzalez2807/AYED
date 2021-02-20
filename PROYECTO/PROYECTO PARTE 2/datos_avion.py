from sys import stdin
from random import randint
from random import choice
RANDOM_FULL_NAMES = ['Barrie Alan',
                     'Nariko Velten',
                     'Lonnie Crosthwaite',
                     'Aleksandr McCaughran',
                     'Ingemar Kolin',
                     'Hilario Ziems',
                     'Ximenes Singers',
                     'Ellie MacTavish',
                     'Garreth Wonfor',
                     'Floris Marquese',
                     'Jefferson Escala',
                     'Elisa Yeude',
                     'Trescha Tibb',
                     'Jany Jewess',
                     'Lanni Lardnar',
                     'Jamima Sherwell',
                     'Kala Sheron',
                     'Julee O''Duane',
                     'Warden Clamp',
                     'Allie Franzettoini',
                     'Burk Guillond'
                     ]
class HashTable:
    def __init__(self, size):
        self.elements = [ [] for x in range(size) ]
        self.keys = set()

    def search(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key :
                return e[1]
        return None

    def assign(self, index, element):
        self.elements[index].append(element)

    def getElements(self):
        return self.elements

    def getKeys(self):
        return self.keys

    def printHashTable(self):
        print('========== Hash Table Composition ================')
        print('Elements')
        for index in range(len(self.elements)):
            print(index, ':', self.elements[index])
        print('Keys', self.keys)

    def insert(self, key, element):
        index = self.hash(key)
        self.position(index, key, element)
        self.keys.add(key)

    def hash(self, key):
        return hash(key) % len(self.elements)

    def del_passenger(self,key,name,identificator):
        self.elements[key] = []
        self.assign(key, (name, identificator))                     #FUNCION BIEN

    def confirmed_transaction(self,key,name,identificator):
        print('Confirmando transacción.....')
        print('...')
        print('...')
        print('al pasajero', name, 'identificado como', identificator, 'se le confirma el puesto', key + 1)                #FUNCION BIEN
        self.assign(key, (name, identificator))
        print(self.elements)
        print()
        print()
    def recursivity_passenger(self,identificator,name):
        return self.position(self.hash(identificator + randint(10000, 99999)), identificator, name)         #FUNCION BIEN




    def position(self, key, identificator, name):
        print('al pasajero', name, 'identificado como', identificator, 'se le quiere dar el puesto', key+1)

        if self.elements[key] != []:     #El puesto del avion ya está lleno


            print('El asiento está lleno por la persona',self.elements[key][0][0])

            if self.stop():
                    print('Todos los asientos están llenos')
            else:
                new_key = self.checking_passengers(key)
                if key == new_key:
                    print('Se le asignara otro puesto a', name)
                    print()
                    print()
                    self.recursivity_passenger(identificator,name)

                else:
                    print('Se le asigna el puesto',new_key+1,'a', name)
                    self.del_passenger(new_key,identificator,name)

        elif self.elements[key] == []:               #Si de una vez ese puesto está vacio
            self.confirmed_transaction(key,name,identificator)


    def stop(self):
        ret1 = True
        for i in range(len(self.elements)):
            if self.elements[i] == []:
                ret1 = False
        return ret1

    def checking_passengers(self,key):
        print()
        print()
        count = 0
        print('Se le hará un checking a los pasajeros, para revisar si hay alguno que no pueda viajar')
        for value in self.elements:
            if value != []:
                print('El pasajero', value[0][0], 'ya confirmó su estadia en este vuelo? SI NO')
                answer = stdin.readline().strip()
                if answer.capitalize() == 'Si':
                    count += 1
                elif answer.capitalize() == 'No':
                    key = self.elements.index(value)
        if count == len(self.elements):
            print('Todos los pasajeros confirmaron su estadia, lastimosamente no se puede recibir más pasajeros. Hasta otro viaje')
        return key



def main():
    print('Es usted administrador de la plataforma? Si No')
    answer = stdin.readline().strip()
    if answer.capitalize() == 'Si':
        print('Cuantos pasajeros quieren tomar esta ruta de destino?')
        answer2 = int(stdin.readline().strip())
        passengers  = [(randint(100000000,999999999), choice(RANDOM_FULL_NAMES))for x in range(answer2)]
        data = HashTable(5)
        for value in passengers:
            data.insert(value[0],value[1])
    elif answer.capitalize() == 'No':
        print('No tiene permiso para estar aqui')

main()

