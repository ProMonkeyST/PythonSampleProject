class Car:
    wheel=4
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def MakeSound(self):
        return "whooose"
luxus=Car("luxus","470")

print Car.wheel

print luxus.MakeSound()

