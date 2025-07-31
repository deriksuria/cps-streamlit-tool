import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

# --- Variable aliases ---
VARIABLE_ALIAS = {
    "PUHROFF1": ["PUHROFF1"],
    "PUHROFF2": ["PUHROFF2"],
    "PWSSWGT": ["PWSSWGT"],
    "GESTFIPS": ["GESTFIPS", "STATE"],
    "GTCO": ["GTCO", "COUNTY"],
    "PTDTRACE": ["PTDTRACE"],
    "HEFAMINC": ["HEFAMINC"]
}

from variable_aliases import VARIABLE_ALIASES

# --- Title ---
st.title("📊 CPS Microdata Downloader")

# --- User Inputs ---
api_key = st.text_input("Enter your Census API key", type="password")

start_date = st.date_input("Start Date", datetime(2024, 1, 1))
end_date = st.date_input("End Date", datetime(2025, 6, 1))

selected_vars = st.multiselect(
    "Choose variables to download",
    options=list(VARIABLE_ALIASES.keys()),
    default=["PUHROFF1", "PUHROFF2", "PWSSWGT"]
)

# --- Resolve variables using metadata ---
@st.cache_data(show_spinner=False)
def resolve_variable_names(year, month, selected_vars):
    metadata_url = f"https://api.census.gov/data/{year}/cps/basic/{month}/variables.json"
    try:
        meta = requests.get(metadata_url).json()
        available_vars = set(meta["variables"].keys())
        resolved = {}
        for logical_name in selected_vars:
            for var in VARIABLE_ALIASES.get(logical_name, []):
                if var in available_vars:
                    resolved[logical_name] = var
                    break
        return resolved
    except:
        return {}

# --- Download data for one month ---
def download_month(year, month, selected_vars, api_key):
    var_map = resolve_variable_names(year, month, selected_vars)
    if not var_map:
        return None
    fields = list(var_map.values())
    url = f"https://api.census.gov/data/{year}/cps/basic/{month}"
    params = {"get": ",".join(fields), "key": api_key}
    try:
        r = requests.get(url, params=params)
        if r.status_code == 200:
            data = r.json()
            if len(data) > 1:
                df = pd.DataFrame(data[1:], columns=data[0])
                df = df.apply(pd.to_numeric, errors="coerce")
                df["year"] = year
                df["month"] = month
                df.rename(columns={v: k for k, v in var_map.items()}, inplace=True)
                return df
    except:
        pass
    return None

# --- Download Button ---
if st.button("Start Download"):
    if not api_key:
        st.error("Please enter your Census API key.")
    elif start_date > end_date:
        st.error("Start date must be before end date.")
    elif not selected_vars:
        st.error("Please select at least one variable.")
    else:
        st.info("Downloading data...")
        tasks = []
        current = datetime(start_date.year, start_date.month, 1)
        end_dt = datetime(end_date.year, end_date.month, 1)
        while current <= end_dt:
            tasks.append((current.year, current.strftime('%b').lower()))
            current += relativedelta(months=1)

        all_dfs = []
        progress_bar = st.progress(0)
        status_text = st.empty()

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = {
                executor.submit(download_month, y, m, selected_vars, api_key): (y, m)
                for y, m in tasks
            }

            total = len(futures)
            for i, future in enumerate(as_completed(futures)):
                df = future.result()
                if df is not None:
                    all_dfs.append(df)
                progress_bar.progress((i + 1) / total)
                y, m = futures[future]
                status_text.text(f"Downloaded {m.title()} {y} ({i + 1}/{total})")

        status_text.text("✅ Download complete.")
        progress_bar.empty()

        if all_dfs:
            full_df = pd.concat(all_dfs, ignore_index=True)
            filename = f"cps_sample_{start_date.strftime('%b%Y').lower()}_{end_date.strftime('%b%Y').lower()}.csv"
            full_df.to_csv(filename, index=False)
            st.success(f"✅ Data saved as: {filename}")
            st.download_button("📥 Download CSV", data=full_df.to_csv(index=False), file_name=filename, mime="text/csv")
        else:
            st.warning("❗ No data retrieved.")
