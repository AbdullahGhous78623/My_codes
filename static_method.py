class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Calling static methods
result1 = MathOperations.add(5, 3)          # 8
result2 = MathOperations.multiply(4, 6)     # 24

print(result1)
print(result2)
