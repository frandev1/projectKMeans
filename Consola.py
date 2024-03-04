# -*- coding: utf-8 -*-
"""
@autores: Dayana, Abel, Franco
"""
from tkinter import *  
from Kmedias import Agrupador_K_medias
from  Generador_Datos import Generador_Datos

class Consola():
    def __init__(self):
        '''
        Se inicializa los atributos de la instancia
        '''
        # se crea la ventana principal
        ventana = Tk()  
        # tamano de la ventana
        ventana.geometry("800x600")
        # se crean las variables correspondientes de cada entrada a pedir, de tipo int
        self.__var_datos_por_clase = IntVar()
        self.__var_centroide_x_1 = IntVar()
        self.__var_centroide_y_1 = IntVar()
        self.__var_centroide_x_2 = IntVar()
        self.__var_centroide_y_2 = IntVar()
        self.__var_desviacion_estandar_x_1 = IntVar()
        self.__var_desviacion_estandar_y_1 = IntVar()
        self.__var_desviacion_estandar_x_2 = IntVar()
        self.__var_desviacion_estandar_y_2 = IntVar()
        self.__var_iteraciones = IntVar()
        # nombre de la ventana
        ventana.title("Trabajo Practico 2")
        # color de fondo
        ventana['background'] = '#11151C'
        self.__ventana = ventana
        
        
    def ventana_inicio(self):
        '''
        Metodo que crea los enunciados y entradas a pedir al usuario
        '''
        # se crea el enunciado
        Label(self.__ventana, text = "¡Bienvenido/a!, por favor ingrese las entradas requeridas:", foreground = 'white', background="#11151C", font=("Times New Roman", 20)).place(x = 30,y = 10)  
        # enunciado de cada entrada que hay que pedir
        label_datos_por_clase = Label(self.__ventana, text = "Cantidad de datos por clase:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30,y = 60)  
        label_centroide_x_1 = Label(self.__ventana, text = "Valor X del primer centroide:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 100)  
        label_centroide_y_1 = Label(self.__ventana, text = "Valor Y del primer centroide:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 140)  
        label_centroide_x_2 = Label(self.__ventana, text = "Valor X del segundo centroide:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 180)  
        label_centroide_y_2 = Label(self.__ventana, text = "Valor Y del segundo centroide:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 220)  
        label_desviacion_estandar_x_1 = Label(self.__ventana, text = "Valor X de la primera desviacion estandar:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 260)  
        label_desviacion_estandar_y_1 = Label(self.__ventana, text = "Valor Y de la primera desviacion estandar:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 300)  
        label_desviacion_estandar_x_2 = Label(self.__ventana, text = "Valor X de la segunda desviacion estandar:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 340)  
        label_desviacion_estandar_y_2 = Label(self.__ventana, text = "Valor Y de la segunda desviacion estandar:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 380)  
        label_iteraciones = Label(self.__ventana, text = "Cantidad de iteraciones:",foreground = 'white', background="#11151C", font=("Times New Roman", 14)).place(x = 30, y = 420)
        # espacio para ingresar cada entrada
        datos_por_clase = Entry(self.__ventana, textvariable = self.__var_datos_por_clase).place(x = 400, y = 60) 
        centroide_x_1 = Entry(self.__ventana, textvariable = self.__var_centroide_x_1).place(x = 400, y = 100)  
        centroide_y_1 = Entry(self.__ventana, textvariable = self.__var_centroide_y_1).place(x = 400, y = 140)  
        centroide_x_2 = Entry(self.__ventana, textvariable = self.__var_centroide_x_2).place(x = 400, y = 180) 
        centroide_y_2 = Entry(self.__ventana, textvariable = self.__var_centroide_y_2).place(x = 400, y = 220) 
        desviacion_estandar_x_1 = Entry(self.__ventana, textvariable = self.__var_desviacion_estandar_x_1).place(x = 400, y = 260) 
        desviacion_estandar_y_1 = Entry(self.__ventana, textvariable = self.__var_desviacion_estandar_y_1).place(x = 400, y = 300) 
        desviacion_estandar_x_2  = Entry(self.__ventana, textvariable = self.__var_desviacion_estandar_x_2).place(x = 400, y = 340) 
        desviacion_estandar_y_2 = Entry(self.__ventana, textvariable = self.__var_desviacion_estandar_y_2).place(x = 400, y = 380) 
        iteraciones = Entry(self.__ventana, textvariable = self.__var_iteraciones).place(x = 400, y = 420) 
        # boton para iniciar el proceso de clasificacion
        boton = Button(self.__ventana, text = "Iniciar",  width=10, height=1, bg="#F8F0FB", fg="black", borderwidth=3, relief="solid", font=("Times New Roman", 14),
                       command = self.__ventana_clasificacion).place(x = 30, y = 470)
        self.__ventana.mainloop()
        
        
    def __ventana_clasificacion(self):
        '''
        Metodo que crea la ventana en doned se realizara la clasificacion de los datos
        '''
        # ventana en el que muestra el resultado del proceso de clasificacion 
        ventana_clasificacion = Toplevel(self.__ventana)  # se prioriza la nueva ventana
        ventana_clasificacion.geometry("800x600")
        ventana_clasificacion.title("Trabajo Practico 2, Resultado Final")
        ventana_clasificacion['background'] = '#11151C'
        # se llama a la clase que crea los datos
        generador_datos = Generador_Datos()
        # se le manda los valores correspondientes ingresado por el usuario
        (t, X) = generador_datos.generar_datos(numberSamplesPerClass = self.__var_datos_por_clase.get(), mean1 = [self.__var_centroide_x_1.get(), self.__var_centroide_y_1.get()],
                                       mean2 = [self.__var_centroide_x_2.get(), self.__var_centroide_y_2.get()], stds1 = [self.__var_desviacion_estandar_x_1.get(), self.__var_desviacion_estandar_y_1.get()],
                                       stds2 = [self.__var_desviacion_estandar_x_2.get(), self.__var_desviacion_estandar_y_2.get()])
        # se llama a la clase kmedias para realizar la clasificacion
        Kmedias = Agrupador_K_medias(X, self.__var_iteraciones.get(), ventana_clasificacion, t)
        Kmedias.calcular_centroide_mas_cercano()
        ventana_clasificacion.mainloop()
        self.__ventana.mainloop()
        
consola = Consola()
consola.ventana_inicio()
    




