# CSV to Database: Titanic Data Pipeline

## Project Overview
This project demonstrates an **end-to-end data pipeline** using Python.  
It loads the Titanic CSV dataset, performs **data cleaning**, stores it in a **SQLite database**, and generates **summary insights and visualizations**.

---

## Features
- Loads CSV data into a Pandas DataFrame
- Handles missing values (`Age`, `Embarked`, `Cabin`) and removes duplicates
- Stores cleaned data into a SQLite database (`titanic.db`)
- Generates summary statistics:
  - Total passengers
  - Average age
  - Survival count
  - Passenger class distribution
- Visualizes data with **matplotlib**:
  - Survival rate (survived vs. not survived)
  - Survival by passenger class

---

## Technologies Used
- Python 3.x
- Pandas
- SQLite
- Matplotlib

---

## Folder Structure
csv-data-pipeline/
├─ data/
│ └─ dataset.csv # Titanic CSV
├─ main.py # Python pipeline
├─ titanic.db # SQLite database (generated)
├─ README.md
└─ requirements.txt

---

---

## Install Dependencies
1. Make sure you have **Python 3.x** installed.  
2. Install the required Python libraries using `requirements.txt`:

```bash
pip install -r requirements.txt

## How to Run

Clone this repository:

git clone <your-github-repo-link>
cd csv_to_db_project

Install dependencies (see above).

Run the pipeline:

python main.py

View outputs:

Summary statistics appear in the terminal

Visualizations pop up in separate windows

## screenshots
### survival rate
![survival rate](<Screenshot (180)-1.png>)
### survival by passenger class
![survival by class](<Screenshot (181).png>)