import math

# Base class for shapes
class Area:
    def __init__(self):
        # Constructor for the base class, no specific initialization here
        pass

    def calculate_area(self):
        # This method should be implemented by subclasses
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Circle
class Circle(Area):
    def __init__(self, radius):
        # Initialize the base class
        super().__init__()
        # Validate the radius
        if radius <= 0:
            raise ValueError("Radius must be positive")
        # Set the radius of the circle
        self.radius = radius

    def calculate_area(self):
        # Calculate and return the area of the circle
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Area):
    def __init__(self, length, width):
        # Initialize the base class
        super().__init__()
        # Validate the length and width
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        # Set the length and width of the rectangle
        self.length = length
        self.width = width

    def calculate_area(self):
        # Calculate and return the area of the rectangle
        return self.length * self.width

# Subclass for Square, which inherits from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        # Initialize the base class with side as both length and width
        super().__init__(side, side)
        # Validate the side length
        if side <= 0:
            raise ValueError("Side length must be positive")

# Main function to demonstrate the usage of the classes
def main():
    try:
        # Create a Circle instance with radius 5
        circle = Circle(5)
        # Print the area of the circle
        print(f"Area of the circle: {circle.calculate_area()}")

        # Create a Rectangle instance with length 4 and width 6
        rectangle = Rectangle(4, 6)
        # Print the area of the rectangle
        print(f"Area of the rectangle: {rectangle.calculate_area()}")

        # Create a Square instance with side 3
        square = Square(3)
        # Print the area of the square
        print(f"Area of the square: {square.calculate_area()}")

    except ValueError as e:
        # Print any value errors that occur during initialization
        print(e)

# Run the main function if this file is executed as a script
if __name__ == "__main__":
    main()
