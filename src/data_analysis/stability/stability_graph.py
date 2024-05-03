# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def scatter_plot_errors(FSR_dir):
#     file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = os.listdir(file_path)
#     sorted_files_list = sorted(files)

#     for file in sorted_files_list:
#         file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
#         try:
#             df = pd.read_csv(file_path, encoding='latin-1')  # Specify encoding here
#             print(df.head())  # Print first few rows of DataFrame to check its contents

#             # Check if the required columns exist
#             if 'Force (lbf)' not in df.columns or 'Percent Error (%)' not in df.columns:
#                 print(f"Error: Required columns not found in file {file}. Skipping...")
#                 continue

#             # Plotting
#             plt.figure(figsize=(10, 6))
#             plt.scatter(df['Force (lbf)'], df['Percent Error (%)'], label=file)
#             plt.xlabel('Force (lbf)')
#             plt.ylabel('Percent Error (%)')
#             plt.title('Percent Error vs. Force Applied')
#             plt.legend()
#             plt.grid(True)
#             plt.show()

#         except Exception as e:
#             print(f"Error occurred while processing file {file}: {e}")

# FSR_dir = 'FSR_S1'
# scatter_plot_errors(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_percent_error_histograms(FSR_dir):
#     file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = os.listdir(file_path)
#     sorted_files_list = sorted(files)

#     for file in sorted_files_list:
#         file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
#         df = pd.read_csv(file_path, encoding='latin-1')  # Specify encoding here
#         if 'Percent Error (%)' in df.columns:  # Check if the percent error column exists
#             plt.figure(figsize=(8, 6))
#             plt.hist(df['Percent Error (%)'], bins=20, color='skyblue', edgecolor='black')
#             plt.xlabel('Percent Error (%)')
#             plt.ylabel('Frequency')
#             plt.title(f'Percent Error Histogram for {file}')
#             plt.grid(True)
#             plt.show()

# FSR_dir = 'FSR_S1'
# plot_percent_error_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_percent_error_histograms_combined(FSR_dir):
#     file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = os.listdir(file_path)
#     sorted_files_list = sorted(files)

#     num_files = len(sorted_files_list)
#     num_rows = (num_files + 1) // 2  # Determine number of rows for subplots

#     fig, axes = plt.subplots(num_rows, 2, figsize=(12, 6 * num_rows))

#     for idx, file in enumerate(sorted_files_list):
#         file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
#         df = pd.read_csv(file_path, encoding='latin-1')  # Specify encoding here
#         if 'Percent Error (%)' in df.columns:  # Check if the percent error column exists
#             row = idx // 2
#             col = idx % 2
#             ax = axes[row, col] if num_rows > 1 else axes[col]
#             ax.hist(df['Percent Error (%)'].abs(), bins=20, color='skyblue', edgecolor='black')
#             ax.set_xlabel('Absolute Percent Error (%)')
#             ax.set_ylabel('Frequency')
#             ax.set_title(f'Absolute Percent Error Histogram for {file}')
#             ax.grid(True)

#     # Adjust layout
#     plt.tight_layout()
#     plt.show()

# FSR_dir = 'FSR_S1'
# plot_percent_error_histograms_combined(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_percent_error_histograms_separate_windows(FSR_dir):
#     file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = os.listdir(file_path)
#     sorted_files_list = sorted(files)

#     num_files = len(sorted_files_list)
#     num_plots_per_window = 5

#     for i in range(0, num_files, num_plots_per_window):
#         fig, axes = plt.subplots(1, min(num_files - i, num_plots_per_window), figsize=(15, 4))

#         for idx, file in enumerate(sorted_files_list[i:i+num_plots_per_window]):
#             file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
#             df = pd.read_csv(file_path, encoding='latin-1')  # Specify encoding here
#             if 'Percent Error (%)' in df.columns:  # Check if the percent error column exists
#                 axes[idx].hist(df['Percent Error (%)'].abs(), bins=20, color='skyblue', edgecolor='black')
#                 axes[idx].set_xlabel('Absolute Percent Error (%)')
#                 axes[idx].set_ylabel('Frequency')
#                 axes[idx].set_title(f'Absolute Percent Error Histogram - {file.split("_")[2]} lbf')
#                 axes[idx].grid(True)

#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_percent_error_histograms_separate_windows(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_percent_error_histograms_separate_windows(FSR_dir):
#     file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = os.listdir(file_path)
#     sorted_files_list = sorted(files)

#     num_files = len(sorted_files_list)
#     num_plots_per_window = 5

#     for i in range(0, num_files, num_plots_per_window):
#         fig, axes = plt.subplots(1, min(num_files - i, num_plots_per_window), figsize=(15, 4))

#         for idx, file in enumerate(sorted_files_list[i:i+num_plots_per_window]):
#             file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
#             df = pd.read_csv(file_path, encoding='latin-1')  # Specify encoding here
#             if 'Percent Error (%)' in df.columns:  # Check if the percent error column exists
#                 lbf_value = file.split("_")[2].split("(")[1][:-3]  # Extract 'lbf' value from file name
#                 axes[idx].hist(df['Percent Error (%)'].abs(), bins=20, color='skyblue', edgecolor='black')
#                 axes[idx].set_xlabel('Absolute Percent Error (%)')
#                 axes[idx].set_ylabel('Frequency')
#                 axes[idx].set_title(f'Absolute Percent Error Histogram - {lbf_value} lbf')
#                 axes[idx].grid(True)

#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_percent_error_histograms_separate_windows(FSR_dir)


# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_percent_error_histograms_separate_windows(FSR_dir):
#     file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = os.listdir(file_path)
#     sorted_files_list = sorted(files)

#     num_files = len(sorted_files_list)
#     num_plots_per_window = 5

#     for i in range(0, num_files, num_plots_per_window):
#         fig, axes = plt.subplots(1, min(num_files - i, num_plots_per_window), figsize=(15, 4))

#         for idx, file in enumerate(sorted_files_list[i:i+num_plots_per_window]):
#             file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
#             df = pd.read_csv(file_path, encoding='latin-1')  # Specify encoding here
#             if 'Percent Error (%)' in df.columns:  # Check if the percent error column exists
#                 lbf_value = file.split("_")[2].split("(")[1][:-3]  # Extract 'lbf' value from file name
#                 axes[idx].hist(df['Percent Error (%)'].abs(), bins=20, color='skyblue', edgecolor='black')
#                 axes[idx].set_xlabel('Absolute Percent Error (%)')
#                 axes[idx].set_ylabel('Frequency')
#                 axes[idx].set_title(f'{lbf_value} lbf')
#                 axes[idx].grid(True)

#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_percent_error_histograms_separate_windows(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_percent_error_histograms_separate_windows(FSR_dir):
#     file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = os.listdir(file_path)
#     sorted_files_list = sorted(files)

#     num_files = len(sorted_files_list)
#     num_plots_per_window = 5

#     for i in range(0, num_files, num_plots_per_window):
#         fig, axes = plt.subplots(1, min(num_files - i, num_plots_per_window), figsize=(15, 4))

#         for idx, file in enumerate(sorted_files_list[i:i+num_plots_per_window]):
#             file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
#             df = pd.read_csv(file_path, encoding='latin-1')  # Specify encoding here
#             if 'Percent Error (%)' in df.columns:  # Check if the percent error column exists
#                 lbf_value = file.split("_")[2].split("(")[1].split("lbf")[0]  # Extract 'lbf' value from file name
#                 axes[idx].hist(df['Percent Error (%)'].abs(), bins=20, color='skyblue', edgecolor='black')
#                 axes[idx].set_xlabel('Absolute Percent Error (%)')
#                 axes[idx].set_ylabel('Frequency')
#                 axes[idx].set_title(f'{lbf_value} lbf')
#                 axes[idx].grid(True)

#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_percent_error_histograms_separate_windows(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")
    
#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     num_files = len(files_sorted)
#     num_rows = num_files // 5 + 1  # Calculate number of rows required
#     fig, axs = plt.subplots(num_rows, 5, figsize=(20, num_rows * 4))

#     for idx, file in enumerate(files_sorted):
#         file_path = os.path.join(data_path, file)
#         df = pd.read_csv(file_path)
#         df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#         ax = axs[idx // 5, idx % 5] if num_rows > 1 else axs[idx % 5]  # Select axis based on number of rows
#         ax.hist(df['Percent Error (%)'], bins=20)
#         force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#         ax.set_title(f"{force} lbf")
#         ax.set_xlabel('Percent Error (%)')
#         ax.set_ylabel('Frequency')

#     # Adjust layout
#     plt.tight_layout()
#     plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")
    
#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     num_files = len(files_sorted)
#     num_windows = num_files // 5 + (1 if num_files % 5 != 0 else 0)  # Calculate number of windows required
#     files_per_window = num_files // num_windows
#     remaining_files = num_files % num_windows

#     for window_idx in range(num_windows):
#         window_files = files_sorted[window_idx * files_per_window: (window_idx + 1) * files_per_window]
#         if remaining_files and window_idx == num_windows - 1:
#             window_files += files_sorted[-remaining_files:]

#         fig, axs = plt.subplots(1, min(5, len(window_files)), figsize=(20, 4))
#         fig.suptitle(f'Histograms of Percent Error (%)')
        
#         for idx, file in enumerate(window_files):
#             file_path = os.path.join(data_path, file)
#             df = pd.read_csv(file_path)
#             df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#             ax = axs[idx] if len(window_files) > 1 else axs  # Select axis if there are multiple files
#             ax.hist(df['Percent Error (%)'], bins=20)
#             force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#             force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#             ax.set_title(f"{force} lbf")
#             ax.set_xlabel('Percent Error (%)')
#             ax.set_ylabel('Frequency')

#         # Adjust layout
#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)


# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")
    
#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     num_files = len(files_sorted)
#     num_windows = num_files // 5 + (1 if num_files % 5 != 0 else 0)  # Calculate number of windows required
#     files_per_window = num_files // num_windows
#     remaining_files = num_files % num_windows

#     for window_idx in range(num_windows):
#         window_files = files_sorted[window_idx * files_per_window: (window_idx + 1) * files_per_window]
#         if remaining_files and window_idx == num_windows - 1:
#             window_files += files_sorted[-remaining_files:]

#         # Sort window files by force values
#         window_files.sort(key=lambda file: float(re.search(r'\((\d+\.\d+)lbf\)', file).group(1)))

#         fig, axs = plt.subplots(1, min(5, len(window_files)), figsize=(20, 4))
#         fig.suptitle(f'Histograms of Percent Error (%)')
        
#         for idx, file in enumerate(window_files):
#             file_path = os.path.join(data_path, file)
#             df = pd.read_csv(file_path)
#             df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#             ax = axs[idx] if len(window_files) > 1 else axs  # Select axis if there are multiple files
#             ax.hist(df['Percent Error (%)'], bins=20)
#             force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#             force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#             ax.set_title(f"{force} lbf")
#             ax.set_xlabel('Percent Error (%)')
#             ax.set_ylabel('Frequency')

#         # Adjust layout
#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re
# import math

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")

#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     num_files = len(files_sorted)
#     num_windows = math.ceil(num_files / 5)  # Calculate number of windows required
#     files_per_window = math.ceil(num_files / num_windows)
#     remaining_files = num_files % files_per_window

#     for window_idx in range(num_windows):
#         start_idx = window_idx * files_per_window
#         end_idx = min((window_idx + 1) * files_per_window, num_files)
#         window_files = files_sorted[start_idx:end_idx]

#         fig, axs = plt.subplots(1, min(5, len(window_files)), figsize=(20, 4))
#         fig.suptitle(f'Histograms of Percent Error (%)')

#         for idx, file in enumerate(window_files):
#             file_path = os.path.join(data_path, file)
#             df = pd.read_csv(file_path)
#             df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#             ax = axs[idx] if len(window_files) > 1 else axs  # Select axis if there are multiple files
#             ax.hist(df['Percent Error (%)'], bins=20)
#             force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#             force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#             ax.set_title(f"{force} lbf")
#             ax.set_xlabel('Percent Error (%)')
#             ax.set_ylabel('Frequency')

#         # Adjust layout
#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re
# import math

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")

#     # Sort files based on force values
#     files_sorted = sorted(files, key=lambda x: float(re.search(r'\((\d+\.\d+)lbf\)', x).group(1)))

#     # Plot histograms
#     num_files = len(files_sorted)
#     num_windows = math.ceil(num_files / 5)  # Calculate number of windows required
#     files_per_window = math.ceil(num_files / num_windows)
#     remaining_files = num_files % files_per_window

#     for window_idx in range(num_windows):
#         start_idx = window_idx * files_per_window
#         end_idx = min((window_idx + 1) * files_per_window, num_files)
#         window_files = files_sorted[start_idx:end_idx]

#         fig, axs = plt.subplots(1, min(5, len(window_files)), figsize=(20, 4))
#         fig.suptitle(f'Histograms of Percent Error (%)')

#         for idx, file in enumerate(window_files):
#             file_path = os.path.join(data_path, file)
#             df = pd.read_csv(file_path)
#             df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#             ax = axs[idx] if len(window_files) > 1 else axs  # Select axis if there are multiple files
#             ax.hist(df['Percent Error (%)'], bins=20)
#             force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#             force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#             ax.set_title(f"{force} lbf")
#             ax.set_xlabel('Percent Error (%)')
#             ax.set_ylabel('Frequency')

#         # Adjust layout
#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")
    
#     # Sort files based on force values
#     files_sorted = sorted(files, key=lambda x: float(re.search(r'\((\d+\.\d+)lbf\)', x).group(1)))

#     # Plot histograms
#     num_windows = 3  # Number of windows
#     files_per_window = len(files_sorted) // num_windows  # Number of files per window

#     for window_idx in range(num_windows):
#         window_files = files_sorted[window_idx * files_per_window: (window_idx + 1) * files_per_window]

#         fig, axs = plt.subplots(1, len(window_files), figsize=(20, 4))
#         fig.suptitle('Histograms of Percent Error (%)')

#         for idx, file in enumerate(window_files):
#             file_path = os.path.join(data_path, file)
#             df = pd.read_csv(file_path)
#             df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#             ax = axs[idx] if len(window_files) > 1 else axs  # Select axis if there are multiple files
#             ax.hist(df['Percent Error (%)'], bins=20)
#             force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#             force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#             ax.set_title(f"{force} lbf")
#             if window_idx == 0:
#                 ax.set_xlabel('Percent Error (%)')  # Set x label for the first window only
#             ax.set_ylabel('Frequency')

#         # Adjust layout
#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")
    
#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Define order based on provided brackets
#     order = [[4, 4.5, 5, 5.5, 6], [6.5, 7, 7.5, 8, 8.5], [9, 9.5, 10, 10.5], [11]]

#     # Plot histograms
#     window_idx = 0
#     for group in order:
#         fig, axs = plt.subplots(1, len(group), figsize=(20, 4))
#         fig.suptitle('Histograms of Percent Error (%)')
#         for idx, force in enumerate(group):
#             file = next((f for f in files_sorted if str(force) in f), None)
#             if file:
#                 file_path = os.path.join(data_path, file)
#                 df = pd.read_csv(file_path)
#                 df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#                 ax = axs[idx] if len(group) > 1 else axs  # Select axis if there are multiple files
#                 ax.hist(df['Percent Error (%)'], bins=20)
#                 ax.set_title(f"{force} lbf")
#                 ax.set_xlabel('Percent Error (%)')
#                 ax.set_ylabel('Frequency')
#         plt.tight_layout()
#         plt.show()
#         window_idx += 1

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")

#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     num_files = len(files_sorted)
#     num_windows = num_files // 5 + (1 if num_files % 5 != 0 else 0)  # Calculate number of windows required
#     files_per_window = num_files // num_windows
#     remaining_files = num_files % num_windows

#     sorted_files_grouped = [files_sorted[i:i+5] for i in range(0, len(files_sorted), 5)]

#     for group in sorted_files_grouped:
#         fig, axs = plt.subplots(1, len(group), figsize=(20, 4))
#         fig.suptitle('Histograms of Percent Error (%)')
        
#         for idx, file in enumerate(group):
#             file_path = os.path.join(data_path, file)
#             df = pd.read_csv(file_path)
#             df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages
#             ax = axs[idx] if len(group) > 1 else axs  # Select axis if there are multiple files
#             ax.hist(df['Percent Error (%)'], bins=20)
#             force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#             force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#             ax.set_title(f"{force} lbf")
#             ax.set_xlabel('Percent Error (%)')
#             ax.set_ylabel('Frequency')

#         # Adjust layout
#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")

#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     for file in files_sorted:
#         fig, ax = plt.subplots(figsize=(8, 6))
#         fig.suptitle('Histogram of Percent Error (%)')

#         file_path = os.path.join(data_path, file)
#         df = pd.read_csv(file_path)
#         df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages

#         ax.hist(df['Percent Error (%)'], bins=20)
#         force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#         ax.set_title(f"Force: {force} lbf")
#         ax.set_xlabel('Percent Error (%)')
#         ax.set_ylabel('Frequency')

#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def plot_histograms(FSR_dir):
    # Get list of CSV files
    data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
    files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

    # Extract force values from file names using regular expressions
    force_values = []
    for file in files:
        match = re.search(r'\((\d+\.\d+)lbf\)', file)
        if match:
            force_values.append(float(match.group(1)))
        else:
            print(f"Warning: Unable to extract force value from file name: {file}")

    # Sort files based on force values
    files_sorted = [file for _, file in sorted(zip(force_values, files))]

    # Plot histograms
    for file in files_sorted:
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.suptitle('Histogram of Percent Error (%)', fontsize=16, y=0.95)

        file_path = os.path.join(data_path, file)
        df = pd.read_csv(file_path)
        df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages

        sns.histplot(df['Percent Error (%)'], bins=20, kde=True, ax=ax, color='skyblue', edgecolor='black')
        force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
        force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
        ax.set_title(f"Force: {force} lbf", fontsize=14)
        ax.set_xlabel('Percent Error (%)', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.tick_params(axis='both', which='major', labelsize=10)

        plt.tight_layout()
        plt.show()

FSR_dir = 'FSR_S1'
plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")

#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     for file in files_sorted:
#         fig, ax = plt.subplots(figsize=(8, 6))
#         fig.suptitle('Histogram of Percent Error (%)', fontsize=16, y=0.95)

#         file_path = os.path.join(data_path, file)
#         df = pd.read_csv(file_path)
#         df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages

#         sns.histplot(df['Percent Error (%)'], bins=20, kde=True, ax=ax, color='skyblue', edgecolor='black')
#         sns.kdeplot(df['Percent Error (%)'], color='navy', ax=ax, linewidth=2)  # Function in darker color

#         force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#         ax.set_title(f"Force: {force} lbf", fontsize=14)
#         ax.set_xlabel('Percent Error (%)', fontsize=12)
#         ax.set_ylabel('Frequency', fontsize=12)
#         ax.tick_params(axis='both', which='major', labelsize=10)

#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")

#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     for file in files_sorted:
#         fig, ax = plt.subplots(figsize=(8, 6))
#         fig.suptitle('Histogram of Percent Error (%)', fontsize=16, y=0.95)

#         file_path = os.path.join(data_path, file)
#         df = pd.read_csv(file_path)
#         df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages

#         sns.histplot(df['Percent Error (%)'], bins=20, kde=False, cumulative=False, ax=ax, color='skyblue', edgecolor='black')

#         force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#         ax.set_title(f"Force: {force} lbf", fontsize=14)
#         ax.set_xlabel('Percent Error (%)', fontsize=12)
#         ax.set_ylabel('Frequency', fontsize=12)
#         ax.tick_params(axis='both', which='major', labelsize=10)

#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# # plot_histograms(FSR_dir)

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import re

# def plot_histograms(FSR_dir):
#     # Get list of CSV files
#     data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
#     files = [file for file in os.listdir(data_path) if file.endswith('.csv')]

#     # Extract force values from file names using regular expressions
#     force_values = []
#     for file in files:
#         match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         if match:
#             force_values.append(float(match.group(1)))
#         else:
#             print(f"Warning: Unable to extract force value from file name: {file}")

#     # Sort files based on force values
#     files_sorted = [file for _, file in sorted(zip(force_values, files))]

#     # Plot histograms
#     for file in files_sorted:
#         fig, ax = plt.subplots(figsize=(8, 6))
#         fig.suptitle('Histogram of Percent Error (%)', fontsize=16, y=0.95)

#         file_path = os.path.join(data_path, file)
#         df = pd.read_csv(file_path)
#         df['Percent Error (%)'] = df['Percent Error (%)'].abs()  # Take absolute value of percentages

#         # Plot histogram bars
#         sns.histplot(df['Percent Error (%)'], bins=20, kde=False, cumulative=False, ax=ax, color='skyblue', edgecolor='black')

#         # Calculate cumulative percentage
#         total_count = len(df)
#         df_sorted = df['Percent Error (%)'].value_counts().sort_index(ascending=True).cumsum() / total_count * 100

#         # Plot Pareto chart-like line
#         ax2 = ax.twinx()
#         ax2.plot(df_sorted.index, df_sorted.values, color='navy', marker='o', linestyle='-', linewidth=2, markersize=6)
#         ax2.set_ylim(0, 100)
#         ax2.set_ylabel('Cumulative Percentage', fontsize=12)
#         ax2.tick_params(axis='y', labelcolor='navy')

#         force_match = re.search(r'\((\d+\.\d+)lbf\)', file)
#         force = force_match.group(1) if force_match else 'Unknown'  # Extract force value from file name or use 'Unknown' if not found
#         ax.set_title(f"Force: {force} lbf", fontsize=14)
#         ax.set_xlabel('Percent Error (%)', fontsize=12)
#         ax.set_ylabel('Frequency', fontsize=12)
#         ax.tick_params(axis='both', which='major', labelsize=10)

#         plt.tight_layout()
#         plt.show()

# FSR_dir = 'FSR_S1'
# plot_histograms(FSR_dir)
