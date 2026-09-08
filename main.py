class Dog:
    def __init__(self,breed,name,):
        self.breed = breed
        self.name = name

    def bark(self,name):
        print(f"{name} Barks!")

#START#
dog_list = []
print("Welcome to the Dog House!\n")
while True:
    response = input("Would you like to add a dog? (y/n): ")
    if response.casefold() == "y":
        breed = input("What is the dogs breed?: ")
        name = input("What the dogs name?: ")
        dog_list.append(Dog(breed,name))
    elif response.casefold() == "n":
        break
    else:
        print("INVALID INPUT")

print("\nDogs in the Dog House:")
#print(dog_list)
for dog in dog_list:    #for loops in Python -> the 'dog' word here is used as an iterator
    dog.bark(dog.name)
    print("BREED:",dog.breed,"\nNAME:",dog.name,end="\n\n")


