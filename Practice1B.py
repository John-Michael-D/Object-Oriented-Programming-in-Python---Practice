class Car:
    def __init__(self, model, year, color, for_sale): #This is a constructor method. We use this to construct objects. This is a dunder (double underscore) method.
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}!")

    def stop(self):
        print(f"You stop the {self.color} {self.model}!")

    def describe(self):
        print(f"Here are the details of your {self.model}: {self.year}, {self.color}, {self.year}.")