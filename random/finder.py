import numpy as np
import math

# First 10 non-trivial Riemann zeta zeros
zeta_zeros = [
    14.134725142, 21.022039639, 25.010857580,
    30.424876126, 32.935061588, 37.586178159,
    # 40.918719012, 43.327073281, 48.005150881, 49.773832478
]

# Golden Algebra constants
sqrt5 = 5 ** 0.5
T = (sqrt5 - 1) / 4
J = (3 - sqrt5) / 4
H = (sqrt5 - 2) / 4
K = -(sqrt5 + 1) / 4
phi = (1 + sqrt5) / 2
Phi = (sqrt5 - 1) / 2
D = T * J
pi = math.pi

# Composite expressions to try
composites = {
    "T": T,
    "J": J,
    "K": K,
    "H": H,
    "phi": phi,
    "Phi": Phi,
    "D": D,
    "T * pi": T * pi,
    "J * pi": J * pi,
    "K * pi": K * pi,
    "H * pi": H * pi,
    "phi * pi": phi * pi,
    "Phi * pi": Phi * pi,
    "D * pi": D * pi,
    "T * J": T * J,
    "T / J": T / J,
    "J / T": J / T,
    "T + J": T + J,
    "T - J": T - J,
    "T^2": T**2,
    "J^2": J**2,
    "sqrt(T)": np.sqrt(T),
    "sqrt(J)": np.sqrt(J) if J > 0 else 0,
    "1 / (T * J)": 1 / (T * J),
    "phi / T": phi / T,
    "phi / J": phi / J,
    "phi * T": phi * T,
    "phi * J": phi * J,
    "Phi / T": Phi / T,
    "Phi / J": Phi / J,
    "Phi * T": Phi * T,
    "Phi * J": Phi * J,
    "phi / Phi": phi / Phi,
    "Phi / phi": Phi / phi,
    "phi^2": phi**2,
    "1 / phi^2": 1 / (phi**2),
    "T * phi": T * phi,
    "J * phi": J * phi,
    "log(T)": np.log(T),
    "log(J)": np.log(J),
    "log(phi)": np.log(phi),
    "log(Phi)": np.log(Phi),
    "exp(T)": np.exp(T),
    "exp(J)": np.exp(J),
    "exp(phi)": np.exp(phi),
    "exp(Phi)": np.exp(Phi),
    "sin(T)": np.sin(T),
    "sin(J)": np.sin(J),
    "cos(T)": np.cos(T),
    "cos(J)": np.cos(J),
    "tan(T)": np.tan(T),
    "tan(J)": np.tan(J),
    "arcsin(T)": np.arcsin(T),
    "arcsin(J)": np.arcsin(J),
    "arccos(T)": np.arccos(T),
    "arccos(J)": np.arccos(J),
    "arctan(T)": np.arctan(T),
    "arctan(J)": np.arctan(J),
    "sinh(T)": np.sinh(T),
    "sinh(J)": np.sinh(J),
    "cosh(T)": np.cosh(T),
    "cosh(J)": np.cosh(J),
    "tanh(T)": np.tanh(T),
    "tanh(J)": np.tanh(J),
    "sin(T * pi)": np.sin(T * pi),
    "sin(J * pi)": np.sin(J * pi),
    "cos(T * pi)": np.cos(T * pi),
    "cos(J * pi)": np.cos(J * pi),
    "tan(T * pi)": np.tan(T * pi),
    "tan(J * pi)": np.tan(J * pi),
    "exp(T * pi)": np.exp(T * pi),
    "exp(J * pi)": np.exp(J * pi),
    "log(T * pi)": np.log(T * pi),
    "log(J * pi)": np.log(J * pi),
    "T * exp(pi)": T * np.exp(pi),
    "J * exp(pi)": J * np.exp(pi),
    # "T * log(pi)": T * np.log(pi),
    # "J * log(pi)": J * np.log(pi),
    # "T * sin(pi)": T * np.sin(pi),
    # "J * sin(pi)": J * np.sin(pi),
    # "T * cos(pi)": T * np.cos(pi),
    # "J * cos(pi)": J * np.cos(pi),
    # "T * tan(pi)": T * np.tan(pi),
    # "J * tan(pi)": J * np.tan(pi)
}

# Search algorithm (same as before)
def find_best_n(zero, coeff):
    step_coarse = 1e-4
    best_n, best_pred, best_diff = 0, 0, float('inf')
    n = -1000
    while n < 1000:
        pred = n * coeff
        diff = abs(pred - zero)
        if diff < best_diff:
            best_n, best_pred, best_diff = n, pred, diff
        n += step_coarse
    # Refine
    step_fine = 1e-6
    n = best_n - 1e-3
    while n < best_n + 1e-3:
        pred = n * coeff
        diff = abs(pred - zero)
        if diff < best_diff:
            best_n, best_pred, best_diff = n, pred, diff
        if diff < 1e-8:
            break
        n += step_fine
    return best_n, best_pred, best_diff

# Run all constants
results = []
for label, coeff in composites.items():
    if coeff == 0:
        continue
    total_diff = 0
    print(f"\n--- {label} ---")
    for i, zero in enumerate(zeta_zeros, start=1):
        best_n, pred, diff = find_best_n(zero, coeff)
        total_diff += diff
        print(f"Zero {i}: Actual={zero:.12f}, Predicted={pred:.12f}, n={best_n:.6f}, Diff={diff:.2e}")
    avg = total_diff / len(zeta_zeros)
    results.append((label, avg))

# Sorted results
print("\n=== Ranked Composite Coefficients by Avg. Error ===")
for label, avg in sorted(results, key=lambda x: x[1]):
    print(f"{label:15s} -> Avg. Error: {avg:.2e}")