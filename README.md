\# ECommerceAnalytics



An end-to-end e-commerce data analytics project built with Python.



The project demonstrates a complete data workflow starting from raw transactional data and progressing through data cleaning, database storage, analytics, REST API development, interactive visualization, and automated testing.



\---



\## Project Overview



ECommerceAnalytics analyzes the \*\*Online Retail\*\* dataset and provides business-oriented insights from historical e-commerce transactions.



The project was designed to demonstrate practical data engineering and analytics skills, including:



\- Data ingestion

\- Data exploration

\- Data cleaning

\- Relational database storage

\- SQL-based analytics

\- REST API development

\- Interactive dashboard development

\- Automated testing

\- Modular Python project structure



\---



\## Architecture



The project follows an end-to-end data pipeline:



```text

Online Retail Dataset

&#x20;       │

&#x20;       ▼

Data Ingestion

&#x20;       │

&#x20;       ▼

Data Exploration

&#x20;       │

&#x20;       ▼

Data Cleaning

&#x20;       │

&#x20;       ▼

SQLite Database

&#x20;       │

&#x20;       ▼

Analytics

&#x20;       │

&#x20;       ▼

FastAPI REST API

&#x20;       │

&#x20;       ▼

Streamlit Dashboard



The project separates data processing, database access, API functionality, and presentation logic into different modules.



Technologies



| Technology | Purpose                      |

| ---------- | ---------------------------- |

| Python     | Core programming language    |

| Pandas     | Data processing and analysis |

| SQLAlchemy | Database interaction         |

| SQLite     | Relational database          |

| FastAPI    | REST API                     |

| Uvicorn    | API server                   |

| Streamlit  | Interactive dashboard        |

| Requests   | API communication            |

| Pytest     | Automated testing            |

| Jupyter    | Data exploration             |





Dataset



The project uses the Online Retail dataset from the UCI Machine Learning Repository.



The dataset contains transactional data from an online retail business.



Original Dataset



The dataset contains:



541,909 transaction records

8 columns

Invoice information

Product information

Quantity

Unit price

Customer information

Country information



Main columns:



InvoiceNo

StockCode

Description

Quantity

InvoiceDate

UnitPrice

CustomerID

Country



Dataset source:



https://archive.ics.uci.edu/dataset/352/online+retail



The original dataset is not committed to the repository.





Data Processing



The raw dataset contains duplicate records, cancelled transactions, invalid quantities, invalid prices, and missing product descriptions.



The cleaning pipeline performs the following operations:



Remove duplicate records

Remove records with missing product descriptions

Remove cancelled transactions

Remove transactions with non-positive quantities

Remove transactions with non-positive unit prices



After cleaning:



Original records: 541,909

Cleaned records: 524,878



Customer IDs with missing values are retained because customer-level analysis is not required for the current analytics layer.



Database



The cleaned transaction data is stored in a SQLite database.



Database table:



transactions



The table contains:



id

invoice\_no

stock\_code

description

quantity

invoice\_date

unit\_price

customer\_id

country



SQLAlchemy is used to define the database model and manage the database connection.





Analytics



The analytics layer provides reusable functions for calculating business metrics.



Total Revenue



Revenue is calculated as:



Quantity × UnitPrice



Transaction Count



Calculates the number of cleaned transactions.



Top-Selling Products



Identifies products with the highest total quantity sold.



Revenue by Country



Calculates total revenue grouped by country.



Monthly Revenue



Calculates revenue grouped by month to show changes over time.



REST API



The project exposes the analytics through a FastAPI REST API.



Base URL:



http://127.0.0.1:8000

Available Endpoints

| Method | Endpoint                            | Description          |

| ------ | ----------------------------------- | -------------------- |

| GET    | `/`                                 | API health/status    |

| GET    | `/api/analytics/revenue`            | Total revenue        |

| GET    | `/api/analytics/transactions/count` | Transaction count    |

| GET    | `/api/analytics/products/top`       | Top-selling products |

| GET    | `/api/analytics/revenue/by-country` | Revenue by country   |

| GET    | `/api/analytics/revenue/monthly`    | Monthly revenue      |



FastAPI also provides interactive API documentation through:



http://127.0.0.1:8000/docs



Dashboard



The project includes an interactive Streamlit dashboard.



The dashboard consumes the FastAPI endpoints instead of accessing the database directly.



It currently provides:



Total Revenue KPI

Transaction Count KPI

Top-Selling Products table

Revenue by Country chart

Monthly Revenue chart



Architecture:



Streamlit

&#x20;   │

&#x20;   │ HTTP

&#x20;   ▼

FastAPI

&#x20;   │

&#x20;   ▼

SQLite



This separation keeps the dashboard focused on presentation while the API handles access to analytics data.



Project Structure

DataAnalytics/

│

├── data/

│   ├── processed/

│   ├── raw/

│   └── ecommerce.db

│

├── notebooks/

│   └── 01\_data\_exploration.ipynb

│

├── reports/

│

├── src/

│   ├── analytics/

│   │   └── sales.py

│   │

│   ├── api/

│   │   ├── main.py

│   │   └── analytics.py

│   │

│   ├── dashboard/

│   │   ├── app.py

│   │   └── api\_client.py

│   │

│   ├── database/

│   │   ├── connection.py

│   │   ├── models.py

│   │   ├── init\_db.py

│   │   └── load\_to\_db.py

│   │

│   ├── ingestion/

│   │   └── load\_data.py

│   │

│   └── processing/

│       └── clean\_data.py

│

├── tests/

│   ├── test\_ingestion.py

│   ├── test\_processing.py

│   ├── test\_database.py

│   ├── test\_analytics.py

│   ├── test\_api.py

│   └── test\_dashboard.py

│

├── .gitignore

├── README.md

└── requirements.txt



Installation



Clone the repository and navigate to the project directory.



Create and activate the Anaconda environment:



conda create -n data-analytics python=3.11

conda activate data-analytics



Install the project dependencies:



pip install -r requirements.txt

Running the Project

1\. Prepare the Dataset



Download the Online Retail dataset and place it at:



data/raw/Online Retail.xlsx



The raw dataset should not be committed to Git.



2\. Initialize the Database

python -m src.database.init\_db

3\. Load the Cleaned Data



The cleaned transaction data must be loaded into the SQLite database before starting the API.



4\. Start the FastAPI Server

uvicorn src.api.main:app --reload



The API will be available at:



http://127.0.0.1:8000



Swagger documentation:



http://127.0.0.1:8000/docs

5\. Start the Streamlit Dashboard



Open another terminal and run:



streamlit run src/dashboard/app.py



The dashboard will normally be available at:



http://localhost:8501



The FastAPI server should remain running while using the dashboard.



Testing



The project uses Pytest for automated testing.



Run the complete test suite:



pytest



The tests cover:



Data ingestion

Data cleaning

Database functionality

Analytics calculations

API endpoints

Dashboard API client



The current test suite contains:



26 tests

Data Quality Checks



The project validates important data quality conditions during the cleaning process.



Examples include:



Duplicate detection

Missing descriptions

Cancelled invoices

Invalid quantities

Invalid unit prices



These checks help ensure that analytics are performed on a consistent dataset.



Development Workflow



The project was developed using a feature-branch workflow.



Example:



main

&#x20;│

&#x20;├── feature/project-setup

&#x20;├── feature/data-ingestion

&#x20;├── feature/data-exploration

&#x20;├── feature/data-cleaning

&#x20;├── feature/database

&#x20;├── feature/analytics

&#x20;├── feature/api

&#x20;├── feature/dashboard

&#x20;└── feature/dashboard-testing



Each feature was developed, tested, committed, pushed, reviewed through a Pull Request, and merged into main.



Future Improvements



Possible future extensions include:



Interactive dashboard filters

Date-range filtering

Customer-level analytics

Product category analysis

Customer segmentation

More advanced visualizations

Docker containerization

PostgreSQL support

CI/CD integration



These improvements are intentionally kept separate from the current core implementation.



Learning Objectives



This project demonstrates practical experience with:



Python data analysis

Pandas

SQL

Relational databases

SQLAlchemy

REST APIs

FastAPI

Streamlit

Automated testing

Modular software architecture

Git and GitHub workflows



License

The dataset is provided by the UCI Machine Learning Repository under its applicable dataset license.



