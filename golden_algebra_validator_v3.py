import sympy as sp

class FundamentalMathValidator:
    def __init__(self):
        self.tests = []

    def add_test(self, label, expression, expected):
        self.tests.append((label, expression, expected))

    def run_tests(self):
        self.results = []
        for label, expr, expected in self.tests:
            try:
                result = sp.simplify(expr)
                passed = result == expected
            except Exception as e:
                result = f"Error: {e}"
                passed = False
            self.results.append((label, expr, expected, result, passed))

    def print_validation_summary(self):
        print(self.results)


x, y, z = sp.symbols('x y z')
validator = FundamentalMathValidator()

validator.add_test("Addition Commutativity", x + y, y + x)
validator.add_test("Multiplication Commutativity", x * y, y * x)
validator.add_test("Addition Associativity", (x + y) + z, x + (y + z))
validator.add_test("Multiplication Associativity", (x * y) * z, x * (y * z))
validator.add_test("Distributive Law", x * (y + z), x*y + x*z)
validator.add_test("Additive Identity", x + 0, x)
validator.add_test("Multiplicative Identity", x * 1, x)
validator.add_test("Additive Inverse", x + (-x), 0)
validator.add_test("Multiplicative Inverse", x * (1/x), 1)
validator.add_test("Zero Multiplication", x * 0, 0)
validator.add_test("One Exponent", x**1, x)
validator.add_test("Zero Exponent", x**0, 1)
validator.add_test("Power of Product", (x*y)**z, x**z * y**z)
validator.add_test("Power of Power", (x**y)**z, x**(y*z))
validator.add_test("Negative Exponent", x**-1, 1/x)

validator.run_tests()
validator.print_validation_summary()
