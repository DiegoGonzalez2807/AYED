import Lineales

def doublelinkedlist_proof(list_1):
    print('=======================INICIO EJEMPLO LISTAS DOBLEMENTE ENLAZADAS==============')
    print('')
    linked_list = Lineales.DoubleLinked()
    print('la fila esta vacia? (Prueba donde la lista es vacia)', linked_list.empty())
    print('')
    print('PRUEBA ADICION DE ELEMENTOS A LA FILA DEL BANCO')
    for value in list_1:
        linked_list.insert(value)
    print('Con la adicion de valores la lista esta vacia?', linked_list.empty())
    print('')
    print('PRUEBA TAMAÑO DE LISTA')
    print('El tamaño de la lista es', len(linked_list))
    print('')
    print('PRUEBA BUSQUEDA DE VALORES')
    print('Esta el numero 216 en la fila del banco?', linked_list.search(216))
    print('Esta el numero 2519 en la fila del banco?', linked_list.search(2519))
    print('')
    print('PRUEBA DE PRINT')
    print('vista de la lista del banco completa',linked_list.printList())
    print('')
    print('PRUEBA DE ELIMINACION')
    print('Eliminar al numero 5 de la fila del banco', linked_list.remove(5))
    print('Nueva fila del banco sin el numero 5', linked_list.printList())
    print('')
    print('======================FIN EJEMPLO LISTAS DOBLEMENTE ENLAZADAS==================')


def pila_proof(list_2):
    print('=======================INICIO EJEMPLO PILAS ENLAZADAS==============')
    linked_pila = Lineales.Pila()
    print('PRUEBA DE LONGITUD DE LA PILA DE LIBROS AL INICIO')
    print('La pila de libros esta vacia ?', linked_pila.empty())
    print('')
    print('PRUEBA DE ADICION DE ELEMENTOS A LA PILA')
    for value in list_2:
        linked_pila.Push(value)
    print('Ahora con la adicion sigue vacia la pila de libros?', linked_pila.empty())
    print('')
    print('PRUEBA LONGITUD DE LA PILA')
    print('La cantidad de libros que tengo en la pila es de ', len(linked_pila))
    print('')
    print('PRUEBA INGRESO A LA FILA')
    print('Se coloca un libro en la pila', linked_pila.Push('Ecuaciones Diferenciales'))

    print('')
    print('PRUEBA PRINT DE LA PILA')
    print('La pila con el ingreso del nuevo libro queda de la siguiente manera')
    linked_pila.printList()
    print('')
    print('PRUEBA ELIMINACION DE PILA')
    print('Una persona se lleva el libro que acaban de poner, el cual es ', linked_pila.Pop())
    print('La pila sin ese libro ahora queda:')
    linked_pila.printList()
    print('')
    print('======================FIN EJEMPLO PILAS ENLAZADAS==================')


def cola_proof(list_3):
    print('=======================INICIO EJEMPLO COLAS ENLAZADAS==============')
    linked_cola = Lineales.Cola()
    print('PRUEBA DE LONGITUD DE LA COLA AL INICIO')
    print('La cola del cine esta vacia ?', linked_cola.empty())
    print('')
    print('PRUEBA DE ADICION DE ELEMENTOS A LA COLA')
    for value in list_3:
        linked_cola.enqueue(value)
    print('Ahora con la adicion sigue vacia la cola del cine?', linked_cola.empty())
    print('')
    print('PRUEBA LONGITUD DE LA COLA')
    print('La cantidad de personas que hay en la cola del cine es de ', len(linked_cola))
    print('')
    print('PRUEBA INGRESO A LA COLA')
    print('Ingresa otra persona a la cola del cine', linked_cola.enqueue('Alejandro'))

    print('')
    print('PRUEBA PRINT DE LA COLA')
    print('La cola del cine con la nueva persona queda de la siguiente manera')
    linked_cola.printList()
    print('')
    print('PRUEBA ELIMINACION DE COLA')
    print('La primera persona de la cola se acaba de ir, la cual era ', linked_cola.dequeue())
    print('La cola del cine sin esa persona queda:')
    linked_cola.printList()
    print('')
    print('======================FIN EJEMPLO COLAS ENLAZADAS==================')




def main():
    #Ejemplo 1 fila de banco con listas doblemente enlazadas
    fila_banco = [1,2,3,4,5,7,9,81,216,217,218,2518,2520]
    doublelinkedlist_proof(fila_banco)
    #Ejemplo 2 pila de libros con pilas enlazadas
    pila_libros = ['Precalculo', 'Calculo Diferencial e Integral', 'Algebra lineal', 'Calculo vectorial', 'Mecanica de fluidos']
    pila_proof(pila_libros)
    #Ejemplo 3 cola del cinema con colas enlazadas
    cola_cine = ['Diego', 'Juan', 'Carolina', 'Vanessa', 'Maria', 'Jose', 'Cristian']
    cola_proof(cola_cine)
main()






