# A thought on the bones of the world...
from sympy import sqrt, simplify

# Define our algebraic field constants
T = (sqrt(5) - 1) / 4
J = (3 - sqrt(5)) / 4

# Let's say we have a stable 2-body orbit.
# Initial position p1 is an algebraic integer, e.g., 1
p1 = 1
# Then the stable position p2 = -T/J = -phi
p2 = -T/J

# The Law of Algebraic Conservation states that if we evolve this system,
# any point on the orbit, p1(t), will also be an algebraic integer in Q(sqrt(5)).
# For instance, a 90-degree rotation would be p1_new = I * p1.
# This breaks the law! The orbits must live entirely on the real line or be
# described by complex numbers whose real and imaginary parts are in the field.
# The true orbits are more constrained than you imagine.

print(f"Is p2 = {p2} an algebraic integer in Q(sqrt(5))? {p2.is_algebraic_exp()}")
print(f"Is p2 = {p2} an algebraic integer in Q(sqrt(5))? {p2.is_algebraic_integer()}")