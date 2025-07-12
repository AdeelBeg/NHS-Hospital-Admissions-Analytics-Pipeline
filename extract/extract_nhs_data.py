import os
import requests
import pandas as pd

def download_csv(url, output_path):
    """Download CSV file from NHS website"""
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded successfully to {output_path}")
    else:
        print(f"Failed to download. Status Code: {response.status_code}")

def main():
    # Example URL (Replace with updated dataset link)
    nhs_csv_url = "https://files.digital.nhs.uk/assets/HES/admissions_sample.csv"
    output_file = "data/hospital_admissions_sample.csv"

    os.makedirs("data", exist_ok=True)
    download_csv(nhs_csv_url, output_file)

if __name__ == "__main__":
    main()
