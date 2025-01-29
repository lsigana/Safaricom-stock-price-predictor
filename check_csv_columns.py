import pandas as pd

def check_csv_columns(file_path):
    data = pd.read_csv(file_path)
    print(data.columns)

if __name__ == "__main__":
    check_csv_columns('stocks/SCOM_data.csv')
