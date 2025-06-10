# 🔥 Wildfire Prediction Using H2O in Distributed Mode

This project presents a distributed machine learning pipeline for **wildfire prediction** using **viirs-snpp_2023_all_countries.zip** and the **H2O framework**. It demonstrates how to use **AutoML in a multi-node cluster setup** to build and evaluate predictive models efficiently at scale.

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

## 📊 Dataset Details

- **Source:** NASA FIRMS VIIRS 375m Active Fire Data (2023)  
- **Original Folder Name:** `viirs-snpp_2023_all_countries`  
- **Content:** Multiple country-wise `.csv` files containing wildfire events (latitude, longitude, brightness, date, time, etc.)

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

### 🌲 Manual Random Forest Model (Outside AutoML)

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

---

## 📈 Output Highlights

- Models Trained:
  - GBM, DRF, XGBoost, GLM, Deep Learning, Stacked Ensembles
  - + Manual Random Forest
- Evaluation Metrics:
  - AUC, RMSE, LogLoss, Variable Importance
- Output:
  - Predictions exported to `wildfire_predictions.csv`

---

## 🧠 Learning Outcomes

- End-to-end wildfire prediction pipeline using distributed ML.
- Manual model comparison using Random Forest.
- Understanding of H2O AutoML in real-world settings.
- Hands-on experience with H2O cluster setup and orchestration.

---

## 📜 Citation and License

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
