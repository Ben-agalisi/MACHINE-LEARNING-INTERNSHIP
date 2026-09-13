# Project Week 1: Python, Data Preparation & Machine Learning Fundamentals

## 1. Short Explanation of the Machine Learning Problem
* **The Problem:** Predicting whether a passenger survived the Titanic disaster based on socio-economic status, age, gender, and ticket metrics.
* **Core Machine Learning Concepts:** 
  * **Features & Target Variables:** *Features* are the input variables used for prediction (e.g., Age, Pclass, Fare, Sex). The *Target* is the output label we aim to predict (`Survived`).
  * **Classification vs. Regression:** This is a **Classification** problem because the target variable is categorical (Binary: survived or did not survive). Regression, by contrast, predicts continuous numerical values.
  * **Supervised Learning:** The model utilizes historical data containing known target outcomes (`Survived`) to learn mapping patterns between features and labels.
  * **Training & Testing Datasets:** Preparing the dataset layout to allow models to learn from a training partition and evaluate performance on an unseen testing partition.

---

## 2. Data Preprocessing Documentation
The data preparation pipeline was implemented programmatically via a custom Python automation script (`clean_data.py`). The step-by-step process includes:

1. **Data Ingestion:** Pulled the raw Titanic dataset directly into a Pandas DataFrame from the remote source URL.
2. **Data Inspection:** Evaluated dataset dimensions, inspected column data types, and scanned for data quality issues.
3. **Handling Missing Values:**
   * Imputed missing values in the `Age` column using the **median** age to prevent distortion from extreme outliers.
   * Dropped high-missing-percentage structural identifiers and text columns (`Cabin`, `PassengerId`, `Name`, `Ticket`).
   * Filled missing categorical values in the `Embarked` column using the **mode** (most frequent value).
4. **Duplicate Management:** Scanned for and removed duplicate rows to maintain data integrity.
5. **Feature Encoding:** 
   * Converted text-based categorical columns (`Sex`) into binary numerical mappings (`0` for male, `1` for female).
   * Applied one-hot encoding (`pd.get_dummies`) to multi-category text columns (`Embarked`) to prepare data structures for machine learning algorithms.
6. **Exportation:** Automatically resolved the host desktop path and exported the finalized, processed dataset as `cleaned_titanic.csv`.

---

## 3. Files Included in this Repository
* **`clean_data.py`** — The standalone Python script that automates downloading, inspecting, cleaning, encoding, and saving the dataset.
* **`cleaned_titanic.csv`** — The final clean dataset ready for model training

#Nexafrica
