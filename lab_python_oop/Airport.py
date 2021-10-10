import sys
import math
import django #Еще одно виртуальное окружение со своим пакетом

#Виртуальное окружение создано: 
#Виртуальное окружение создается в "C:\Users\79626\source\repos\lab_2\lab_2\env".
#Виртуальное окружение успешно создано в "C:\Users\79626\source\repos\lab_2\lab_2\env".
#Внешний пакет Django установлен с использованием pip.

class Airport(object):
    """строка документа"""

    def __init__(self, model, aircompany, destination, flight_num):
        """конструктор"""
        self.model = model # self - способ сообщения между экземплярами, описания любого обьекта
        self.aircompany = aircompany
        self.destination = destination
        self.flight_num = flight_num

    def takeoff(self):
        """
        МЕТОД

        Взлет
        """
        return "Самолет успешно взлетел!"

    def landing(self):
        """
        МЕТОД

        Посадка
        """
        return "Самолет успешно приземлился!"

        pass



