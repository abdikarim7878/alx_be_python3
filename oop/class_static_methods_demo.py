class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: does not use class or instance data"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: uses the class attribute"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
