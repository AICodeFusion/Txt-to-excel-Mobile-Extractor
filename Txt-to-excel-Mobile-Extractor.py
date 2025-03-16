import os
import pandas as pd

def print_banner():
    banner = """
    ################################################
    #                                              #
    #       🚀 AI Code Fusion Tool 🚀              #
    #  Extract Mobile Numbers to Excel Efficiently #
    #        Created by AI Code Fusion             #
    #                                              #
    ################################################
    """
    print(banner)

def extract_numbers_from_file(file_path):
    """Reads a text file and extracts mobile numbers."""
    with open(file_path, 'r', encoding='utf-8') as file:
        numbers = [line.strip() for line in file if line.strip().isdigit()]
    return numbers

def save_numbers_to_excel(folder_path, output_file):
    """Reads all text files in a folder and saves numbers to an Excel file."""
    print_banner()  # Display banner
    all_numbers = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Process only .txt files
            file_path = os.path.join(folder_path, filename)
            numbers = extract_numbers_from_file(file_path)
            all_numbers.extend(numbers)
    
    # Convert to DataFrame
    df = pd.DataFrame(all_numbers, columns=['Mobile Number'])
    
    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"✅ Numbers successfully saved to {output_file}")

# Example usage
folder_path = "D:\Phone Number Data"  # Change this to your folder path
output_file = "mobile_numbers.xlsx"  # Output Excel file name
save_numbers_to_excel(folder_path, output_file)
