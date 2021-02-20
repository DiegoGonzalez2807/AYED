from sys import stdin
import datos
import datos_avion
def main():
    print('Señor Usuario, deme la ciudad a la que se dirige')
    city = str(stdin.readline().strip())
    print('Desde que ciudad de origen')
    city2 = str(stdin.readline().strip())
    connections = datos.connect(city2,city)
    print('Es usted administrador de la plataforma? Si No')
    answer = stdin.readline().strip()
    if answer.capitalize() == 'Si':
        print(datos.Getsize())
        datos = datos_avion.HashTable(datos.Getsize())
        passengers = datos.getdatas()
        for value in passengers:
            datos.insert(passengers[0], passengers[1])
    else:
        print('No tiene permiso para estar aqui')
main()


