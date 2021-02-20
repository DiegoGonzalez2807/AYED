def airport(city):
    """Funcion para revisar por que aeropuerto tiene que pasar para llegar a su destino, solo retorna el nombre del aeropuerto"""
    airports = [
        ('Aeropuerto El Dorado', 'Bogotá'),
        ('Aeropuerto Alfonso Bonilla Aragón', 'Cali'),
        ('Aeropuerto Internacional Palonegro', 'Bucaramanga'),
        ('Aeropuerto José María Córdova', 'Medellín'),
        ('Aeropuerto La Nubia', 'Manizales'),
        ('Aeropuerto de San Juan de Pasto', 'Pasto'),
        ('Aeropuerto Gustavo Rojas Pinilla', 'Isla de San Andrés'),
        ('Aeropuerto de Cartagena de Indias', 'Cartagena'),
        ('Aeropuerto Internacional Ernesto Cortissoz', 'Barranquilla'),
        ('Aeropuerto Camilo Daza', 'Cúcuta'),
        ('Aeropuerto Simón Bolívar', 'Santa Marta'),
        ('Aeropuerto Perales', 'Ibagué')
    ]
    for i in range(len(airports)-1):
        if city in airports[i]:
            return 'Tendra que pasar por el aeropuerto', airports[i][0]