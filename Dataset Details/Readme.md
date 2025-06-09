# 📁 Dataset Preparation for Wildfire Prediction Project

This document describes the process of preparing the dataset used in our wildfire prediction project. The raw data was sourced from NASA FIRMS and includes wildfire incidents recorded globally during the year 2023.

---

## 🌍 Dataset Source

- **Original Dataset Name:** `viirs-snpp_2023_all_countries`
- **Source:** [NASA FIRMS VIIRS 375m Active Fire Data](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/v1-vnp14imgt)
- **Projection:** WGS84 Geographic (latitude/longitude)
- **Disclaimer:** Refer to `AttributesReadme.txt` for licensing, citation, and usage policies.

---

## 📑 Data Description

The raw dataset contains multiple `.csv` files, each representing fire/hotspot data for different countries in the year 2023. These files include attributes such as:

- Latitude & Longitude
- Brightness
- Scan & Track values
- Acq_Date & Acq_Time
- Satellite
- Confidence
- FRP (Fire Radiative Power)
- Day/Night indicator

See [VIIRS Attribute Documentation](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/v1-vnp14imgt#ed-viirs-375m-attributes) for full details.

---

## 🛠️ Preprocessing Steps

1. **Merging CSV Files:**
   - A custom Python script `csv_merge.py` was used to merge all individual `.csv` files into a single file.
   - Output file: `Wildfire_prediction.csv`

2. **Script:**

```bash
python csv_merge.py
```
This script recursively reads all .csv files inside viirs-snpp_2023_all_countries/ and concatenates them into one unified dataset for further processing and model training.
