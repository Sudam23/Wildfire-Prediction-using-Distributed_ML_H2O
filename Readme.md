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

## 📈 Output Highlights

- Models trained using AutoML include:
  - GBM, XGBoost, DRF, and Stacked Ensembles
- Evaluation metrics:
  - AUC, LogLoss, MSE, and variable importance
- Final predictions exported as CSV for analysis

---

## 🧠 Learning Outcomes

- End-to-end wildfire prediction pipeline using distributed ML
- Understanding of H2O AutoML in real-world settings
- Hands-on experience with H2O cluster setup and orchestration

---

## 📜 Citation and License

NASA FIRMS VIIRS data is open and free to use under its  
📄 [Data Policy](https://earthdata.nasa.gov/earth-observation-data/near-real-time/citation#ed-firms-citation)  

See `Dataset Details/AttributesReadme.txt` for full citation and disclaimer info.

---
## 🖥️ Sample Visualization
> Added screenshots of the silhouette score plot or 3D scatter plot here.


## 👨‍💻 Author
- **Sudam Kumar Paul**  
MSc Big Data Analytics | RKMVERI 
- **Kanan Pandit**  
MSc Big Data Analytics | RKMVERI

## 📬 Contact

For any questions or contributions, feel free to open an issue or a pull request.
