import DoubleLinkedList
import PilasYColasEnlazadas

def DLLsample(array):
    print('=================================== EJEMPLO DE LISTAS DOBLEMENTE ENLAZADAS ===================================')
    DLList = DoubleLinkedList.DLinkedList()
    print('¿La Lista esta vacia?   R/', DLList.isEmpty())
    for i in array:
        DLList.add(i)
    print('¿La Lista esta vacia?   R/', DLList.isEmpty())
    print('El tamaño de la lista es:', len(DLList))
    print('¿Esta la nota "F" en la lista?  R/', DLList.search('F'))
    print('¿Esta la nota "A+" en la lista?  R/', DLList.search('A+'))
    print('Veamos la lista entera')
    DLList.printList()
    print('Eliminemos la nota "B"')
    print(DLList.remove('B'))
    DLList.printList()
    print('Intento de eliminar otra nota que no debe estar')
    print(DLList.remove('B'))
    print('Asi queda la lista')
    DLList.printList()
    print('Probemos la devolucion')
    print('La cabeza es:',DLList.head().getValue(),"'El siguiente es:',DLList.head().getNext().getValue(),'Y el anterior es:', DLList.head().getPrev" )
    print('================================= FIN EJEMPLO DE LISTAS DOBLEMENTE ENLAZADAS =================================')

def LQueueSample(cinefilos):
    print('========================================= EJEMPLO DE COLAS ENLAZADAS ========================================')
    lqueue = PilasYColasEnlazadas.LinkedQueue()
    for persona in cinefilos:
        lqueue.Enqueue(persona)
    print('Hay',len(lqueue),'Cinefilos')
    print('Llegan en este orden')
    lqueue.printQueue()
    print('Se atiende a',lqueue.getHead().getValue())
    lqueue.dequeue()
    lqueue.printQueue()
    print('Se atiende a',lqueue.getHead().getValue())
    lqueue.dequeue()
    lqueue.printQueue()
    print('El ultimo es',lqueue.getTail().getValue())
    print('Llega un tipo con su novia')
    lqueue.enqueue('El Tipo con novia')
    lqueue.printQueue()
    print('======================================= FIN EJEMPLO DE COLAS ENLAZADAS ======================================')

def LStacksample(procrastinacion):
    print('========================================= EJEMPLO DE PILAS ENLAZADAS ========================================')
    lstack = PilasYColasEnlazadas.LinkedStack()
    for tarea in procrastinacion:
        lstack.Enqueue(tarea)
    print('Tengo',len(lstack),'Tareas')
    print('Me llegaron es este orden')
    lstack.printStack()
    print('Primero hago:',lstack.pop())
    print('Me quedan')
    lstack.pop()
    lstack.printStack()
    print('Ahora hago',lstack.pop())
    print('Me quedan')
    lstack.printStack()
    print('En AYED me dejaron otro trabajo mas para el viernes asi que...')
    lstack.push('La otra de AYED')
    lstack.printStack()
    print('======================================= FIN EJEMPLO DE PILAS ENLAZADAS ======================================')

def main():
    array = ['A','A-','B','F','F','F']
    cinefilos = ['El de la camisa de spiderman', 'Los que vienen en combo a ver la de Marvel','La Familia generica 1','El pobre que viene solo','La familia generica 2']
    procrastinacion = ['la tarea de AYED','El proyecto del grupo de videojuegos','las arenas de ACSO','El proyecto de Bases']
    DLLsample(array)
    LQueueSample(cinefilos)
    LStacksample(procrastinacion)
main()
