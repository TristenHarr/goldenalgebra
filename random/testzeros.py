import numpy as np

# First 10 non-trivial Riemann zeta zeros
zeta_zeros = [
    14.134725142, 21.022039639, 25.010857580, 30.424876126, 32.935061588,
    37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478
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

# Composite expressions to try
composites = {
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
    "H": H
}

# Search algorithm (same as before)
def find_best_n(zero, coeff):
    step_coarse = 1e-4
    best_n, best_pred, best_diff = 0, 0, float('inf')
    n = 0
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

