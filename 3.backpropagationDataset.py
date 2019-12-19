# encoding: utf-8
# Autor: Carlos Andres Delgado
# Algoritmo propagación hacia atrás
# Cargamos Dataset https://ocw.mit.edu/courses/sloan-school-of-management/15-097-prediction-machine-learning-and-statistics-spring-2012/datasets/
# Haberman’s Survival (CSV)	Integer	Haberman description (TXT)
import numpy as np
import math
import matplotlib.pyplot as plt

#Implementación algoritmo BP Xor

#Función escalon
def escalon(x):
	if x >= 0:
		return 0
	else:
		return 1

#Función lineal
#Función lineal
def lineal(x):
	if x >= 0:
		return x
	else:
		return 0

#Derivada lineal
def derivadaLineal(x):
  return 1


#Función sigmoidea
def sigmoidea(x):
	if x > 45:
		return 1
	elif x < -45:
		return 0
	else:
		return 1.0 / (1.0 + math.exp(-x))

#Derivada sigmoidea
def derivadaSigmoidea(x):
  return sigmoidea(x)*(1 - sigmoidea(x));


#Para ajustar
def funcionActivacion(x):
  #z = lineal(x);
  z = sigmoidea(x)
  return z
  
def derivada(x):
  #z = derivadaLineal(x)
  z = derivadaSigmoidea(x)
  return z


def redNeuronal(entrada, pesosCapaOculta, pesosCapaSalida, tendenciasCapaOculta, tendenciasCapaSalida):
  
  #Capa de entrada
  #No se realiza ningun procesamiento
  #*************************************

  
  #Capa oculta
  
  entradaNetaCapaOculta = np.dot(pesosCapaOculta,np.transpose(entrada))
  entradaNetaCapaOculta = entradaNetaCapaOculta + tendenciasCapaOculta
  
  salidaCapaOculta = np.zeros(entradaNetaCapaOculta.shape[0])
  for i in range(0, entradaNetaCapaOculta.shape[0]):
	  salidaCapaOculta[i] = funcionActivacion(entradaNetaCapaOculta[i])
	
  #*************************************
  #Capa de salida
  
  entradaNetaCapaSalida = np.dot(pesosCapaSalida,np.transpose(salidaCapaOculta))
  entradaNetaCapaSalida = entradaNetaCapaSalida + tendenciasCapaSalida
  
  salida = np.zeros(entradaNetaCapaSalida.shape[0])
  
  for i in range(0, entradaNetaCapaSalida.shape[0]):
	  salida[i] = funcionActivacion(entradaNetaCapaSalida[i])
  
  return salida,entradaNetaCapaOculta,entradaNetaCapaSalida, salidaCapaOculta


def backPropagation(factorEntrenamiento,errorPermitido,datos,max_it):

	pesosCapaOculta = 2*np.random.rand(15,3)-1
	tendenciasCapaOculta = 2*np.random.rand(15)-1
	pesosCapaSalida = 2*np.random.rand(15)-1
	tendenciasCapaSalida = 2*np.random.rand(1)-1 
	
	#Tomando en cuenta el patrón de entrada
	#Tomamos el 80% de los datos para entrenamiento y el 20% para pruebas
	size = datos.shape[0]
	indicesReordenados = np.random.permutation(datos.shape[0])
	trainingSize = int(math.floor(0.8*size))
	
	training_idx = indicesReordenados[:trainingSize]
	test_idx = indicesReordenados[trainingSize:]
	
	entrenamiento, prueba = datos[training_idx,:], datos[test_idx,:]	
	
	#Si los datos son muy pocos, se recomienda usar todos para entrenar
	#entrenamiento = datos

	#Calculamos error global
	errorGlobal = 0
	for i in range(0, entrenamiento.shape[0]):
		entradaActual = entrenamiento[i,0:3]
		salidaDeseada = entrenamiento[i,3]
		salidaObtenida,entradaNetaCapaOculta,entradaNetaCapaSalida, salidaCapaOculta = redNeuronal(entradaActual, pesosCapaOculta, pesosCapaSalida, tendenciasCapaOculta, tendenciasCapaSalida)

		#Calculamos el error cuadrático medio
		errorGlobal += math.pow(salidaDeseada - salidaObtenida, 2)	
	errorGlobal = errorGlobal/2
	error = np.array([errorGlobal])
	#Calculamos error total (entrenamiento + prueba)
	errorTotal = 0
	for i in range(0, datos.shape[0]):
		entradaActual = datos[i,0:3]
		salidaDeseada = datos[i,3]
		salidaObtenida,entradaNetaCapaOculta,entradaNetaCapaSalida, salidaCapaOculta = redNeuronal(entradaActual, pesosCapaOculta, pesosCapaSalida, tendenciasCapaOculta, tendenciasCapaSalida)

		#Calculamos el error cuadrático medio
		errorTotal += math.pow(salidaDeseada - salidaObtenida, 2)		
	

	errorT = np.array([errorTotal])
	
	it = 0
	patron = 0
	while errorGlobal>=errorPermitido and it < max_it:
		
		entradaActual = entrenamiento[patron,0:3]
		salidaDeseada = entrenamiento[patron,3]
		
		salidaObtenida,entradaNetaCapaOculta,entradaNetaCapaSalida,salidaCapaOculta = redNeuronal(entradaActual, pesosCapaOculta, pesosCapaSalida, tendenciasCapaOculta, tendenciasCapaSalida)
		 
		#calculamos el error de salida
		errorSalida = np.zeros(salidaObtenida.shape[0])
		for i in range(0, salidaObtenida.shape[0]):
			errorSalida[i] = (salidaDeseada-salidaObtenida[i])*derivada(entradaNetaCapaSalida[i])
			
		#Calculamos el error de la capa oculta
		errorCapaOculta = np.zeros(salidaCapaOculta.shape[0])
		for i in range(0, salidaCapaOculta.shape[0]):
			errorCapaOculta[i] = errorSalida*derivada(entradaNetaCapaOculta[i])*pesosCapaSalida[i]  

		#Actualizamos pesos capa salida	
		for n in range(0, pesosCapaSalida.shape[0]):
			pesosCapaSalida[n] = pesosCapaSalida[n] + factorEntrenamiento*errorSalida*salidaCapaOculta[n] 
		
		tendenciasCapaSalida = tendenciasCapaSalida + factorEntrenamiento*errorSalida
		
		#Actualizamos pesos en capa oculta
		#pesosCapaOculta = pesosCapaOculta + factorEntrenamiento*errorCapaOculta*entradaActual
		for n in range(0, pesosCapaOculta.shape[0]):
			for m in range(0, pesosCapaOculta.shape[1]):
				pesosCapaOculta[n,m] = pesosCapaOculta[n,m] +  factorEntrenamiento*errorCapaOculta[n]*entradaActual[m]
		

		for n in range(0, tendenciasCapaOculta.shape[0]):
			tendenciasCapaOculta[n] = tendenciasCapaOculta[n] + factorEntrenamiento*errorCapaOculta[n]		
		
		#Calculamos error global
		errorGlobal = 0
		for i in range(0, entrenamiento.shape[0]):
			entradaActual = entrenamiento[i,0:3]
			salidaDeseada = entrenamiento[i,3]
			salidaObtenida,a,b,c = redNeuronal(entradaActual, pesosCapaOculta, pesosCapaSalida, tendenciasCapaOculta, tendenciasCapaSalida)
			#Calculamos el error cuadrático medio
			errorGlobal += math.pow(salidaDeseada - salidaObtenida, 2)	
		errorGlobal = errorGlobal/2	
		error = np.append(error, errorGlobal)

		errorTotal = 0
		for i in range(0, datos.shape[0]):
			entradaActual = datos[i,0:3]
			salidaDeseada = datos[i,3]
			salidaObtenida,entradaNetaCapaOculta,entradaNetaCapaSalida, salidaCapaOculta = redNeuronal(entradaActual, pesosCapaOculta, pesosCapaSalida, tendenciasCapaOculta, tendenciasCapaSalida)

			#Calculamos el error cuadrático medio
			errorTotal += math.pow(salidaDeseada - salidaObtenida, 2)		
		errorTotal = errorTotal/2	
		errorT = np.append(errorT, errorTotal)
		
		it = it+1
		patron = patron+1
		if patron>=entrenamiento.shape[0]:
			patron=0
		
	return error, errorT, pesosCapaOculta,tendenciasCapaOculta,	pesosCapaSalida,tendenciasCapaSalida
"""
https://ocw.mit.edu/courses/sloan-school-of-management/15-097-prediction-machine-learning-and-statistics-spring-2012/datasets/haberman_info.txt
 Attribute Information:
   1. Age of patient at time of operation (numerical)
   2. Patient's year of operation (year - 1900, numerical)
   3. Number of positive axillary nodes detected (numerical)
   4. Survival status (class attribute)
         0 = the patient survived 5 years or longer
         1 = the patient died within 5 year
"""

datos = np.genfromtxt('entrenamiento.csv', delimiter=',')

factorEntrenamiento = 0.01
errorPermitido = 10
max_iter = 5000
error, errorT, pesosCapaOculta,tendenciasCapaOculta,pesosCapaSalida,tendenciasCapaSalida  = backPropagation(factorEntrenamiento,errorPermitido,datos,max_iter)

for i in range(0, datos.shape[0]):
	entradaActual = datos[i,0:3]
	salidaDeseada = datos[i,3]
	salidaObtenida,a,b,c = redNeuronal(entradaActual, pesosCapaOculta, pesosCapaSalida, tendenciasCapaOculta, tendenciasCapaSalida)
	print("******************")
	print("Entrada",entradaActual)
	print("Salida Deseada",salidaDeseada)
	print("Salida Obtenida",salidaObtenida)


#Pintamos la evolución del error
figura = plt.figure()
plt.title(u'Función de perdida Neuronal Backpropagation')
plt.xlabel('Iteraciones')
plt.ylabel(u'Error cuadrático medio')
plt.plot(range(1,error.shape[0]+1), error,'b-')
plt.plot(range(1,errorT.shape[0]+1), errorT,'r-')
plt.grid(True)
plt.legend(["Error entrenamiento","Error global"])
plt.show()
