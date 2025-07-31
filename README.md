# 📊 CPS Microdata Downloader

This tool makes it easy to download monthly microdata from the U.S. Census Bureau’s **Current Population Survey (CPS)** using the Census API. Designed with accessibility in mind, it lets users without much coding experience pull customized datasets across a selected time range—all through a clean and interactive Streamlit interface.

---

## 🚀 Try It Live

You can access the app here:  
👉 [https://cpstool.streamlit.app/](https://cpstool.streamlit.app/)

---

## 🔍 What It Does

The app allows you to:
- Select a **start and end date** (month/year granularity)
- Choose from a list of commonly used CPS variables (e.g., hours missed from work, race, income, etc.)
- Automatically fetch and compile monthly datasets from the Census API
- Save the combined dataset as a downloadable CSV file

Behind the scenes, the app:
- Dynamically resolves variable names based on monthly metadata (since variable names can change across months)
- Downloads data in parallel for speed
- Handles months where data is unavailable
- Displays a real-time progress bar during the download

---

## ⚙️ How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/deriksuria/cps-microdata-downloader.git
cd cps-microdata-downloader
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the App
```
streamlit run app.py
```
---

### 🔑 API Key
To use the app, you'll need a Census API key. You can request one for free here:
👉 https://api.census.gov/data/key_signup.html

Once you have it, simply paste it into the input field in the app.

### 📁 Output
After processing, your selected data will be:
Saved locally as a CSV file (e.g., cps_sample_jan2022_jun2023.csv)
Available to download directly through the Streamlit interface

### ✅ Example Use Cases
- Researching trends in work absences over time
- Analyzing demographic and economic indicators by month
- Quickly building longitudinal datasets from public microdata

### 📌 Notes
- Not all months are available for every year—if data isn’t published yet, the app will skip and keep going.\
- Variable names can differ slightly between months; the app uses a fallback alias system to resolve them dynamically.
- Built using pandas, requests, concurrent.futures, and streamlit.

### 🙌 Credits
Created by Derik Suria
Inspired by the need for fast, user-friendly access to CPS microdata for policy analysis and research.
