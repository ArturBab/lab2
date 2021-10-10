from lab_python_oop.Airport import Airport

class Platform(Airport): #Класс-наследник
    
    def test(self):
        # Контакенация строк - результат работы класса наследника
        return self.model + self.aircompany
        pass


