def suma(lista,n):
    if n == 0:
         return lista[0]
    return lista[n] + suma(lista,n-1)