from sys import getsizeof


class Car:
    def __init__(self, car_speed, car_color, car_name, car_ispolice):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.ispolice = car_ispolice

    def go(self):
        print('Машина начала движение')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print('Текущая скорость автомобиля:', self.speed)

class ElectricCar(Car):
    __slots__ = ['speed', 'color', 'name', 'ispolice']

    def __init__(self):
        pass

    # def __init__(self, speed_param, color_param, name, ispolice):
    #     self.speed_param = speed_param
    #     self.color_param = color_param
    #     self.name = name
    #     self.ispolice = ispolice
    #
    # def go(self):
    #     print('Машина начала движение')
    #
    # def stop(self):
    #     print('Машина остановилась')
    #
    # def turn(self, direction):
    #     print('Машина повернула', direction)
    #
    # def show_speed(self):
    #     print('Текущая скорость автомобиля:', self.speed_param)


car_objet = Car(car_speed=60, car_color='red', car_name='Honda', car_ispolice=False)
print(car_objet.__dict__)
print(getsizeof(car_objet))
electric_car_object = ElectricCar()
# electric_car_object = ElectricCar(60, 'red', 'Honda', False)
print(electric_car_object.__slots__)
print(getsizeof(electric_car_object))

# по какой-то причине использование __slots__, измеряя память с помощью getsizeof, лишь увеличивает память