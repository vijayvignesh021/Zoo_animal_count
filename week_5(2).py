#ANIMAL IN ZOO PROJECT
#IN GOOGLE PYTHON 
class Animal:
    name = ""
   # category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category
      
class Turtle(Animal):
    category = "reptile"

print(Turtle.category)

class Snake(Turtle):
    pass

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle")
snake = Snake("Snake") 

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile"))
print(zoo.current_animals)