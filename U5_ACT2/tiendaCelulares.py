import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Creamos la clase TelefonoCelular con los siguientes atrbutos privados: marca, modelo, color, capacidad de almacenamiento, precio, plan_renta, seguro, precio_total
class TelefonoCelular:
    def __init__(self, marca, modelo, color, capacidad_almacenamiento, precio, plan_renta, seguro):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__capacidad_almacenamiento = capacidad_almacenamiento
        self.__precio = precio
        self.__plan_renta = plan_renta
        self.__seguro = seguro
        self.__precio_total = precio + plan_renta + seguro

   # GETTERS Y SETTERS

   # marca
    @property # getter atributo marca
    def marca(self):
        return self.__marca

    @marca.setter # setter atributo marca
    def marca(self, value):
        self.__marca = value

    # modelo
    @property # getter atributo modelo
    def modelo(self):
        return self.__modelo

    @modelo.setter # setter atributo modelo
    def modelo(self, value):
        self.__modelo = value

    # color
    @property # getter atributo color
    def color(self):
        return self.__color

    @color.setter # setter atributo color
    def color(self, value):
        self.__color = value

    # capacidad_almacenamiento
    @property # getter atributo capacidad_almacenamiento
    def capacidad_almacenamiento(self):
        return self.__capacidad_almacenamiento

    @capacidad_almacenamiento.setter # setter atributo capacidad_almacenamiento
    def capacidad_almacenamiento(self, value):
        self.__capacidad_almacenamiento = value

    # precio
    @property # getter atributo precio
    def precio(self):
        return self.__precio

    @precio.setter # setter atributo precio
    def precio(self, value):
        self.__precio = value

    # plan_renta
    @property # getter atributo plan_renta
    def plan_renta(self):
        return self.__plan_renta

    @plan_renta.setter # setter atributo plan_renta
    def plan_renta(self, value):
        self.__plan_renta = value
    
    # seguro
    @property # getter atributo seguro
    def seguro(self):
        return self.__seguro

    @seguro.setter # setter atributo seguro
    def seguro(self, value):
        self.__seguro = value

    # precio_total
    @property # getter atributo precio_total
    def precio_total(self):
        return self.__precio_total

    @precio_total.setter # setter atributo precio_total
    def precio_total(self, value):
        self.__precio_total = value

