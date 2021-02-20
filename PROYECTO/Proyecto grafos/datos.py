import Taller_grafos


change = {'Bogotá':0,
          'Cali':1,
          'Bucaramanga':2,
          'Medellín':3,
          'Manizales':4,
          'Pasto':5,
          'Isla de San Andrés':6,
          'Cartagena':7,
          'Barranquilla':8,
          'Cúcuta':9,
          'Santa Marta':10,
          'Ibagué':11
          }
airports = {
        'Bogotá':'Aeropuerto El Dorado',
        'Cali':'Aeropuerto Alfonso Bonilla Aragón',
        'Bucaramanga':'Aeropuerto Internacional Palonegro',
        'Medellín':'Aeropuerto José María Córdova',
        'Manizales':'Aeropuerto La Nubia',
        'Pasto':'Aeropuerto de San Juan de Pasto',
        'Isla de San Andrés':'Aeropuerto Gustavo Rojas Pinilla',
        'Cartagena':'Aeropuerto de Cartagena de Indias',
        'Barranquilla':'Aeropuerto Internacional Ernesto Cortissoz',
        'Cúcuta':'Aeropuerto Camilo Daza',
        'Santa Marta':'Aeropuerto Simón Bolívar',
        'Ibagué':'Aeropuerto Perales',
    }

def take_position(number):
    r1 = []
    for value in change.keys():
        r1 += [value]
    return r1[number]

def connect(city_origin,city_destiny):
    n, m = 12, 21
    array = []
    arcs = [
        [0, 11],
        [0, 1],
        [1, 10],
        [1, 3],
        [2, 9],
        [2, 3],
        [3, 5],
        [4, 8],
        [5, 7],
        [6, 4],
        [6, 2],
        [7, 6],
        [8, 1],
        [8, 9],
        [9, 0],
        [10, 7],
        [11, 10],
        [11, 5],
        [3, 9],
        [9, 11],
        [10, 2]
    ]
    vertexes = [x for x in range(n)]
    graph = Taller_grafos.GraphL(vertexes, arcs)
    value1 = change.get(city_origin)
    value2 = change.get(city_destiny)
    r1 = graph.printBFS(graph.BFS(value1),value1,value2)
    for i in range(len(r1)):
        array.append(take_position(r1[i]))
    return answer(city_origin,city_destiny,array,airports)

def answer(city_origin,city_destiny,list_1,airports):
    index = len(list_1[1:len(list_1)-1])
    print('Su punto de origen será el' + ' ' + airports.get(city_origin))
    while index != 0:
        print('Tendra que pasar por el aeropuerto' + ' ' +airports.get(list_1[index]))
        index -= 1
    print('Su punto final será el' + ' ' + airports.get(city_destiny))



