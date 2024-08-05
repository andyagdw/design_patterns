"""Examples of design patterns"""

import copy


# Singleton design pattern
class Singleton():
    """
    Represents the singleton design pattern
    (creational)

    Ensures that one instance of a class can ever be created

    Overrides the static __new method__ to control the creation of
    instances. It checks if an instance already exists (if cls.instance
    is None). If there isn't an instance, it will create a new instance.
    Otherwise, it will return the already created instance.
    """

    # Will hold the single instance of the class. Only for internal use
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Prototype design pattern (creational)
# Prototype
class Shape():
    """
    Represents the prototype design pattern

    Allows objects to be cloned, providing a way to create
    new instances by cloning existing ones rather than creating new
    ones from scratch

    It defines the interface for cloning itself
    """
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def clone(self):
        """Create a deep copy of the instance"""
        return copy.deepcopy(self)


class Circle(Shape):
    """
    The concrete prototype
    It is a concrete implementation of the Shape class
    """
    def __init__(self, radius):
        super().__init__("Circle")
        self._radius = radius

    @property
    def radius(self):
        """Get the radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        """Set a new radius for the circle"""
        self._radius = new_radius


# Builder design pattern (creational)
class PersonBuilder():
    """
    Represents the builder design pattern

    Responsible for constructing a Person object
    """
    def __init__(self):
        self.person = Person()

    def reset(self):
        """Reset the Person Builder internal state"""
        self.person = Person()

    def set_name(self, name):
        """Sets the name of the person being created"""
        self.person.name = name

    def set_age(self, age):
        """Sets the age of the person being created"""
        self.person.age = age

    def set_gender(self, gender):
        """Sets the gender of the person being created"""
        self.person.gender = gender

    def set_ethnicity(self, ethnicity):
        """Sets the ethnicity of the person being created"""
        self.person.ethnicity = ethnicity

    def build(self):
        """To retrieve the constructed person object"""
        return self.person


class Person():
    """The thing being constructed"""
    def __init__(self,
                 name=None,
                 age=None,
                 gender=None,
                 ethnicity=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.ethnicity = ethnicity

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Ethnicity: {self.ethnicity}")


# Factory design pattern (creational)

if __name__ == "__main__":

    # Singleton
    singleton_one = Singleton()
    singleton_two = Singleton()
    # This will return 'True' as they both refer to the same instance
    print(f'{singleton_one is singleton_two = }\n')

    # Prototype
    # Create a prototype object
    circle_one = Circle(5)

    # Clone the prototype to create a new object
    circle_two = circle_one.clone()

    # Will return 'False' as they are different objects
    print(f'{circle_one is circle_two = }')

    # Verify that they have the same attributes
    print(f'{circle_one.shape_type = }', f'{circle_one.radius = }')
    print(f'{circle_two.shape_type = }', f'{circle_two.radius = }')

    # Verify that changes to one circle does not affect the other
    circle_two.radius = 10
    print(f'{circle_one.radius = }', f'{circle_two.radius = }\n')

    # Builder
    person_builder = PersonBuilder()

    person_builder.set_name("John")
    person_builder.set_age(30)
    person_builder.set_gender("Male")

    # Construct the Person object with the set attributes
    person_one = person_builder.build()  # Assign it to person_one
    print(person_one)
    # Clear PersonBuilder internal state to create new object
    person_builder.reset()
