# -*- coding: utf-8 -*-
"""
@autores: Dayana, Abel, Franco

"""
import numpy as np
from random import randrange
from math import sqrt
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.cluster import KMeans



class Agrupador_K_medias:
    def __init__(self, X, iteraciones, ventana_clasificacion, t,  K = 2):
        '''
        Se inicializa los atributos de la instancia
        '''
        # datos
        self.__X = X
        # matriz de pesos
        self.__W = np.zeros((X.shape[0], K))
        # centroides generados aleatoriamente
        self.__Centroides = np.array(self.__crear_centroide())
        # cantidad de iteraciones especificada por el usuario
        self.__iteraciones = iteraciones
        # interfaz en donde se mostrara el resultado final
        self.__ventana_clasificacion = ventana_clasificacion
        # etiquetas correctas
        self.__etiquetas_correctas = t

    def __calcular_min(self, fila_actual, columna_actual):
        '''
        Metodo que calcula el valor minimo de una lista
        '''
        # inicialmente como elemento menor se asigna el primer elemento de los datos, como referencia
        elemento_menor = self.__X[fila_actual][columna_actual]
        # se recorre todas las filas de los datos
        for fila in self.__X:
            # se verifica por columna, buscando el elemento menor
            if fila[columna_actual] < elemento_menor:
                # se guarda el menor
                elemento_menor = fila[columna_actual]
        return elemento_menor

    def __calcular_max(self, fila_actual, columna_actual):
        '''
        Metodo que calcula el valor maximo de una lista
        '''
        # inicialmente como elemento mayor se asigna el primer elemento de los datos, como referencia
        elemento_mayor = self.__X[fila_actual][columna_actual]
        # se recorre todas las filas de los datos
        for fila in self.__X:
            # se verifica por columna, buscando el elemento mayor
            if fila[columna_actual] > elemento_mayor:
                # se guarda el menor
                elemento_mayor = fila[columna_actual]
        return elemento_mayor 

    def __ubicar_centroides(self, minimo, maximo, centroide):
        '''
        Metodo que asigna al centroide su respectivo valor x y y
        '''
        # se crean sus valores de manera aleatoria con los minimos y maximos
        valor_x_centroide = randrange(int(minimo), int(maximo))
        valor_y_centroide = randrange(int(minimo), int(maximo))
        # se asigna al centroide sus valores correspondientes
        centroide += [[valor_x_centroide, valor_y_centroide]]
        return centroide   

    def __crear_centroide(self):
        '''
        Metodo que crea un centroide nuevo
        '''
        fila = 0
        columna = 0
        centroide = []
        # se crean centroides  hasta que no queden filas y columnas por revisar
        while fila < len(self.__X) and columna < len(self.__X[0]):
            # se calcula el minimo de las columnas
            minimo = self.__calcular_min(fila, columna)
            # se calcula el maximo de las columnas
            maximo = self.__calcular_max(fila, columna)
            # se llama al metodo encargado de asignarle los valores correspondientes del centroide
            centroide = self.__ubicar_centroides(minimo, maximo, centroide)
            fila +=1
            columna += 1
        return centroide

    def __calcular_distancia_euclidiana(self, fila_X, fila_Centroide):
        '''
        Metodo que calcula la distancia que hay entre el dato y el centroide
        param fila_X = dato actual
        param fila_Centroide = centroide actual
        '''
        distancia = sqrt(((fila_X[0] - fila_Centroide[0])** 2) + (fila_X[1] - fila_Centroide[1])** 2)
        return distancia

    def calcular_centroide_mas_cercano(self):
        '''
        Metodo que calcula cual centroide esta mas cercano al dato actual
        '''
        # se muestra los valores iniciales de los centroides
        print('Centroides iniciales:\n', self.__Centroides)     
        plt.scatter(self.__X[:, 0], self.__X[:, 1], marker = 'x')
        plt.scatter(self.__Centroides[:, 0], self.__Centroides[:, 1], marker = 'o')
        plt.show()      
        distancia_euclidiana_min = 9999
        centroide_mas_cercano = -1
        # se lleva la cuenta de las iteraciones
        iteracion_actual = 1
        # mientras que queden iteraciones
        while iteracion_actual <= self.__iteraciones:
            # por cada fila de X
            for i in range(0, self.__X.shape[0]):
                # por cada fila de centroide
                for j in range(0 , self.__Centroides.shape[0]):
                    # se calcula la listancia
                    distancia_euclidiana = self.__calcular_distancia_euclidiana(self.__X[i], self.__Centroides[j])
                    if(distancia_euclidiana < distancia_euclidiana_min):
                        # se guarda la distancia menor
                        distancia_euclidiana_min = distancia_euclidiana
                        # se guarda la posicion y el dato cercano
                        posicion_dato_mas_cercano_al_centroide = i
                        posicion_centroide_mas_cercano = j
                        centroide_mas_cercano = self.__Centroides[j]
                        dato_mas_cercano_al_centroide = self.__X[i]
                # luego de averiguar el centroide mas cercano, se actualiza la matriz W, con el dato y su respectivo centroide
                self.__actualizar_W(posicion_dato_mas_cercano_al_centroide, posicion_centroide_mas_cercano)
                # se reinicia la distancia
                distancia_euclidiana_min = 9999
            # luego de haber revisado cada dato, se actualizan los centroides
            self.__Centroides = self.__actualizar_centroides()
            print('Iteracion: ', iteracion_actual, ',Centroides Actualizados:' ,  '\n', self.__Centroides)
            plt.scatter(self.__X[:, 0], self.__X[:, 1], marker = 'x')
            plt.scatter(self.__Centroides[:, 0], self.__Centroides[:, 1], marker = 'o')
            plt.show()      
            # se suma una iteracion
            iteracion_actual += 1
        # cuando llegue a la ultima iteracion, muestra el resultado en la interfaz
        self.__mostrar_resultado_final()
        
    def __mostrar_resultado_final(self):
        '''
        Metodo que muestra la grafica del resultado de la clasificacion en la interfaz grafica
        '''
        distancia_inicial = 9999
        clase_1 = []
        clase_2 = []
        # por cada fila de X
        for dato in self.__X:
            # por cada fila de centroide
            for centroide in range(0,self.__Centroides.shape[0]):
                distancia = self.__calcular_distancia_euclidiana(dato, self.__Centroides[centroide])
                if distancia < distancia_inicial:
                    # se guarda el dato y su centroide correspondiente
                    dato_cercano = dato
                    centroide_cercano = centroide
                    distancia_inicial = distancia
            distancia_inicial = 9999
            # se clasifica el dato segun su clase
            if centroide_cercano == 0:
                clase_1 += [dato_cercano]
            else:
                clase_2 += [dato_cercano]
        # luego de tener todos los datos ya finalmente clasificados
        # se convierten en arrays
        clase_1 = np.array(clase_1)
        clase_2 = np.array(clase_2)
        # se crea la figura donde se pondra la grafica resultante
        figure = Figure(figsize=(5, 5), dpi=100)
        plot = figure.add_subplot(111)
        # graficar los datos con su respectiva clase, diferenciandolos por colores
        plot.plot(clase_1[:, 0], clase_1[:, 1],color="salmon", marker="x", linestyle="") 
        plot.plot(clase_2[:, 0],clase_2[:, 1], color="green", marker="x", linestyle="")
        canvas = FigureCanvasTkAgg(figure, self.__ventana_clasificacion)
        canvas.get_tk_widget().pack(pady=20)
        # se agrega el boton para observar la tasa de error
        boton_tasa_error = Button(self.__ventana_clasificacion, text = "Tasa de error", command=self.__tasa_de_error).place(x = 375, y = 500)

    def __actualizar_W(self, posicion_dato_mas_cercano_al_centroide, posicion_centroide_mas_cercano):
        '''
        Metodo que actualiza la matriz de pesos W, clasificando cada dato con su respectivo centroide
        param posicion_dato_mas_cercano_al_centroide: posicion del dato mas cercano al centroide
        param posicion_centroide_mas_cercano: posicion del centroide mas cercano al dato
        '''
        self.__W[posicion_dato_mas_cercano_al_centroide][posicion_centroide_mas_cercano] += 1
    
    def __sumatoria_de_W(self, columna):
        '''
        Metodo que calcula la cantidad de datos pertenecientes al centroide a actualizar
        param columna: columna actual en la matriz W que marca la pertencia del dato con el centroide
        '''
        sumatoria_W = 0
        for fila in self.__W:
            sumatoria_W += fila[columna]
        return sumatoria_W

    def __calcular_nuevo_centroide(self, columna):
        '''
        Metodo calcula el nuevo centroide
        param columna: columna actual en la matriz W que marca la pertencia del dato con el centroide
        '''
        # se calcula la cantidad de datos pertenecientes al centroide a actualizar
        sumatoria = self.__sumatoria_de_W(columna)
        resultado = 0
        fila_actual = 0
        for fila_W in self.__W:
            # se multiplica el dato con su indicador de pertenencia
            resultado += (fila_W[columna]  * self.__X[fila_actual])
            fila_actual += 1
        # se divide por la cantidad de datos pertenecientes al centroide a actualziar
        resultado /= sumatoria
        return resultado

    def __actualizar_centroides(self):
        '''
        Metodo que cuenta actualiza la lista de los centroides
        '''
        columna = 0
        for Centroide in self.__Centroides:
            self.__Centroides[columna] = self.__calcular_nuevo_centroide(columna)
            columna += 1
        return self.__Centroides
        
    def __tasa_de_error(self):
        '''
        Metodo que calcula la tasa de aciertos y de errores que posee el kmeans respecto a las etiquetas correctas.
        '''
        print('Comparar con datos artificiales')
        kmeans = KMeans(n_clusters=2, random_state=0).fit(self.__X)
        # se obtienen las etiquetas del kmeans
        etiquetas_kmeans = kmeans.labels_
        print("Resultado kmeans ", etiquetas_kmeans)
        # se clasifican las etiquetas en listas con su respectiva clase
        (etiquetas_clase_0, etiquetas_clase_1) = self.__calcular_tasa_kmeans(etiquetas_kmeans)
        (etiquetas_clase_0_correcta, etiquetas_clase_1_correcta) = self.__calcular_tasa_correcta()
        # se calculan la cantidad de etiquetas incorrectas que hay de la clase 0, obtenidos por kmeans
        incorrectas_clase_0 = abs(self.__contar_cantidad(etiquetas_clase_0) - self.__contar_cantidad(etiquetas_clase_0_correcta))
        # se calculan la cantidad de etiquetas correctas que hay de la clase 0, obtenidos por kmeans
        correctas_clase_0 = abs(self.__contar_cantidad(etiquetas_clase_0_correcta) - incorrectas_clase_0)
        # se calculan la cantidad de etiquetas incorrectas que hay de la clase 1, obtenidos por kmeans
        incorrectas_clase_1 = abs(self.__contar_cantidad(etiquetas_clase_1) - self.__contar_cantidad(etiquetas_clase_1_correcta))
        # se calculan la cantidad de etiquetas correctas que hay de la clase 1, obtenidos por kmeans
        correctas_clase_1 = abs(self.__contar_cantidad(etiquetas_clase_1_correcta) - incorrectas_clase_1)
        # se calcula el porcentaje de etiquetas correctas obtenidas por el kmeans con los generados
        tasa_de_aciertos = (((correctas_clase_0 + correctas_clase_1) / (self.__contar_cantidad(etiquetas_clase_0_correcta) + self.__contar_cantidad(etiquetas_clase_1_correcta))))*100
        # se calcula el porcentaje de etiquetas incorrectas que hay obtenidas ppor el kmeans con los generados
        tasa_de_error = 100 - tasa_de_aciertos
        # se crea el texto a mostrar en el interfaz
        label_tasa_aciertos = "Tasa de aciertos: " + str(tasa_de_aciertos) + '%'
        label_tasa_error = "Tasa de error: " + str(tasa_de_error) + '%'
        Label(self.__ventana_clasificacion, text=label_tasa_aciertos, foreground = 'white', background="#11151C", font=("Times New Roman", 20)).place(x = 375,y = 520)  
        Label(self.__ventana_clasificacion, text=label_tasa_error, foreground = 'white', background="#11151C", font=("Times New Roman", 20)).place(x = 375,y = 550)  
        print('tasa de error: ',tasa_de_error, '%' )
        print('tasa de aciertos', tasa_de_aciertos, '%')

    def __contar_cantidad(self, lista):
        '''
        Metodo que cuenta cuantos elementos tiene la lista
        param lista: lista a contar sus elementos
        '''
        cantidad = 0
        for columna in lista:
            cantidad += 1
        return cantidad
        
    def __calcular_tasa_kmeans(self, etiquetas_kmeans):
        '''
        Metodo que clasifica cada valor de las etiquetas del kmeans en una sola lista de la misma clase
        '''
        clase_0 = []
        clase_1 = []
        for elemento in etiquetas_kmeans:
            if elemento == 0:
                clase_0 += [elemento]
            else:
                clase_1 += [elemento]
        return (clase_0, clase_1)
    
    def __calcular_tasa_correcta(self):
        '''
        Metodo que clasifica cada valor de las etiquetas generadas artificalmente en una sola lista de la misma clase
        '''
        clase_0_correcta = []
        clase_1_correcta = []
        for fila in self.__etiquetas_correctas:
            for etiqueta_correcta in fila:
                if etiqueta_correcta == 0:
                    clase_0_correcta += [etiqueta_correcta]
                else:
                    clase_1_correcta += [etiqueta_correcta]
        return (clase_0_correcta, clase_1_correcta)
