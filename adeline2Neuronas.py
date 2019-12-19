# encoding: utf-8
# Autor: Carlos Andres Delgado
# Algoritmo Adeline
#Esta red neuronal, primera salida suma, segunda salida 2x+y

import numpy as np
import matplotlib.pyplot as plt
import math
import random as rnd


#Función lineal
def lineal(x):
	result = x
	return result

#Neurona
def redNeuronal(entrada, pesos, theta):
	entradaNetaN1 = np.dot(pesos[0,:],np.transpose(entrada))+theta[0]
	salidaN1 = lineal(entradaNetaN1)
	
	entradaNetaN2 = np.dot(pesos[1,:],np.transpose(entrada))+theta[1]
	salidaN2 = lineal(entradaNetaN2)
	
	return np.array([salidaN1,salidaN2])

#Algoritmo Adeline
def algoritmoAdeline(entrada, tasaAprendizaje, errorAceptado,entradaPrueba):
	#Error
	evolucionDelError = np.array([])	
	evolucionDelErrorPruebas = np.array([])
	#Generar pesos aleatorios entre -1 y 1
	pesos = 2*np.random.rand(2,2)-1
	theta = 2*np.random.rand(2)-1
	#Iniciamos con el primer patron
	patron = 0
	
	#Obtenemos filas y columnas
	filas = entrada.shape[0]
	columnas = entrada.shape[1]
	
	#El primer criterio de parada es el número de iteraciones
	for it in range(0,iteraciones):
		error = 0
		#entrada.shape[0] número de datos en la primera dimensión (filas)
		#Probamos todas las entradas con los pesos
		for i in range(0, filas):
			entradaActual = entrada[i,0:2]
			salidaDeseada = entrada[i,2:4]
			salidaObtenida = redNeuronal(entradaActual,pesos,theta)
			#Calculamos el error cuadrático medio

			error += math.pow(salidaDeseada[0] - salidaObtenida[0], 2)
			error += math.pow(salidaDeseada[1] - salidaObtenida[1], 2)
		error = error/2
		evolucionDelError = np.append(evolucionDelError,error)

		#Error de pruebas
		errorPruebas = 0
		for i in range(0,entradasPruebas.shape[0]):
			entradaActual = entradasPruebas[i,0:2]
			salidaDeseada = entradasPruebas[i,2:4]
			salidaObtenida = redNeuronal(entradaActual,pesos,theta)
			#Calculamos el error cuadrático medio

			errorPruebas += math.pow(salidaDeseada[0] - salidaObtenida[0], 2)
			errorPruebas += math.pow(salidaDeseada[1] - salidaObtenida[1], 2)		
			
		errorPruebas=errorPruebas/2
		evolucionDelErrorPruebas = np.append(evolucionDelErrorPruebas,errorPruebas)
		
		#El segundo criterio de parada es si alcanzamos un error = 0
		if(error<=errorAceptado):
			break
		else:
			#Si hay error actualizamos los pesos con la regla del perceptrón
						
			#Obtenemos el error de un patrón dado 
			entradaActual = entrada[patron,0:2]
			salidaDeseada = entrada[patron,2:4]
			salidaObtenida = redNeuronal(entradaActual,pesos,theta)

			#Debido a que es una sola neurona tomamos el error de este patrón
			errorPatronN1 = salidaDeseada[0] - salidaObtenida[0]	
			errorPatronN2 = salidaDeseada[1] - salidaObtenida[1]

			#Se toma columnas-1, ya que la ultima columna es la salida
			for j in range(0,columnas-2):
				pesos[0,j] = pesos[0,j] + tasaAprendizaje*errorPatronN1*entradaActual[j]
				pesos[1,j] = pesos[1,j] + tasaAprendizaje*errorPatronN2*entradaActual[j]

			theta[0] = theta[0] + tasaAprendizaje*errorPatronN1	
			theta[1] = theta[1] + tasaAprendizaje*errorPatronN2	
			#Ahora seguimos con el siguiente patrón de entrada
			patron=patron+1
			
		#Si todos los patrones han sido probados, volvemos a empezar
		if patron>=filas:
			patron = 0
		
	return pesos, evolucionDelError,theta, evolucionDelErrorPruebas
    
#Tasa de aprendizaje
tasaAprendizaje = 0.1

#Funcion suma
#entradasEntrenamiento = np.array([[1,3,4,5],[2,1,3,5],[2,2,4,6],[1,1,2,3]])
entradasEntrenamiento = np.array([[1,3,4,7],[2,1,3,4],[2,2,4,6],[1,1,2,3]])
entradasPruebas = np.array([[6,7,13,20],[5,6,8,14],[5,9,13,22],[9,9,18,27],[10,8,18,26],[1,7,8,15]])

iteraciones = 200

#Error aceptado
errorAceptado = 0.8

pesos, evolucionDelError,theta, evolucionDelErrorPruebas = algoritmoAdeline(entradasEntrenamiento, tasaAprendizaje,errorAceptado,entradasPruebas)

filas = entradasEntrenamiento.shape[0]
columnas = entradasEntrenamiento.shape[1]

#Probamos los pesos entrenados
for i in range(0, filas):
	entradaActual = entradasEntrenamiento[i,0:2]
	salidaDeseada = entradasEntrenamiento[i,2:4]
	salidaObtenida = redNeuronal(entradaActual,pesos,theta)
	print("******************")
	print("Entrada",entradaActual)
	print("Salida Deseada",salidaDeseada)
	print("Salida Obtenida",salidaObtenida)

print("Pesos",pesos)
print("Error",evolucionDelError)
#Pintamos la evolución del error
figura = plt.figure()
plt.title(u'Aprendizaje y Error red Neuronal')
plt.xlabel('Iteraciones')
plt.ylabel(u'Error cuadrático medio')
plt.plot(range(1,evolucionDelError.shape[0]+1), evolucionDelError,'bo-')
plt.plot(range(1,evolucionDelErrorPruebas.shape[0]+1), evolucionDelErrorPruebas,'ro-')
plt.grid(True)
plt.xticks(range(1,evolucionDelError.shape[0]+1))
plt.legend(["Entrenamiento","Error de pruebas"])
plt.show()

