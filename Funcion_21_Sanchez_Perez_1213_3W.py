print(" ") # print imprime espacio
print("Briana Sarahi Sanchez Perez, 1213, 3-W")
print(" ") # print imprime espacio


def tri_recursion(k):# definiendo la funcion 
  if(k > 0): # abriendo if
    result = k + tri_recursion(k - 1) # haciendo secuencia de operaciones
    print(result)# print imprimiendo resultado
  else: # se ejecuta si la parte es falsa
    result = 0 # dando resultado
  return result # terminando ejecucion

print("\n\nRecursion Example Results") # print imprimiendo
tri_recursion(60) # numero de secuencia

print(" ") # print imprime espacio
