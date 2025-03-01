import os
import kaggle
import zipfile
import duckdb

# Define the dataset and file names
dataset_url = 'open-flights/airline-database'
output_zip = 'data/airline-database.zip'
csv_file = 'data/airlines.csv'

# Step 1: Download the dataset using Kaggle API
def download_dataset():
    print(f"Downloading dataset from Kaggle: {dataset_url}")
    kaggle.api.dataset_download_files(dataset_url, path='./data', unzip=False)

    # Unzip the dataset after download
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall(path='data')
    print(f"Extracted files: {zip_ref.namelist()}")

# Step 2: Load the CSV data into DuckDB
def load_to_duckdb():
    print("Loading data into DuckDB...")
    con = duckdb.connect('airline_data.db')  # Connect to DuckDB (creates a new DB if not exists)
    
    # Load the CSV file into DuckDB
    con.execute(f"""
        CREATE TABLE IF NOT EXISTS airline_data AS 
        SELECT * FROM read_csv_auto('{csv_file}')
    """)
    print("Data loaded into DuckDB successfully.")

# Main function to orchestrate the steps
def main():
    download_dataset()
    load_to_duckdb()

if __name__ == '__main__':
    main()
