import os 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

# Define the power function to be fitted
def power_function(x, a, b):
    """
    Power function: y = a * x^b
    Args:
        x (float): Independent variable.
        a (float): Scale parameter.
        b (float): Exponent parameter.
    Returns:
        float: Calculated y value.
    """
    return a * np.power(x, b)


def calibration_curvefitting(FSR_dir, file_name):

    # File and directory information
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed', file_name)

    # Read data from CSV file
    df = pd.read_csv(file_path, index_col=False)
    x_data = np.array(df['Load (lbf)'].values)
    y_data = np.array(df['Resistance (Ohms)'].values)

    # Fit the power function to the data
    popt, pcov = curve_fit(power_function, x_data, y_data)
    a_fit, b_fit = popt

    # Calculate standard errors
    SE = np.sqrt(np.diag(pcov))
    SE_A = SE[0]
    SE_B = SE[1]

    # Print parameter estimates and standard errors
    print("Parameter Estimates and Standard Errors:")
    print(f"The value of A is {a_fit:.5f} with standard error of {SE_A:.5f}.")
    print(f"The value of B is {b_fit:.5f} with standard error of {SE_B:.5f}.")

    # Generate fitted curve
    x_fit = np.linspace(min(x_data), max(x_data), 3000)
    y_fit = power_function(x_fit, a_fit, b_fit)

    # Calculate confidence intervals based on x_fit
    alpha = 0.05
    n = len(x_data)
    df_resid = n - len(popt)
    t = np.abs(np.random.standard_t(df_resid, size=len(x_fit)))
    s_err = np.sqrt(np.sum((y_data - power_function(x_data, a_fit, b_fit)) ** 2) / df_resid)
    CI = t * s_err * np.sqrt(1/n + (x_fit - np.mean(x_data))**2 / np.sum((x_data - np.mean(x_data))**2))

    # Print values for LaTeX document
    print("\nValues for LaTeX Document:")
    print(f"\\textbf{{Parameter Estimates and Standard Errors:}}")
    print(f"The value of $A$ is {a_fit:.5f} with standard error of {SE_A:.5f}.")
    print(f"The value of $B$ is {b_fit:.5f} with standard error of {SE_B:.5f}.")

    # Calculate R-squared
    y_pred = power_function(x_data, a_fit, b_fit)
    SSR = np.sum((y_pred - np.mean(y_data))**2)  # Regression sum of squares
    SST = np.sum((y_data - np.mean(y_data))**2)  # Total sum of squares
    r_squared = SSR / SST

    # Calculate Mean Squared Error (MSE)
    mse = np.mean((y_data - y_pred)**2)

    print("\n\\textbf{Goodness-of-Fit Metrics:}")
    print(f"Coefficient of Determination ($R^2$): {r_squared:.5f}")
    print(f"Mean Squared Error (MSE): {mse:.5f}")

    # Calculate residuals
    residuals = y_data - y_pred

    print("\n\\textbf{Residuals:}")
    print(residuals)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, c='black', marker=',', label='Original Data')
    plt.plot(x_fit, y_fit, c='blue', label='Fitted Curve')
    plt.fill_between(x_fit, y_fit - 2*CI, y_fit + 2*CI, color='black', alpha=.69, label='95% Confidence Interval')

    # Add equation text to the plot
    equation_text = f'$y = {a_fit:.2f} \cdot x^{{{b_fit:.2f}}}$'
    plt.text(max(x_data)*0.6, max(y_data)*0.7, equation_text, fontsize=12, color='black')

    # Add labels, title, legend, and grid
    plt.xlabel('Force (lbf)')
    plt.ylabel('Resistance (Ohms)')
    plt.title(file_name[:-4])
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.show()

os.system('cls')
FSR_dir = 'FSR_S1'
file_name = 'FSR_S1_Calibration_PreCond.csv'
calibration_curvefitting(FSR_dir, file_name)
