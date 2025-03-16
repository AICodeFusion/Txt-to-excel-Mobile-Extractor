# 📌 Excel Mobile Extractor

## 🚀 Overview
Excel Mobile Extractor is a Python-based tool designed to extract mobile numbers from multiple `.txt` files stored in a folder and save them into an organized Excel spreadsheet. This tool is efficient, easy to use, and ideal for bulk data processing.

---

## 📂 Features
- Automatically reads all `.txt` files from a specified folder 📄
- Extracts mobile numbers accurately 🔢
- Saves the extracted numbers into an Excel file 📊
- User-friendly and efficient processing 🚀

---

## 🛠️ Requirements
Make sure you have the following installed before running the script:
- **Python** (>= 3.6) 🐍
- **Pandas** (`pip install pandas`)
- **OpenPyXL** (`pip install openpyxl`) (for Excel support)

---

## 📥 Installation
1. Clone this repository or download the script.
   ```sh
   git clone https://github.com/AICodeFusion/Txt-to-excel-Mobile-Extractor.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Excel-Mobile-Extractor
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

## ▶️ Usage
1. Place all `.txt` files containing mobile numbers into a folder.
2. Update the `folder_path` variable in the script with the path to your folder.
3. Run the script:
   ```sh
   python script.py
   ```
4. The extracted mobile numbers will be saved in an Excel file (`mobile_numbers.xlsx`).

---

## 📌 Example
```python
folder_path = "C:/Users/YourName/Documents/mynumbers"  # Change this to your folder path
output_file = "mobile_numbers.xlsx"  # Output Excel file name
save_numbers_to_excel(folder_path, output_file)
```

---

## 🤝 Contributing
If you want to contribute to this project, feel free to submit a pull request! 🎉

---

## ⚡ License
This project is licensed under the **MIT License**. You are free to use and modify it as needed!

---

### 💬 Need Help?
If you face any issues, feel free to open an issue in the repository or reach out! 😊

