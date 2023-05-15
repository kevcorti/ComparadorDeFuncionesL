#Crear una cantidad n de puntos

#Debe empezar en un punto (x, y)

#Los puntos deben ir incrementando en X, no pueden retroceder

#El rango de puntos debe ser -100<=x<=100 y -100<=y<=100
import random as rd
file = open("funciones2.csv", "w")
file.write("id_funcion,puntos"+"\n")

for grafica in range(100):
  cant_actual = 0
  
  cant_puntos = rd.randint(10,10)
  start_point_x = rd.randint(-10, 10)
  start_point_y = rd.randint(-10, 10)
  
  l_data = [str(grafica)]
  
  while(cant_puntos != cant_actual):
    start_point_x += rd.randint(1, 5)
    start_point_y += rd.randint(0, 5)
    cant_actual+=1
    point = "{},{}".format(start_point_x, start_point_y)
    l_data.append(point)
  file.write("|".join(l_data)+"\n")
