#Semana 3 AYED
def iterative_sort(lista):
    for j in range(1,len(lista)):
        key = lista[j]
        i = j 
        while i > 0 and lista[i-1] > key:
            lista[i] = lista[i-1]
            i = i - 1
        lista[i] = key
def search_number(lista):
    menor = lista[0]
    cont = 0
    while cont != len(lista)-1:
        if lista[cont] < menor:
            menor = lista[cont]
        cont += 1 
    return menor
def faltante(lista):
    answer = 0
    cont = 0
    while cont != len(lista)-1:
        if abs(lista[cont+1] - lista[cont]) == 2:
            answer = lista[cont] + 1
            print(answer)
            break
        else:
            cont += 1
            return faltante(lista[cont:])
    return answer
def divide_conquer(number,total):
    bajo = 0
    alto = 99
    numero = 50
    proof = number ** numero
    while proof != total:
        if proof > total:    #Creo que divide and conquer es con listas, con lo cual se tendria que revisar si se puede hacer este algoritmo de esa manera
            alto = numero
            numero = (bajo + alto)//2
        elif proof < total:
            bajo = numero
            numero = (bajo+alto)//2
        proof = number ** numero
    return numero
print(search_number([2,1,23,4,6,8,4,2,12,3,5,7,8,7,5,3,5,7,9,95,4,6]))
faltante([1,2,3,4,5,6,8,9])
print(divide_conquer(5,390625))
