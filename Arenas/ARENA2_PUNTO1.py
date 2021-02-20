from sys import stdin
def memory_Recur(number,memory):
    if number in memory.keys():
        return memory[number]
    else:
        if number == 1:
            memory[number] = 1
        else:
            memory[number] = 1+(memory_Recur(3*number+1,memory) if number % 2 == 1 else
                                 memory_Recur(number//2,memory))
    return memory[number]
def spaces(number_1,number_2,memory):
    number_1,number_2,arreglo = min(number_1,number_2),max(number_1,number_2),[]
    for number in range(number_1,number_2+1):
        arreglo += [memory_Recur(number,memory)]
    return max(arreglo)
def main():
    line = list(map(int, stdin.readline().strip().split()))
    while len(line) != 0:
        answer = spaces(line[0],line[1],{})
        print(line[0],line[1],answer)
        line = list(map(int, stdin.readline().strip().split()))
main()


"""Otro punto de monedas, es de una arena, pero me dio pereza ponerlo en otro .py"""


def ways(n,monedas,dictio,i):
    if i > 4:
        return 0
    else:
        if n - monedas[i] == 0:            #Si el numero funciona
            return 1
        elif n - monedas[i] < 0:           #Si el numero no funciona
            return 0
        else:
            return ways(n-monedas[i],monedas,dictio,i) + ways(n,monedas,dictio,i+1)       #Rama izquierda coge cuando el numero sirve, #rama derecha sirve cuando el numero no sirve se mira la siguiente moneda
def memory(n,monedas,dictio,i):
    if (n,monedas[i]) in dictio.keys():      #Revisa si n y monedas[i] puestos como tuplas estan en el diccionario
        return dictio((n,monedas[i]))        #Si es verdad, retorna el valor que este en ese espacio
    else:                                    # si no:
        dictio[(n,i)] = ways(n,monedas,dictio,i)   #Se genera un espacio con esos valores, donde se le aplica funcion ways con ese valor y ese indice para mirar en monedas
    return dictio[(n,i)]                           #Ahora si retorna el valor en ese espacio
def main():
    line = stdin.readline().strip()                #Lee el numero que manda el usuario
    money = [1,5,10,25,50]                         #Arreglo seguro
    dictio = {}                                    #Diccionario vacio
    while line:                                    #Mientras que la lectura tenga algo que leer:
        print('There are', memory(int(line),money,dictio,0), 'to produce', int(line), 'cents change.') #Se genera el print de la memoria entre el numero dado por el usuario
        line = stdin.readline().strip()                                                                #el arreglo seguro llamado monedas, el diccionario vacio y un indice inicial de 0
main()

