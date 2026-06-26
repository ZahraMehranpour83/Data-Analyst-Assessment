# Data Analyst Assessment

## 📌 Introduction

Welcome to the **Data Analyst Assessment** repository.

The purpose of this assessment is to evaluate your practical skills in:

* Python
* Pandas
* NumPy
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Debugging
* Code Quality
* Data Visualization

Each task should be completed independently and submitted through a **Pull Request**.

---

# Repository Structure

```text
Data-Analyst-Assessment
│
├── README.md
│
├── datasets
│   └── train.csv
│
├── tasks
│   ├── Task-01-EDA.md
│   └── Task-02-Debug.md
│
├── debug
│   └── broken_code.py
│
├── submissions
│   └── YOUR_NAME
│       ├── task1.ipynb
│       ├── task2.py
│       ├── report.pdf
│       ├── requirements.txt
│       └── README.md
│
└── images
```

---

# 📂 Task 1 – Data Preprocessing & Exploratory Data Analysis

## Dataset

Use the **train.csv** file located in the `datasets` folder.

---

## Objective

The objective of this task is to evaluate your ability to clean, preprocess, analyze, and visualize a real-world dataset.

---

## Requirements

### 1. Data Loading

* Load the dataset into a Pandas DataFrame.
* Display the number of rows and columns.
* Display the data type of each column.
* Calculate the DataFrame memory usage.
* Display the number and percentage of missing values for each column.

---

### 2. Data Reduction

* Remove columns with more than **60% missing values**.
* Remove duplicate or unnecessary columns (if any).
* Optimize data types (Type Casting) to reduce memory usage.
* Compare memory usage before and after optimization.

---

### 3. Missing Value Handling

Choose the most appropriate strategy for handling missing values based on the type and importance of each feature.

Possible strategies include:

* Mean
* Median
* Mode
* Drop rows or columns (when justified)

Provide a brief explanation for each decision.

---

### 4. Descriptive Statistics

For all numerical columns, calculate:

* Minimum
* Maximum
* Mean
* Median
* Variance
* Standard Deviation

Present the results in a well-formatted table.

---

### 5. Data Visualization

For all numerical features:

* Plot Histograms.
* Plot Violin Plots.

Then provide a brief analysis of:

* Data distribution
* Potential outliers
* Distribution normality

---

### 6. Final Report

Prepare a short report including:

* Missing values before and after preprocessing.
* Memory usage before and after optimization.
* Key descriptive statistics.
* Insights from the visualizations.

---

# 📂 Task 2 – Debugging Assessment

## Objective

A Python script containing multiple issues will be provided.

Your task is to identify, fix, and improve the code using your knowledge of Python, Pandas, NumPy, and data analysis best practices.

---

## Requirements

Review the provided code and:

* Fix all syntax errors.
* Fix all runtime errors.
* Identify and resolve logical errors.
* Refactor the code to improve readability and maintainability.
* Apply best practices when using Pandas and NumPy.
* Correct the missing value handling strategy.
* Verify and fix statistical calculations.
* Ensure all visualizations work correctly.
* Prevent data loss caused by incorrect data type conversions.
* Add error handling where appropriate.
* Improve overall code quality and performance.

Finally, provide a brief explanation covering:

* The bugs you identified.
* Why they caused problems.
* How you fixed them.

---

# 📤 Submission

Create a folder named with your own name inside the `submissions` directory:

```text
submissions/YOUR_NAME
```

Include the following files:

* `task1.ipynb`
* `task2.py`
* `report.pdf`
* `requirements.txt`
* `README.md`

---

# ✅ Evaluation Criteria

| Criteria               | Points |
| ---------------------- | -----: |
| Data Preprocessing     |     20 |
| Missing Value Handling |     15 |
| Statistical Analysis   |     15 |
| Data Visualization     |     10 |
| Code Quality           |     15 |
| Debugging              |     20 |
| Documentation          |      5 |

**Total: 100 Points**
