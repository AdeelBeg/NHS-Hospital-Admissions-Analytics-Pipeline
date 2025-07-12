# 🏥 NHS Hospital Admissions ETL Pipeline

This project builds a scalable ETL (Extract, Transform, Load) pipeline to process and analyze hospital admissions data from the UK’s NHS Hospital Episode Statistics (HES). The pipeline extracts raw data, performs transformation and cleaning, and loads it into a structured PostgreSQL database. It also includes Jupyter notebooks for analysis and an optional Streamlit dashboard for data visualization.

---

## 📌 Objectives

- 🔄 Automate extraction of publicly available NHS admission datasets
- 🧹 Clean and normalize data (dates, codes, trust names)
- 🗃️ Load structured data into PostgreSQL or a local SQLite database
- 📊 Analyze trends in admissions, diagnosis categories, and seasonal variation
- 💡 Optional: Build a dashboard with Streamlit for quick insights

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Data Processing**: Pandas, NumPy
- **Database**: PostgreSQL (or SQLite for demo)
- **Orchestration** (optional): Apache Airflow
- **Visualization**: Jupyter Notebooks, Streamlit
- **Testing**: Pytest
- **Deployment**: Docker-ready

---

## 📂 Project Structure

nhs-hospital-admissions-etl/
│
├── data/ # Sample raw data (CSV format)
│ └── hospital_admissions_sample.csv
│
├── extract/ # Scripts to fetch/download data
│ └── extract_nhs_data.py
│
├── transform/ # Data cleaning/transformation logic
│ └── clean_admissions_data.py
│
├── load/ # Load cleaned data into database
│ └── load_to_postgres.py
│
├── notebooks/ # EDA & analysis in Jupyter
│ └── admissions_trends.ipynb
│
├── dashboard/ # Streamlit dashboard app
│ └── streamlit_app.py
│
├── tests/ # Unit tests
│ └── test_transform.py
│
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
├── README.md # Project documentation
└── LICENSE # License info (MIT)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nhs-hospital-admissions-etl.git
cd nhs-hospital-admissions-etl
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
⚙️ Running the ETL Pipeline
Step 1: Extract
Download the raw dataset from the NHS portal:
python extract/extract_nhs_data.py
Step 2: Transform
Clean and format the extracted data:
python transform/clean_admissions_data.py
Step 3: Load
Load the cleaned data into PostgreSQL:

python load/load_to_postgres.py
Note: Update the database connection string in load_to_postgres.py or use environment variables.

📓 Exploratory Data Analysis
Launch Jupyter Notebook to explore the dataset:

jupyter notebook notebooks/admissions_trends.ipynb
Includes:

Admissions over time

Seasonal spikes

Top causes of admissions

🧪 Running Tests

pytest tests/
Covers:

Data transformation correctness
Null/missing value handling
Schema validation

📚 NHS Data Source
Hospital Episode Statistics (HES)

📈 Sample Use Cases
Monitor NHS trust performance

Identify seasonal healthcare pressure points

Predict future capacity needs using historical trends

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

🙋‍♂️ Contributions
Contributions are welcome! Please fork this repo, make a branch, and submit a pull request. Open issues for any bugs or feature suggestions.
