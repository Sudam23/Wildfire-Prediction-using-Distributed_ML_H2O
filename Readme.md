# 🔥 Wildfire Prediction Using H2O in Distributed Mode

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![H2O.ai](https://img.shields.io/badge/H2O.ai-distributed-yellow)
![License: Academic Use](https://img.shields.io/badge/License-Academic%20Use%20Only-lightgrey)
![Status](https://img.shields.io/badge/status-active-success)

This project presents a distributed machine learning pipeline for **wildfire prediction** using **viirs-snpp_2023_all_countries.zip** and the **H2O framework**. It demonstrates how to use **AutoML in a multi-node cluster setup** to build and evaluate predictive models efficiently at scale.

> A multiclass classification project leveraging a **2-node distributed H2O cluster** and a **Distributed Random Forest (DRF)** model to predict wildfire confidence levels using **VIIRS SNPP 2023 global data**.

---

## 🎯 Objective

The primary objective of this project is to:
- Build a **high-accuracy wildfire classification system**
- Utilize **distributed computing** to handle large-scale satellite data
- Deploy a **Distributed Random Forest (DRF)** model via H2O.ai
- Evaluate performance using real metrics like **AUC, Accuracy, F1-score**
- Enable analysis across all countries using 2023 fire records

---


## 📁 Project Structure

```plaintext
Wildfire-Prediction-using-Distributed_ML_H2O/
├── Dataset Details/
│   ├── AttributesReadme.txt
│   ├── dataset_name.txt
│   └── Readme.md
├── Dataset Preparation/
│   └── csv_merge.py
├── H2O Cluster Setup/
│   ├── Steps to Create H2O Cluster.txt
│   └── h2o_flatfile.txt
├── Final_Distributed_ML_using_H2O Framework.ipynb
├── AutoML.txt
└── README.md
```

---

## 📍 Course Project | Ramakrishna Mission Vivekananda Educational and Research Institute, Belur Math  
🧠 Team: Tom and Jerry  
👨‍💻 Members: Kanan Pandit , Sudam Paul  


## 📊 Dataset Details

- **Source:** NASA FIRMS VIIRS 375m Active Fire Data (2023)  
- **Original Folder Name:** `viirs-snpp_2023_all_countries`  
- **Content:** Multiple country-wise `.csv` files containing wildfire events (latitude, longitude, brightness, date, time, etc.)

### 🔗 Official Data Sources

- 🌍 **Global Fire Data Download**: [https://firms.modaps.eosdis.nasa.gov/download/](https://firms.modaps.eosdis.nasa.gov/download/)  
- 🌐 **Country-wise Fire Data Viewer**: [https://firms.modaps.eosdis.nasa.gov/country/](https://firms.modaps.eosdis.nasa.gov/country/)

This dataset includes active fire points detected globally by the **Suomi National Polar-orbiting Partnership (SNPP)** satellite using the **VIIRS sensor at 375m resolution**.
### 📄 Data Overview

- **Satellite**: VIIRS SNPP  
- **Temporal Coverage**: January 1 – December 31, 2023  
- **Spatial Coverage**: 🌍 All countries (global)  
- **Resolution**: 375 meters  
- **Projection**: WGS84 (latitude/longitude)  
- **Format**: CSV (also available as KML, SHP via FIRMS)

---

### 🔍 Feature Summary

| Feature     | Description                                |
|-------------|--------------------------------------------|
| `latitude`  | Fire latitude (WGS84)                      |
| `longitude` | Fire longitude (WGS84)                     |
| `brightness`| Brightness of fire detection               |
| `scan`      | Width of the scan footprint                |
| `track`     | Length of the scan footprint               |
| `acq_date`  | Date of fire detection                     |
| `acq_time`  | Time of fire detection (UTC)               |
| `satellite` | SNPP satellite ID                          |
| `confidence`| Confidence level (Low, Nominal, High)      |
| `frp`       | Fire Radiative Power (MW)                  |
| `daynight`  | Day or Night detection                     |
| `version`   | Collection version info                    |

For more information on attribute fields:  
🔗 https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/v1-vnp14imgt#ed-viirs-375m-attributes

---

## 🛠️ Dataset Preparation

All raw `.csv` files from different countries were merged into a single unified dataset for training:

- **Script Used:** `csv_merge.py`
- **Output File:** `Wildfire_prediction.csv`

To merge:
```bash
python dataset_preparation/csv_merge.py
```

---

## ☁️ H2O Cluster Setup (Distributed Mode)

To run H2O in a distributed cluster, follow these steps:

1. **Install H2O and dependencies** on each node:
   ```bash
   pip install h2o
   ```

2. **Create a flatfile** (`h2o_flatfile.txt`) listing all worker node IPs (including master), one per line:
   ```text
   192.168.1.10:54321
   192.168.1.11:54321
   ```

3. **Start H2O on each node**:
   ```bash
   java -Xmx4g -jar h2o.jar -flatfile h2o_flatfile.txt -port 54321
   ```

4. **Check H2O Cluster Web UI** (on the master IP):
   ```
   http://<master-ip>:54321
   ```

📁 Refer to: `H2O Cluster Setup/Steps to Create H2O Cluster.txt`

---

## 🤖 AutoML Pipeline

- **Platform:** H2O AutoML (multi-node)
- **Notebook:** `Final_Distributed_ML_using_H2O Framework.ipynb`
- **Tasks Covered:**
  - Cluster initialization
  - Data import and exploration
  - Automatic training of multiple models
  - Leaderboard evaluation
  - Model interpretation
  - Final prediction

📄 Additional explanation is provided in `AutoML.txt`.

---

## 📘 Notebook Overview – `Final_Distributed_ML_using_H2O Framework.ipynb`

This notebook demonstrates a complete, distributed machine learning workflow using the H2O framework.

### 🔹 Steps Covered:

1. **Environment Setup**
   - Warnings suppressed, visualization style set.
   - H2O cluster initialized using `h2o.init(ip="172.20.252.53", port=54323)`.

2. **Data Loading**
   - Data loaded from:
     ```python
     h2o.upload_file("Wildfire_prediction.csv")
     ```

3. **Exploratory Data Analysis**
   - Sample records, data schema, null checks, summary stats.

4. **Feature Engineering**
   - Column conversion, data cleaning.
   - Train/validation/test split:
     ```python
     train, valid, test = data.split_frame(ratios=[0.7, 0.15], seed=1234)
     ```

5. **AutoML Training**
   - Automatically trains models using:
     ```python
     from h2o.automl import H2OAutoML
     aml = H2OAutoML(max_models=10, seed=1, max_runtime_secs=600)
     aml.train(y="target_column", training_frame=train, validation_frame=valid)
     ```

6. **Model Leaderboard**
   - AutoML leaderboard includes GBM, XGBoost, DRF, GLM, and Ensembles.

7. **Evaluation**
   - Leader model is evaluated on test set.
   - Metrics and visualizations include AUC, LogLoss, variable importance.

8. **Prediction and Export**
   - Final predictions saved as:
     ```python
     preds = aml.leader.predict(test)
     preds.as_data_frame().to_csv("wildfire_predictions.csv")
     ```

---

### Manual Random Forest Model (Outside AutoML)

In addition to AutoML, the notebook also trains a standalone **Random Forest Classifier** using `H2ORandomForestEstimator` for predicting wildfire confidence levels.

#### Model Details:
- **Target Variable:** `confidence` (converted to categorical)
- **Features:** All columns except `confidence`
- **Model Parameters:**
  ```python
  rf_model = H2ORandomForestEstimator(ntrees=30, max_depth=20, seed=1234)
  rf_model.train(x=x, y=y, training_frame=train, validation_frame=valid)
  ```

The model is trained and summarized to compare.
#### 📈 Model Performance: 

| Metric                | Value    |
|-----------------------|----------|
| RMSE                  | 0.1721   |
| MSE                   | 0.02964  |
| Mean Per Class Error  | 0.070    |
| LogLoss               | 0.0961   |


---

## 📈 Output Highlights

- Models Trained:
  - GBM, DRF, XGBoost, GLM, Deep Learning, Stacked Ensembles
  - + Manual Random Forest
- Evaluation Metrics:
  - MSE, RMSE, LogLoss, Variable Importance
- Output:
  - 

---

## 🧠 Learning Outcomes

- End-to-end wildfire prediction pipeline using distributed ML.
- Manual model comparison using Random Forest.
- Understanding of H2O AutoML in real-world settings.
- Hands-on experience with H2O cluster setup and orchestration.

---

### 🙏 Acknowledgements

Special thanks to:

**Champak Kumar Dutta**  
Assistant Professor, Department of Data Science  
RKMVERI, Belur Math, West Bengal  

For his guidance, mentorship, and continuous encouragement.

---
## 📜 Citation and License
This project is intended for **academic use only** and is **not licensed for commercial or production deployment**.  
**No license is granted.**  
Please contact the authors for further usage rights.

NASA FIRMS VIIRS data is open and free to use under its  
📄 [Data Policy](https://earthdata.nasa.gov/earth-observation-data/near-real-time/citation#ed-firms-citation)  

See `Dataset Details/AttributesReadme.txt` for full citation and disclaimer info.

---
## 🖥️ Sample Visualization
> Added screenshots of the H2O cluster setup and Output of ML models here.


## 👨‍💻 Author
- **Sudam Kumar Paul**  
MSc Big Data Analytics | RKMVERI 
- **Kanan Pandit**  
MSc Big Data Analytics | RKMVERI

## 📬 Contact

For any questions or contributions, feel free to open an issue or a pull request.

### 👨‍💻 Kanan Pandit  
🌐 [Portfolio](https://kananpanditportfolio.netlify.app/)  
✉️ kananpandit02@gmail.com  

### 👨‍💻 Sudam Paul  
🌐 [Portfolio](https://sudam23.github.io/My_Portfolio/)  
✉️ 2002sudam@gmail.com  

### 🏫 Institution  
**Ramakrishna Mission Vivekananda Educational and Research Institute**  
📍 *Belur Math, Howrah, West Bengal*
