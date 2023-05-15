import numpy as np
import time
from datetime import timedelta

S_PERCENTAGE = 0.4 #Variable de control de similitud

#Función que recibe de entrada dos listas de pendientes. Se buscará, por medio de DP, la coincidencias entre estas dos gráficas y determinar si son iguales, similares o diferentes.
def LCSlopes(slps_1, slps_2):
  N = len(slps_1)
  M = len(slps_2)

  #Creación de matriz MxN con base en las pendientes
  LCSuff = [[0 for k in range(M+1)] for l in range(N+1)]
  mx = 0 #Variable que contiene el número secuencias comúnes
  for i in range(N + 1):
    for j in range(M + 1):
      if (i == 0 or j == 0):
        LCSuff[i][j] = 0
      elif (slps_1[i-1] == slps_2[j-1]):
        #En el caso que las pendientes sean iguales, se suma +1 a la diagonal.
        LCSuff[i][j] = LCSuff[i-1][j-1] + 1
        mx = max(mx, LCSuff[i][j])
      else:
        LCSuff[i][j] = 0
  
  #Etiquetas E = Equals, S = Similar, D = Different      
  if M>=N:
    percentage = mx/N

    if percentage == 1.00 and (N==M):
      #Para ser iguales tiene que tener la misma cantidad de elementos
      return "E"
    elif percentage > S_PERCENTAGE:
      return "S"
  elif N>M:
    percentage = mx/M
    if percentage > S_PERCENTAGE:
      return "S"
  return "D"

similares = []
iguales = []
diferentes = []

def compararGraficas(listaP, listaIds): 
  n = len(listaP)
  matrix = np.full([n,n], "")
  
  for i in range(n):
    for j in range(n):
      if i==j:
        matrix[i][j] = "E"
      else:
        if matrix[j][i] == "": #verifica que no haya sido calculado previamente
          valor = LCSlopes(listaP[i], listaP[j])
          matrix[i][j] = valor
          
          if valor == "E":
            iguales.append("(" + str(listaIds[i])+","+str(listaIds[j])+")")
          elif valor == "S":
            similares.append("(" +str(listaIds[i])+","+str(listaIds[j])+")")
          else:
            diferentes.append("(" +str(listaIds[i])+","+str(listaIds[j])+")")
        else: #si ya fue calculado, lo copia
          matrix[i][j] = matrix[j][i]
  return matrix

def leerArchivo(archivo):
  diccionario_funciones = {}
  file = open(archivo, "r")
  file.readline()

  for idx, line in enumerate(file):
    lista = line.strip().split("|")
    nfuncion = lista[0] #Se obtiene el nombre de la función
    diccionario_funciones[nfuncion] = []
    puntos = lista[1:]

    #Se obtiene la lista de pendietes
    for i in range(len(puntos) - 1):
      x1, y1 = puntos[i].split(",")
      x1, y1  = int(x1), int(y1)
  
      x2, y2 = puntos[i + 1].split(",")
      x2, y2  = int(x2), int(y2)
      diccionario_funciones[nfuncion].append((y2-y1)/(x2-x1)) #Fórmula de pendiente
  
  return diccionario_funciones

diccionario = leerArchivo("funciones.csv")

listaPendientes = list(diccionario.values())
listaIds = list(diccionario.keys())
start_time = time.monotonic()
matrix = compararGraficas(listaPendientes, listaIds)
end_time = time.monotonic()
print(matrix)
print()
print("Similares:",similares)
print()
print("Iguales:", iguales)
print()
print("Diferentes:", diferentes)
print()

f = open("resultados.txt", "w")
f.write("Iguales:")
f.write(' '.join(iguales))
f.write("\n")
f.write("Similares:")
f.write(' '.join(similares))
f.write("\n")
f.write("Diferentes:")
f.write(' '.join(diferentes))
f.close()

print(timedelta(seconds=end_time - start_time))