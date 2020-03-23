import cv2
import numpy as np
import glob
import os
from PIL import Image
from collections import OrderedDict
##########  DEFINICIONES DE FUNCIONES NECESARIAS

###### FILTRANDO RUIDO / HACIENDO NITIDA LA IMAGEN
#####Utilizando la umbralización de Kittler utilizando la
#####herramienta antes creada en  https://github.com/brown9804/Image_Segmentation_Project-
#####se obtiene una varianza1: 15.381974 por lo que se utilizan valores
#####de 15 para las imágenes
#####ya que se considera que son de laboratorio sin cambios en la iluminación
#####Considerando las diferentes pruebas se consideran los valores
####15 15 7 15 (30s aprox) a pesar de que
#####la bibliografía leida recomienda valores de 10 10 7 21 (1:42 minutos aprox)
# def denoising_sharpening(input):
#     sin_ruido= cv2.fastNlMeansDenoisingColored(input, None,15,15,7,15)
#     kernel=np.array([[-1,-1,-1,-1,-1],
#                       [-1,2,2,2,-1],
#                       [-1,2,8,2,-1],
#                       [-2,2,2,2,-1],
#                       [-1,-1,-1,-1,-1]])/8.0
#     sin_ruido = cv2.filter2D(sin_ruido,-1,kernel)
#     return sin_ruido

#definimos una funcion que calcule la media aritmetica de los elementos de la lista
#calcula el valor medio de todos los numeros, suma todos y los divide entre la cantidad total
# def media_arit(lista):
#     n = float(len(lista))
#     return tuple(sum(x[i] for x in lista)/n for i in range (len(lista[0])))

# #definimos una funcion para varianza entre los elementos de la lista
# #el cuadrado de la desviación estándar, más adelante se define
# #la desviación estandar.

# def varianza(lista):
#     n = float(len(lista))
#     return tuple(sum(x[i] + (media_arit(lista)-x[i])**2   for x in lista)/n for i in range (len(lista[0])))


####para una lista
def media_arit_lista(lista):
	n = len(lista)
	sumatoria = 0
	for indice in range (0, n):
		sumatoria = sumatoria + lista[indice]
	return sumatoria/n

def varianza_lista(lista):
	n = len(lista)
	sumatoria = 0
	for indice in range (0, n):
		sumatoria = sumatoria + (media_arit_lista(lista)-lista[indice])**2
	return sumatoria/n

def desvia_estan_lista(lista):
	desvi = varianza_lista(lista)**(1/2)
	return desvi

#######   DESVIACION ESTANDAR
#La desviación estándar es la medida de dispersión más común,
#que indica qué tan dispersos están los datos con respecto a
#la media. Mientras mayor sea la desviación estándar, mayor
#será la dispersión de los datos.
## lo necesitamos debido a que no considera cambios muy abruptos en los valores de pixeles,
# asi como la ubicacion de los mismos mayor igual a cero.

#Leer la plantilla
template_green = cv2.imread('/Users/belindabrown/Desktop/Reconocimiento13/Reconocimiento_Por_Imagenes/Templates/ledVerde.jpg',0)
template_naranja = cv2.imread('/Users/belindabrown/Desktop/Reconocimiento13/Reconocimiento_Por_Imagenes/Templates/ledNaranja.jpg',0)
template_naranja_oscuro = cv2.imread('/Users/belindabrown/Desktop/Reconocimiento13/Reconocimiento_Por_Imagenes/Templates/ledNaranjaOscuro.jpg',0)

#Almacenar la anchura (w) y la altura (h) de la plantilla
w_verde, h_verde = template_green.shape[::-1]
w_naranja, h_naranja = template_naranja.shape[::-1]
w_naranja_oscuro, h_naranja_oscuro = template_naranja_oscuro.shape[::-1]
#Especificar un umbral (threshold)
threshold= 0.92
# Directorio con las imagenes averificar
img_dir = '/Users/belindabrown/Desktop/Reconocimiento13/Reconocimiento_Por_Imagenes/ImgAVerificar'
data_path = os.path.join(img_dir,'*.jpg')
files = glob.glob(data_path)
data = []
#Analizando todas las imagenes en el folder
for f1 in files:
	########   Para VERDE    ######
	#PARA COMPARAR X
	Verde_x = []
	X_Verde_antes_filrado = []
	#PARA COMPARAR Y
	Verde_y = []
	Y_Verde_antes_filrado = []
	#LAS COORDENADAS VERDES FILTRADAS
	X_Verde_Filtrado =[]
	Y_Verde_Filtrado =[]
	###PARA UNIR LOS DOS VECTORES VERDES
	Verdes_filtrados = []
	#Cantidad de leds en estado # XXX
	Cantidad_Leds_Verde = 0
	#######    Para AMARILLO NARANJA    #####
	#PARA COMPARAR X
	AmarilloNaranja_x = []
	X_AmarilloNaranja_antes_filrado = []
	#PARA COMPARAR Y
	AmarilloNaranja_y = []
	Y_AmarilloNaranja_antes_filrado = []
	#LAS COORDENADAS VERDES FILTRADAS
	X_AmarilloNaranja_Filtrado =[]
	Y_AmarilloNaranja_Filtrado =[]
	###PARA UNIR LOS DOS VECTORES VERDES
	AmarilloNaranja_filtrados = []
	#Cantidad de leds en estado # XXX
	Cantidad_Leds_AmarilloNaranja = 0

	#######    Para NARANJA NARANJA    #####
	#PARA COMPARAR X
	NaranjaNaranja_x = []
	X_NaranjaNaranja_antes_filrado = []
	#PARA COMPARAR Y
	NaranjaNaranja_y = []
	Y_NaranjaNaranja_antes_filrado = []
	#LAS COORDENADAS VERDES FILTRADAS
	X_NaranjaNaranja_Filtrado =[]
	Y_NaranjaNaranja_Filtrado =[]
	###PARA UNIR LOS DOS VECTORES VERDES
	NaranjaNaranja_filtrados = []
	#Cantidad de leds en estado # XXX
	Cantidad_Leds_NaranjaNaranja = 0

	#lee cada imagen
	img = cv2.imread(f1)
	#almacena sus datos
	print(f1) #picture name
	data.append(img)
	#utiliza un filtro gris para facilitar el reconocimiento
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, 0)
	#compara la imagen utilizando una plantilla
	#Template Matching es un método para buscar y encontrar la ubicación de
	#una imagen de plantilla en una imagen más grande. OpenCV viene con una
	#función cv2.matchTemplate () para este propósito. Simplemente desliza
	#la imagen de la plantilla sobre la imagen de entrada (como en convolución 2D)
	# y compara la plantilla y el parche de la imagen de entrada debajo de la imagen
	# de la plantilla. Se implementan varios métodos de comparación en OpenCV.
	#Devuelve una imagen en escala de grises, donde cada píxel indica cuánto
	#coincide el vecindario de ese píxel con la plantilla.

	####TM_CCOEFF_NORMED hace Coeficiente de correlación: el método se usa simplemente para
	# a) hacer que la plantilla y la imagen sean cero y
	# b) hacer que las partes oscuras de los valores negativos de la imagen
	# y las partes brillantes de los valores positivos de la imagen.
	res_verde = cv2.matchTemplate(img_gray,template_green,cv2.TM_CCOEFF_NORMED)
	res_naranja = cv2.matchTemplate(img_gray,template_naranja,cv2.TM_CCOEFF_NORMED)
	res_naranja_oscuro = cv2.matchTemplate(img_gray,template_naranja_oscuro,cv2.TM_CCOEFF_NORMED)
	#f1Filtrada = cv2.imread(f1)
	#img = denoising_sharpening(f1Filtrada)
	#Anuncia cada vez que se revisa una imagen
	print("Imagen cargada, Analizando patrones...")
	#obtiene la posicion
	#-- teoricamente
	#Devuelve elementos elegidos de x o y dependiendo de la condición.
	#da localizion x, y sepadas de todos cumplen la condicion
	location_verde = np.where(res_verde >= threshold)
	location_naranja = np.where(res_naranja >= threshold)
	location_naranja_oscuro = np.where(res_naranja_oscuro >= threshold)
	###    SI HAY VERDE, ENTONCES...
	## VERDE ANTES DE FILTRADO para X - sin las repeticiones
	if len(location_verde[0]) > 0:
		for iteradorloc0 in sorted(location_verde[0]):
			if iteradorloc0 not in Verde_x:
				Verde_x.append(iteradorloc0)
		#compiando el vector sin repeticiones para generar el segundo a comparar
		X_Verde_antes_filrado =  Verde_x.copy()
		#obteniendo la primera coordenada
		x0 = Verde_x[0]
		#Eliminando la primera coordenada
		X_Verde_antes_filrado.pop(0)
		#Al resultado se le agrega la coordenada eliminada
		X_Verde_Filtrado.append(x0)
		#####Verde antes de filtrar para y -- basicamente vector obtenido menos las coordenadas repetidas
		for iteradorloc1 in sorted(location_verde[1]):
			if iteradorloc1 not in Verde_y:
				Verde_y.append(iteradorloc1)
		#compiando el vector para generar el segundo
		Y_Verde_antes_filrado =  Verde_y.copy()
		# obtiene la primera coordenada obtenida de la lista de elementos sin repeticiones
		y0 = Verde_y[0]
		#Eliminando el primer elemento para poder restar con la lista completa
		Y_Verde_antes_filrado.pop(0)
		#Al resultado se le agrega la coordenada eliminada
		Y_Verde_Filtrado.append(y0)
		#Para automatizar el filtrado se calcula las medidas de dispersion
		X_media_arit_lista_re = media_arit_lista(Verde_x)
		# print("Media x Verde", X_media_arit_lista_re)
		X_varianza_lista_re = varianza_lista(Verde_x)
		# print("Varianza x Verde", X_varianza_lista_re)
		X_desvacion_estandar_re = desvia_estan_lista(Verde_x)
		# print("Desviacion estandar x Verde", X_desvacion_estandar_re)
		Y_media_arit_lista_re = media_arit_lista(Verde_y)
		# print("Media y Verde", Y_media_arit_lista_re)
		Y_varianza_lista_re = varianza_lista(Verde_y)
		# print("Varianza y Verde", Y_varianza_lista_re)
		Y_desvacion_estandar_re = desvia_estan_lista(Verde_y)
		# print("Desviacion estandar y Verde", Y_desvacion_estandar_re)
		# print("Verde x completo ", Verde_x)
		# print('Verde y completo', Verde_y)

		#Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
		# Es decir 144,145,146 son 3 pixeles consecutivos por lo que dibujaría 3 rectangulos
		#Entonces por grupo de datos similares necesitamos una coordenada. Dado que no cambian tanto entre
		#grupos es indiferente sino se obtiene la primera, dado que con la segundo cumple las necesidades.
		for e, i in sorted(zip(Verde_x, X_Verde_antes_filrado)):
			Resta_X_verde = i - e
			# print(i)
			# print(e)
			# print("Resta X Verde", Resta_X_verde, i)
			if X_desvacion_estandar_re < Resta_X_verde:
				X_Verde_Filtrado.append(i)
		X_Verde_Filtrado = list(OrderedDict.fromkeys(X_Verde_Filtrado))
		#Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
		# Es decir 1678,1679,1680 son 3 pixeles consecutivos por lo que dibujaría 3 rectangulos
		#Entonces por grupo de datos similares necesitamos una coordenada. Dado que no cambian tanto entre
		#grupos es indiferente sino se obtiene la primera, dado que con la segundo cumple las necesidades.
		for ee, ii in sorted(zip(Verde_y, Y_Verde_antes_filrado)):
			Resta_Y_verde = ii - ee
			# print(ii)
			# print(ee)
			# print("Resta_Y_verde", Resta_Y_verde, ii)
			if Y_media_arit_lista_re - Y_desvacion_estandar_re < Resta_Y_verde:
				Y_Verde_Filtrado.append(ii)
		Y_Verde_Filtrado = list(OrderedDict.fromkeys(Y_Verde_Filtrado))
		####Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
		####Ahora para poderlo ordenar otra vez en coordenadas necesitamos un arreglo nxn
		####Considerando la logica de filtrado y la arquitectura a nivel de puertos en el commutador
		####Sabemos que dadas les especificaciones necesarias, puede existir un angulo de desviacion, considerando
		#esto y la estructura de los puertos.
		n_X_Verde_nxnC = len(X_Verde_Filtrado)
		n_Y_Verde_nxnC = len(Y_Verde_Filtrado)
		# print("n" , n_Y_Verde_nxnC)
		# print("nx", n_X_Verde_nxnC)
		contador = 0
		while contador < n_Y_Verde_nxnC-1:
			contador = contador +1
			# print(contador, X_Verde_Filtrado)
			if n_X_Verde_nxnC != n_Y_Verde_nxnC and n_X_Verde_nxnC < n_Y_Verde_nxnC:
				X_Verde_Filtrado.append(x0)
		# print("X_Verde_Filtrado", X_Verde_Filtrado)
		# print("Y_Verde_Filtrado", Y_Verde_Filtrado)
		###Uniendo las dos coordenadas x, y
		Verdes_filtrados = sorted(zip(Y_Verde_Filtrado, X_Verde_Filtrado))
		###imprime los puntos en (x,y)
		# print("Pares de coordenadas para punto Verde_filtrados ",Verdes_filtrados)
		for ptVerde in Verdes_filtrados:
		###dibuja el rectangulo en ese caso en donde encuentra verde
		####cv2.rectangle(imagen en donde se dibuja, donde dibujar, color, grueso linea dibujo)
		###color BGR
			cv2.rectangle(img, ptVerde, (ptVerde[0] + w_verde, ptVerde[1] + h_verde), (0,255,255), 1)
		###En esta funcion el color va BGR, lo que hace es poner el texto donde encontró el led
			cv2.putText(img, 'VERDE', ptVerde, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 1)
		###Contar la cantidad de leds que encontró en este estado
			Cantidad_Leds_Verde = Cantidad_Leds_Verde +1
		print("La cantidad de LEDs en estado Verde Verde (encendido/encendido) encontrados es de:      ", Cantidad_Leds_Verde)
	######zip location devuleve  ejemplo:  <zip object at 0x11cf638c0> empacate y accede
	####zip () con n argumentos, entonces la función devolverá un iterador que genera tuplas de longitud n.

	####    SI HAY amarillo naranja, ENTONCES...
	if len(location_naranja[0]) > 0:
	## VERDE ANTES DE FILTRADO para X - sin las repeticiones
		for iteradorloc00 in sorted(location_naranja[0]):
			if iteradorloc00 not in AmarilloNaranja_x:
				AmarilloNaranja_x.append(iteradorloc00)
	####compiando el vector sin repeticiones para generar el segundo a comparar
		X_AmarilloNaranja_antes_filrado =  AmarilloNaranja_x.copy()
	####obteniendo la primera coordenada
		x00 = AmarilloNaranja_x[0]
	####Eliminando la primera coordenada
		X_AmarilloNaranja_antes_filrado.pop(0)
		#Al resultado se le agrega la coordenada eliminada
		X_AmarilloNaranja_Filtrado.append(x00)
	#####Verde antes de filtrar para y -- basicamente vector obtenido menos las coordenadas repetidas
		for iteradorloc11 in sorted(location_naranja[1]):
			if iteradorloc11 not in AmarilloNaranja_y:
				AmarilloNaranja_y.append(iteradorloc11)
	####compiando el vector para generar el segundo
		Y_AmarilloNaranja_antes_filrado =  AmarilloNaranja_y.copy()
	####obtiene la primera coordenada obtenida de la lista de elementos sin repeticiones
		y00 = AmarilloNaranja_y[0]
	###Eliminando el primer elemento para poder restar con la lista completa
		Y_AmarilloNaranja_antes_filrado.pop(0)
	###Al resultado se le agrega la coordenada eliminada
		Y_AmarilloNaranja_Filtrado.append(y00)
	####Para automatizar el filtrado se calcula las medidas de dispersion
		X_media_arit_lista_AN = media_arit_lista(AmarilloNaranja_x)
		# print("Media de Amarillo Naranja X", X_media_arit_lista_AN)
		X_varianza_lista_AN = varianza_lista(AmarilloNaranja_x)
		# print("varianza Amarillo Naranja X", X_varianza_lista_AN)
		X_desvacion_estandar_AN = desvia_estan_lista(AmarilloNaranja_x)
		# print("Desviación estándar Amarillo Naranja X", X_desvacion_estandar_AN)
		Y_media_arit_lista_AN = media_arit_lista(AmarilloNaranja_y)
		# print("Media Amarillo Naranja Y", Y_media_arit_lista_AN)
		Y_varianza_lista_AN = varianza_lista(AmarilloNaranja_y)
		# print("Varianza Amarillo Naranja Y", Y_varianza_lista_AN)
		Y_desvacion_estandar_AN = desvia_estan_lista(AmarilloNaranja_y)
		# print("Desviación estandar Amarillo Naranja Y", Y_desvacion_estandar_AN)
		# print("Amarillo Naranja x completo ", AmarilloNaranja_x)
		# print('Amarillo Naranja y completo', AmarilloNaranja_y)

	####Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
	### Es decir 144,145,146 son 3 pixeles consecutivos por lo que dibujaría 3 rectangulos
	####Entonces por grupo de datos similares necesitamos una coordenada. Dado que no cambian tanto entre
	###grupos es indiferente sino se obtiene la primera, dado que con la segundo cumple las necesidades.
		for eee,iii in sorted(zip(AmarilloNaranja_x,X_AmarilloNaranja_antes_filrado)):
			Resta_X_AN = iii - eee
			# print(iii)
			# print(eee)
			# print("Resta x Amarillo Naranja", Resta_X_AN, iii)
			if X_desvacion_estandar_AN<Resta_X_AN:
				X_AmarilloNaranja_Filtrado.append(iii)
		X_AmarilloNaranja_Filtrado = list(OrderedDict.fromkeys(X_AmarilloNaranja_Filtrado))    #Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
	#### Es decir 1678,1679,1680 son 3 pixeles consecutivos por lo que dibujaría 3 rectangulos
	####Entonces por grupo de datos similares necesitamos una coordenada. Dado que no cambian tanto entre
	####grupos es indiferente sino se obtiene la primera, dado que con la segundo cumple las necesidades.

		for eeee,iiii in sorted(zip(AmarilloNaranja_y,Y_AmarilloNaranja_antes_filrado)):
			Resta_Y_AN = iiii - eeee
			# print(iiii)
			# print(eeee)
			# print("Resta y Amarillo Naranja ", Resta_Y_AN, iiii)
			if Y_media_arit_lista_AN - Y_desvacion_estandar_AN < Resta_Y_AN:
				Y_AmarilloNaranja_Filtrado.append(iiii)
		Y_AmarilloNaranja_Filtrado = list(OrderedDict.fromkeys(Y_AmarilloNaranja_Filtrado))    #Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
	####Ahora para poderlo ordenar otra vez en coordenadas necesitamos un arreglo nxn
	#####Considerando la logica de filtrado y la arquitectura a nivel de puertos en el commutador
	####Sabemos que dadas les especificaciones necesarias, puede existir un angulo de desviacion, considerando
	#####esto y la estructura de los puertos.
		n_X_AN_nxnC = len(X_AmarilloNaranja_Filtrado)
		n_Y_AN_nxnC = len(Y_AmarilloNaranja_Filtrado)
		contadorAN = 0
		while contadorAN < n_Y_AN_nxnC-1 :
			contadorAN = contadorAN +1
			# print(contadorAN, X_AmarilloNaranja_Filtrado)
			if n_X_AN_nxnC != n_Y_AN_nxnC and n_X_AN_nxnC < n_Y_AN_nxnC:
				X_AmarilloNaranja_Filtrado.append(x00)


		# print("X_AN_Filtrado", X_AmarilloNaranja_Filtrado)
		# print("Y_AN_Filtrado", Y_AmarilloNaranja_Filtrado)

	####Uniendo las dos coordenadas x, y
		AmarilloNaranja_filtrados = sorted(zip(Y_AmarilloNaranja_Filtrado, X_AmarilloNaranja_Filtrado ))

	#####imprime los puntos en (x,y)
		# print("Pares de coordenadas para punto Amarillo Naranja Filtradas ",AmarilloNaranja_filtrados)
		#Dibujar un rectángulo alrededor de la región adaptada encontrada en este caso naranja
		for ptAN in AmarilloNaranja_filtrados:
			#dibuja el rectangul        #color BGR
			cv2.rectangle(img, ptAN, (ptAN[0] + w_naranja, ptAN[1] + h_naranja), (0,255,255), 1)
			#En esta funcion el color va BGR, lo que hace es poner el texto donde encontró el led
			cv2.putText(img, 'NARANJA', ptAN, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 1)
			#Contar la cantidad de leds que encontró en este estado
			Cantidad_Leds_AmarilloNaranja = Cantidad_Leds_AmarilloNaranja +1
		print("La cantidad de LEDs en estado Amarillo Naranja (encendido/problema) encontrados es de:      ", Cantidad_Leds_AmarilloNaranja)
	####    SI HAY naranja naranja, ENTONCES...
	if len(location_naranja_oscuro[0]) > 0:
	#####Naranja Naranja ANTES DE FILTRADO para X - sin las repeticiones
		for iteradorloc000 in sorted(location_naranja_oscuro[0]):
			if iteradorloc000 not in NaranjaNaranja_x:
				NaranjaNaranja_x.append(iteradorloc000)
	####compiando el vector sin repeticiones para generar el segundo a comparar
		X_NaranjaNaranja_antes_filrado =  NaranjaNaranja_x.copy()
	####obteniendo la primera coordenada
		x000 = NaranjaNaranja_x[0]
	####Eliminando la primera coordenada
		X_NaranjaNaranja_antes_filrado.pop(0)
		#Al resultado se le agrega la coordenada eliminada
		X_NaranjaNaranja_Filtrado.append(x000)
	#####Verde antes de filtrar para y -- basicamente vector obtenido menos las coordenadas repetidas
		for iteradorloc111 in sorted(location_naranja_oscuro[1]):
			if iteradorloc111 not in NaranjaNaranja_y:
				NaranjaNaranja_y.append(iteradorloc111)
	####compiando el vector para generar el segundo
		Y_NaranjaNaranja_antes_filrado =  NaranjaNaranja_y.copy()
	###3obtiene la primera coordenada obtenida de la lista de elementos sin repeticiones
		y000 = NaranjaNaranja_y[0]
	####Eliminando el primer elemento para poder restar con la lista completa
		Y_NaranjaNaranja_antes_filrado.pop(0)
	####Al resultado se le agrega la coordenada eliminada
		Y_NaranjaNaranja_Filtrado.append(y000)
	####Para automatizar el filtrado se calcula las medidas de dispersion
		X_media_arit_lista_NN = media_arit_lista(NaranjaNaranja_x)
		# print("Media de Naranja Naranja X", X_media_arit_lista_NN)
		X_varianza_lista_NN = varianza_lista(NaranjaNaranja_x)
		# print("Varianza Naranja Naranja X", X_varianza_lista_NN)
		X_desvacion_estandar_NN = desvia_estan_lista(NaranjaNaranja_x)
		# print("Desviación estándar Naranja Naranja X", X_desvacion_estandar_NN)
		Y_media_arit_lista_NN = media_arit_lista(NaranjaNaranja_y)
		# print("Media Naranja Naranja Y", Y_media_arit_lista_NN)
		Y_varianza_lista_NN = varianza_lista(NaranjaNaranja_y)
		# print("Varianza Naranja Naranja Y", Y_varianza_lista_NN)
		Y_desvacion_estandar_NN = desvia_estan_lista(NaranjaNaranja_y)
		# print("Desviación estandar Naranja Naranja Y", Y_desvacion_estandar_NN)
		# print("Naranja Naranja x completo ",  NaranjaNaranja_x)
		# print('Naranja Naranja y completo', NaranjaNaranja_y)

	#####Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
	###Es decir 144,145,146 son 3 pixeles consecutivos por lo que dibujaría 3 rectangulos
	####Entonces por grupo de datos similares necesitamos una coordenada. Dado que no cambian tanto entre
	####grupos es indiferente sino se obtiene la primera, dado que con la segundo cumple las necesidades.
		for nne,nni in sorted(zip(NaranjaNaranja_x,X_NaranjaNaranja_antes_filrado)):
			Resta_X_NN = nni - nne
			# print(nni)
			# print(nne)
			# print("Resta x Naranja Naranja", Resta_X_NN, nni)
			if X_desvacion_estandar_NN<Resta_X_NN:
				X_NaranjaNaranja_Filtrado.append(nni)
		X_NaranjaNaranja_Filtrado = list(OrderedDict.fromkeys(X_NaranjaNaranja_Filtrado))    #Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
	####Es decir 1678,1679,1680 son 3 pixeles consecutivos por lo que dibujaría 3 rectangulos
	#####Entonces por grupo de datos similares necesitamos una coordenada. Dado que no cambian tanto entre
	####grupos es indiferente sino se obtiene la primera, dado que con la segundo cumple las necesidades.

		for nnee,nnii in sorted(zip(NaranjaNaranja_y,Y_NaranjaNaranja_antes_filrado)):
			Resta_Y_NN = nnii - nnee
			# print(nnii)
			# print(nnee)
			# print("Resta y Naranja Naranja ", Resta_Y_NN, nnii)
			if Y_media_arit_lista_NN - Y_desvacion_estandar_NN < Resta_Y_NN:
				Y_NaranjaNaranja_Filtrado.append(nnii)
		Y_NaranjaNaranja_Filtrado = list(OrderedDict.fromkeys(Y_NaranjaNaranja_Filtrado))    #Filtro para la coordenada X, debido que localiza pixeles con umbral similar en la zona cerca
	####Ahora para poderlo ordenar otra vez en coordenadas necesitamos un arreglo nxn
	###Considerando la logica de filtrado y la arquitectura a nivel de puertos en el commutador
	####Sabemos que dadas les especificaciones necesarias, puede existir un angulo de desviacion, considerando
	###esto y la estructura de los puertos.
		n_X_NN_nxnC = len(X_NaranjaNaranja_Filtrado)
		n_Y_NN_nxnC = len(Y_NaranjaNaranja_Filtrado)
		contadorNN = 0
		while contadorNN < n_Y_NN_nxnC-1 :
			contadorNN = contadorNN +1
			# print(contadorNN, X_NaranjaNaranja_Filtrado)
			if n_X_NN_nxnC != n_Y_NN_nxnC and n_X_NN_nxnC < n_Y_NN_nxnC:
				X_NaranjaNaranja_Filtrado.append(x000)


		# print("X_NN_Filtrado", X_NaranjaNaranja_Filtrado)
		# print("Y_NN_Filtrado", Y_NaranjaNaranja_Filtrado)

	#Uniendo las dos coordenadas x, y
		NaranjaNaranja_filtrados = sorted(zip(Y_NaranjaNaranja_Filtrado, X_NaranjaNaranja_Filtrado))

	###imprime los puntos en (x,y)
		# print("Pares de coordenadas para punto Naranja Naranja Filtradas ",NaranjaNaranja_filtrados)
		####Dibujar un rectángulo alrededor de la región adaptada encontrada en este caso naranja oscuro
		for ptNN in NaranjaNaranja_filtrados:
			####dibuja el rectángulo        #color BGR
			cv2.rectangle(img, ptNN, (ptNN[0] + w_naranja_oscuro, ptNN[1] + h_naranja_oscuro), (0,255,255), 1)
			####En esta funcion el color va BGR, lo que hace es poner el texto donde encontró el led
			cv2.putText(img, 'NARANJA NARANJA', ptNN, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 1)
			###Imprime la cantidad de leds encontrados
			Cantidad_Leds_NaranjaNaranja = Cantidad_Leds_NaranjaNaranja + 1
		print("La cantidad de LEDs en estado Naranja Naranja (problema/problema) encontrados es de:      ", Cantidad_Leds_NaranjaNaranja)

	####me muestra la figura ya analizada
	cv2.imshow("Imagen Procesada",img)
	###dado que son varias se espera hasta que presione una tecla y así analiza
	###la otra imagen
	cv2.waitKey(0)
###una vez terminado elimina todas las ventanas
cv2.destroyAllWindows()
