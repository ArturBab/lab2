from lab_python_oop.Airport import Airport
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
from lab_python_oop.Triangle import Triangle


def main():

    print("Лабораторная работа 2, работа с классами:")
    print("Проверка работы собственного класса Аэропорт:")
    print('')

    print("           AIRPORT SHEREMETYEVO: FLIGHT DATA                ")
    
    # Создание объектов класса Airport и вывод на консоль

    plane_one = Airport("Airbus A321", "Aeroflot", "Erevan - Moscow", 148)
    print("   ---", plane_one.aircompany, "---", 
          plane_one.model, "---", 
          plane_one.destination, "---", 
          plane_one.flight_num, "---   ")
    # Передаем другой параметр, чтобы сообщить классу, какой номер самолета мы создаем
    # Вызываем каждый метод для каждого экземпляра
    print(plane_one.takeoff())

    print('')

    plane_two = Airport("Boeing 737-800", "Pobeda", "Moscow - Saratov", 272)
    print("   ---", plane_two.aircompany, "---", 
         plane_two.model, "---",
         plane_two.destination, "---", 
         plane_two.flight_num, "---   ")
    print(plane_two.landing())

    print('')

    plane_three = Airport("Airbus A350-900", "Aeroflot", "Moscow - Saint-Petersburg", 687)
    print("   ---", plane_three.aircompany, "---", 
          plane_three.model, "---", 
          plane_three.destination, "---", 
          plane_three.flight_num, "---   ")
    print(plane_three.takeoff())

    print('')

    print("   ФИГУРЫ И ИХ ПАРАМЕТРЫ:   ")

    print('')

    r = Rectangle("Синий", 3, 2)
    print(r)

    print('')

    c = Circle("Фиолетовый", 8)
    print(c)

    print('')

    s = Square("Зеленый", 13)
    print(s)

    print('')

    obj1 = Rectangle("Красный", 11, 12)
    print(obj1)

    print('')

    t = Triangle("Черный", 13, 14, 15)
    print(t)

    print('')

if __name__ == "__main__":
    main()
