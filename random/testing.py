import numpy as np

# First 10 non-trivial Riemann zeta zeros
zeta_zeros = [
    14.134725142, 21.022039639, 25.010857580,
    # 30.424876126, 32.935061588, 37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478
]

# Golden Algebra constants
T = (5 ** 0.5 - 1) / 4
J = (3 - 5 ** 0.5) / 4
H = (5 ** 0.5 - 2) / 4
K = -(5 ** 0.5 + 1) / 4
phi = (1 + 5 ** 0.5) / 2
Phi = (5**0.5 - 1) / 2
# coeff = (T)*np.pi
coeff = T*J*K*np.pi
# coeff = (T * J)

# Faster approximation
def find_best_n_fast(target_zero):
    # Coarse search
    step_size_coarse = 1e-4
    min_n = -1000
    max_n = 1000

    best_n = 0
    best_diff = float('inf')
    best_pred = 0

    n = min_n
    while n < max_n:
        pred = n * coeff
        diff = abs(pred - target_zero)
        if diff < best_diff:
            best_diff = diff
            best_n = n
            best_pred = pred
        n += step_size_coarse

    # Fine search (faster)
    refined_step = 1e-6
    refined_min_n = best_n - 1e-3
    refined_max_n = best_n + 1e-3

    n = refined_min_n
    while n < refined_max_n:
        pred = n * coeff
        diff = abs(pred - target_zero)
        if diff < best_diff:
            best_diff = diff
            best_n = n
            best_pred = pred
        if diff < 1e-8:  # relax precision tolerance
            break
        n += refined_step

    return best_n, best_pred, best_diff


# Run for all 10 zeros
for i, zero in enumerate(zeta_zeros, start=1):
    best_n, predicted, diff = find_best_n_fast(zero)
    print(f"Zero {i}:")
    print(f"  Actual:   {zero}")
    print(f"  Predicted:{predicted}")
    print(f"  Best n:   {best_n}")
    print(f"  Diff:     {diff:.2e}")
    print()
