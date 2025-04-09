import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from Excel
df = pd.read_excel('testxy.xlsx')  # Replace with your file name
x = df['x'].values
y = df['y'].values

# Fit a curve (e.g., 2nd degree polynomial)
degree = 100
coeffs = np.polyfit(x, y, degree)
poly_eq = np.poly1d(coeffs)

# Generate x values for the smooth curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = poly_eq(x_fit)

# Plot
plt.scatter(x, y, label='Data Points', s=5)
plt.plot(x_fit, y_fit, color='red', label=f'Best Fit Curve (degree {degree})')
plt.xlabel('INPUT ANGLE(θ) (deg(°))')
plt.ylabel('OUTPUT ANGLE(α) (deg(°))')
plt.legend()
plt.title('INPUT ANGLE(θ) VS OUTPUT ANGLE(α)')
plt.xticks(np.arange(0, 361, 30))
plt.grid(plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5, alpha=0.7))
plt.minorticks_on()
plt.grid(plt.grid(which='minor', color='gray', linestyle='--', linewidth=0.2, alpha=0.8))
plt.xlim(0, 359)
plt.ylim(30, 140)
plt.show()
