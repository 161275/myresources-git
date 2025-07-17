class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        print(self.name)
        super().__init__(type)
        super().start()

class Fortuner(Toyota):
    def __init__(self, type)
    self.type = type


car1 = Toyota("fortuner", "diesel")
car2 = Toyota("Glanza", "petrol")
car1.start()
car1.stop()
print(car2.type)