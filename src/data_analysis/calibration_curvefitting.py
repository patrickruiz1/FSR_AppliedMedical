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

def calibration_curvefitting(FSR_dir, file_name, graph_title = 'Graph'):

    # File and directory information
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'calibration', file_name)

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

    # Generate fitted curve
    x_fit = np.linspace(min(x_data), max(x_data), 3000)
    y_fit = power_function(x_fit, a_fit, b_fit)
    z_fit = (1/y_fit)

    # Calculate confidence intervals based on x_fit
    alpha = 0.05
    n = len(x_data)
    df_resid = n - len(popt)
    t = np.abs(np.random.standard_t(df_resid, size=len(x_fit)))
    s_err = np.sqrt(np.sum((y_data - power_function(x_data, a_fit, b_fit)) ** 2) / df_resid)
    CI = t * s_err * np.sqrt(1/n + (x_fit - np.mean(x_data))**2 / np.sum((x_data - np.mean(x_data))**2))

    # Calculate R-squared
    y_pred = power_function(x_data, a_fit, b_fit)
    SSR = np.sum((y_pred - np.mean(y_data))**2)  # Regression sum of squares
    SST = np.sum((y_data - np.mean(y_data))**2)  # Total sum of squares
    r_squared = SSR / SST

    # Calculate Mean Squared Error (MSE)
    mse = np.mean((y_data - y_pred)**2)

    # Calculate residuals
    residuals = y_data - y_pred

    # Plotting
    fig = plt.figure(figsize = (11,7))
    ax1 = fig.add_subplot(111)
    lns1 = ax1.scatter(x_data, y_data, c = 'black', marker = '.', label = 'Original Data')
    lns2 = ax1.plot(x_fit, y_fit, c = 'blue', label = 'Fitted Curve')
    ax2 = ax1.twinx()
    lns3 = ax2.plot(x_fit, z_fit, c = 'orange', label = 'Conductance')

    # Add labels, title, legend, and grid
    plt.xlabel('Force (lbf)')
    ax1.set_ylabel(r'Resistance ($\Omega$)')
    ax1.set_xlabel('Force (lbf)')
    ax2.set_ylabel(r'Conductance (S)')
    plt.title(graph_title)
    lns = [lns1] + lns2 + lns3
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc = 'upper center')
    plt.grid(True)

    # Show plot
    plt.show()

    # Print values for LaTex document 
    print("Fitted Function Equation:")
    print(f"The fitted function equation is: $y = {a_fit:.5f} \\times x^{{{b_fit:.5f}}}$") 

    print(f"\nParameter Estimates and Standard Errors:")
    print(f"The value of $A$ is {a_fit:.5f} with standard error of {SE_A:.5f}.")
    print(f"The value of $B$ is {b_fit:.5f} with standard error of {SE_B:.5f}.")

    print("\nGoodness-of-Fit Metrics:")
    print(f"Coefficient of Determination ($R^2$): {r_squared:.5f}")
    print(f"Mean Squared Error (MSE): {mse:.5f}")

    print("\nResiduals:")
    # np.set_printoptions(threshold=np.inf)
    print(residuals)

# os.system('clear')
os.system('cls')
FSR_dir = 'FSR_S1'
file_name = 'FSR_S1_Calibration_PostCond_Swag.csv'
graph_title = 'FSR_S1 - Calibration Curve - Post Conditioning'
calibration_curvefitting(FSR_dir, file_name, graph_title)
