def min_number(list_1):
    print(list_1)
    min_num = list_1[0]
    for i in range(len(list_1)):
        if list_1[i] < min_num:
            min_num = list_1[i]
    return min_num
#-----------------------------------------------------------------------
def faltante(list_1):
    for i in range(1,len(list_1)):
        if list_1[i] - list_1[i-1] == 2:
            return list_1[i-1] + 1
#------------------------------------------------------------------------
def exponent(base,number_expected,list_1):   #Tomando en cuenta que la list_1 siempre va a estar expresada
                                             # de la manera   memory = [number for number in range(100)]
                                             #pues se toma todos los posibles exponentes de 0 a 99, sin embargo esa
                                             #debe ser implementada en el main en caso de que se quiera meter a un programa
    middle = list_1[len(list_1)//2]
    proof_1 = base ** middle
    if proof_1 == number_expected:
        return middle
    elif proof_1 > number_expected:
        return exponent(base,number_expected,list_1[:len(list_1)//2])
    else:
        return  exponent(base,number_expected,list_1[len(list_1)//2:])

#--------------------------------------------------------------
def mergesort(word):
    lista = list(word)
    print(lista)
    if len(lista) <= 1:
        return lista
    else:
        mid = len(lista) //2
        print(mid)
        izq  = mergesort(lista[:mid])
        print(izq)
        der = mergesort(lista[mid:])
        print(der)
        lista = merge(izq,der)
        print(lista)
        return ''.join(lista)
def merge(izq,der):
    lena = len(izq)
    lenb = len(der)
    nuevo = []
    i,j = 0,0
    while i < lena and j < lenb:
        if izq[i] <= der[j]:
            nuevo += [izq[i]]
            i += 1
        else:
            nuevo += [der[j]]
            j += 1
    while i < lena:
        nuevo += [izq[i]]
        i += 1
    while j < lenb:
        nuevo += [der[j]]
        j += 1
    return nuevo
#----------------------------------------------------------------
def binary(number):
    if number // 2 == 1:
        if number % 2 == 0:
            return 1
        else:
            return 2
    return number % 2 + binary(number//2)

def Memory(number,Mem_1):
    Mem_1[number] = binary(number)

def total_sum(X):
    Mem_1={1:1,2:1}
    number = 0
    count = 1
    while number < X:
        if count not in list[Mem_1.keys()]:
            Memory(count,Mem_1)
        number += Mem_1[count]

        count += 1

print(mergesort('ALGORITMO'))