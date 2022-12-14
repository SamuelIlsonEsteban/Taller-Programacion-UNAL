# -*- coding: utf-8 -*-
"""Taller2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1thHmXAOGvpaCTNfrnhQpBz-rgz-Bvh9f

Escriba un algoritmo que dado un número entero, indique si este valor es par o impar.(recordar Todos los operadores aritméticos "[+, -, *, /, %MOD"]
"""

x=int(input("Inserte un número entero: ")) #Solicita un número entero al usuario
if (x//2)==x/2 : #Determina si es par con la igualdad entre la division entera y la division normal
  print("su número es par") #Mensaje en caso de que sea par
else:
  print("su número es impar") #Mensaje en caso de que sea impar

"""Escriba un algoritmo que pida un número y también un porcentaje entre 0 y 100 que puede ser decimal,  el algoritmo debe entregar el cálculo del porcentaje del primer número, Si el usuario ingresa un dato fuera del rango  (0 a 100), debe mostrar un error y volver a pedir el porcentaje."""

x=float(input("Ingrese un numero: ")) #Se define una variable deen la que se pide un numero aleatorio para que el usuario ingrese.
y=float(input("Ingrese un valor porcentual(entre 0 y 100): ")) #se solicita un valor porcentual, se guarda en otra variable
r=0.0 #se define una variable en donde se va a guardar el resultado del programa 
if y<=100 and y>=0: #se asegura que el valor de porcentaje este entre 0 y 100
  y=y/100 #se transforma el valor del porcentaje a decimal, para hacer el calculo
  r=x*y #se calcula el porcentaje del número ingresado por el usuario
  print("El resultado es: ",r) #se imprime el resultado
else:
  print("Ingrese un número valido:") #mensaje en caso de que el valor del porcentaje este fuera del rango

"""Con base en el primer Ejercicio, si el número indicado es par, entregar todos los números pares entre el 0 y el número.

"""

x=int(input("Inserte un número entero: ")) #Solicita un número entero al usuario
if (x//2)==x/2 : #Determina si es par con la igualdad entre la division entera y la division normal
  print("su número es par") #Mensaje en caso de que sea par
  print("los números pares entre 0 y",x,"son: ") #Preambulo para la secuencia de números pares
  for i in (range(2, x, 2)): #bucle for en un rango entre 2 (para evitar el 0) y el numero del usuario, va sumando de 2 en 2.
    print(i, end=" ") #imprimir el bucle de manera horizontal
else:
  print("su número es impar") #Mensaje en caso de que sea impar

"""Escriba un algoritmo que dado un número entero, entregue la suma de todos los números entre el 0 y el número dado."""

x=int(input("inserte un número entero: "))#Se define una variable que debe ser un numero entero
t1=0#se definen dos variables, t1 y t2, ambas para mostrar un resultado al final, siendo t1 en caso de que x sea positivo y t2 si x es negativo
t2=0
if x>0:#se pone la condicion de que x sea positivo
  for i in(range(1,x,1)):#se saca una lista de los numeros enteros entre 0 y x, el rango empieza en 1 para evitar el 0 y va avanzando de 1 en 1
    t1 += i #se define a t1 como la suma de todos los numeros positivos entre 0 y x
    print(i, end=" ") #se imprime uno por uno los numeros entre 0 y x de forma horizontal
    if i!=(x-1): #se condiciona la impresion del "+" despues de cada numero entre 0 y x, para que no lo imprima en el ultimo numero
      print("+", end=" ")
  print("=",t1,)  #se imprime un igual al final de la secuencia de numeros y "+", y el resultado
elif x<0: #ahora si x es menor que 0(numero negativo) repite el procedimiento de arriba pero en el espectro negativo
  for i in(range(-1,x,-1)): #la secuencia parte de -1 y va de -1 en -1
    t2 += i #en este caso la suma se define como t2
    print(i, end=" ") # se imprime los valores de 0 a x uno a uno
  print("=",t2)    
else:
  print(0) #en caso de que x sea 0, se imprime 0 sin decir nada mas