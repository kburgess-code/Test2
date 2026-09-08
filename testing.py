print("I'm inside testing.py")
print("I made this in the git repo")


class Car:
    def __init__(self,color,max_speed):
        self.color = color
        self.max_speed = max_speed

    def drive(self):
        print(f"{self.color} car is driving {self.max_speed} MPH")
    def brake(self):
        print(f"{self.color} car is braking")


car1 = Car("red",200)
car1.drive()
car1.brake()
#car4.brake()