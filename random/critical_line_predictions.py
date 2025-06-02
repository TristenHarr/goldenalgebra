import matplotlib

matplotlib.use('AGG')  # Set the backend to 'AGG'

import matplotlib.pyplot as plt


def plot_zeta_zeros(num_zeros):
    # Precomputed list of non-trivial zeros of the Riemann zeta function
    zeros = [
        14.134725142, 21.022039639, 25.010857580, 30.424876126, 32.935061588,
        37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478,
        52.970321478, 56.446247697, 59.347044003, 60.831778525, 65.112544048,
        67.079810529, 69.546401711, 72.067157674, 75.704690699, 77.144840069,
        79.337375020, 82.910380854, 84.735492981, 87.425274613, 88.809111208,
        92.491899271, 94.651344041, 95.870634228, 98.831194218, 101.317851006,
        103.725538040, 105.446623052, 107.168611184, 111.029535543, 111.874659177,
        114.320220915, 116.226680321, 118.790782866, 121.370125002, 122.946829294,
        124.256818554, 127.516683880, 129.578704200, 131.087688531, 133.497737203,
        134.756509753, 138.116042055, 139.736208952, 141.123707404, 143.111845808,
        146.000982487, 147.422765343, 150.053520421, 150.925257612, 153.024693811,
        156.112909294, 157.597591818, 158.849988171, 161.188964138, 163.030709687,
        165.537069188, 167.184439978, 169.094515416, 169.911976479, 173.411536520,
        174.754191523, 176.441434298, 178.377407776, 179.916484020, 182.207078484,
        184.874467848, 185.598783678, 187.228922584, 189.416158656, 192.026656361,
        193.079726604, 195.265396680, 196.876481841, 198.015309676, 201.264751944
    ]

    # Extract the specified number of zeros
    zeros = zeros[:num_zeros]

    # Generate Golden Algebra predictions for the same number of zeros
    T = (5 ** 0.5 - 1) / 4
    J = (3 - 5 ** 0.5) / 4

    predictions = [n * (T + J) / 2 for n in range(1, len(zeros) + 1)]

    # Plot the actual zeta zeros and Golden Algebra predictions
    plt.figure(figsize=(12, 8))
    plt.scatter(range(1, len(zeros) + 1), zeros, color='blue', label='Actual Zeta Zeros')
    plt.scatter(range(1, len(predictions) + 1), predictions, color='green', label='Golden Algebra Predictions')

    # Plot the ideal alignment line
    plt.plot(range(1, len(zeros) + 1), zeros, color='red', linestyle='--', label='Ideal Alignment')

    # Add labels and legend
    plt.xlabel('Zero Index')
    plt.ylabel('Value')
    plt.title(f'Actual vs Predicted Zeta Zeros (First {len(zeros)})')
    plt.legend()

    # Save the plot to a file
    plt.tight_layout()
    plt.savefig('zeta_zeros_actual_predicted_alignment.png')

    print("Plot saved as 'zeta_zeros_actual_predicted_alignment.png'")


# Test the function with the first 200 zeros
plot_zeta_zeros(200)