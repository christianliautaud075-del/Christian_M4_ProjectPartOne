"""
Christian_M6_WritingClassesandIdentifyingCommonBugs

This file has the three code samples.
I added comments to show which one works and what is wrong with the others.
"""


# Sample Code 1
# This one is correct.
# The class is written the right way, the objects are created outside the class,
# and the print statements are also in the right place.

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# Create instances of Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Jeep", "Wrangler", 2020)

# Print the car objects
print(car1)  # Output: 2022 Toyota Camry
print(car2)  # Output: 2020 Jeep Wrangler


# --------------------------------------------------
# Sample Code 2
# This one has an error.
# car1 and car2 are indented inside the __str__ method, so they are stuck inside that method.
# Because of that, Python will not know what car1 and car2 are when it gets to the print statements.
# This would cause a NameError.

"""
class Car:

  def __init__(self, make, model, year):

    self.make = make

    self.model = model

    self.year = year

  def __str__(self):

      return f"{self.year} {self.make} {self.model}"

      # Create instance of Car
      car1 = Car("Toyota", "Camry", 2022)
      car2 = Car("Jeep", "Wrangler", 2020)

  # Print the car objects
print(car1)  # NameError
print(car2)  # NameError
"""


# --------------------------------------------------
# Sample Code 3
# This one also has an error.
# The print statements are indented wrong, even though they are not inside a method or block.
# Python would give an IndentationError because of that.

"""
class Car:

  def __init__(self, make, model, year):

    self.make = make

    self.model = model

    self.year = year

  def __str__(self):

      return f"{self.year} {self.make} {self.model}"

  # Create instance of Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Jeep", "Wrangler", 2020)

  # Print the car objects
  print(car1)  # IndentationError
  print(car2)  # IndentationError
"""
