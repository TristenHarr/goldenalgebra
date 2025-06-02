import math

def predicted_zero(n):
    """
    Predicts the n-th non-trivial zero of the Riemann zeta function
    using the Golden Algebra constant Phi and the mathematical constant pi.
    """
    phi = (math.sqrt(5) - 1) / 2
    pi = math.pi
    return 2 * n * (phi * pi)

# Test the formula for the first 10 non-trivial zeta zeros
for n in range(1, 11):
    predicted = predicted_zero(n)
    print(f"Predicted {n}-th non-trivial zero: {predicted:.12f}")