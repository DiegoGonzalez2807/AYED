from sys import stdin
import sys
sys.setrecursionlimit(10000000)
def ways(n,monedas,dictio,i):
    if i > 4:
        return 0
    else:
        if (n, monedas[i]) in dictio.keys():# Revisa si n y monedas[i] puestos como tuplas estan en el diccionario
            return dictio[(n, monedas[i])]
        else:
            if n - monedas[i] == 0:            #Si el numero funciona
                return 1
            elif n - monedas[i] < 0:           #Si el numero no funciona
                return 0
            else:
                dictio[(n,monedas[i])] = ways(n-monedas[i],monedas,dictio,i) + ways(n,monedas,dictio,i+1)#Rama izquierda coge cuando el numero sirve,rama derecha sirve cuando el numero no sirve se mira la siguiente moneda
        return dictio[(n, monedas[i])]
def main():
    line = stdin.readline().strip()                #Lee el numero que manda el usuario
    money = [1,5,10,25,50]                         #Arreglo seguro
    dictio = {}                                    #Diccionario vacio
    while line:                                    #Mientras que la lectura tenga algo que leer:
        print('There are', ways(int(line),money,dictio,0), 'to produce', int(line), 'cents change.') #Se genera el print de la memoria entre el numero dado por el usuario
        line = stdin.readline().strip()                                                                #el arreglo seguro llamado monedas, el diccionario vacio y un indice inicial de 0 
main()