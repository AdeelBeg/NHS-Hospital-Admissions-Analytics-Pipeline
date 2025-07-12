import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Example cleaning steps
    df.dropna(subset=['Admission_Date'], inplace=True)
    df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
    df['Diagnosis'] = df['Diagnosis'].str.strip().str.upper()

    # Remove invalid rows
    df = df[df['Age'] > 0]

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

def main():
    input_file = "data/hospital_admissions_sample.csv"
    output_file = "data/cleaned_admissions.csv"
    clean_data(input_file, output_file)

if __name__ == "__main__":
    main()
