import requests
import os
import time

# Create a folder to store downloaded datasets
os.makedirs("oecd_data", exist_ok=True)

# Base API endpoint for datasets (replace with actual if different)

import requests
import pandas as pd
from io import StringIO

# Data Query
data_query = "https://sdmx.oecd.org/public/rest/data/OECD.ELS.JAI,DSD_TAXBEN_HOURSPOV@DF_HOURSPOV,1.0/...AW100+AW67.C_C2..YES.NO.A?startPeriod=2024&dimensionAtObservation=AllDimensions"


# Structure Query
structure_query = "https://sdmx.oecd.org/public/rest/dataflow/OECD.ELS.JAI/DSD_TAXBEN_HOURSPOV@DF_HOURSPOV/1.0?references=all"


# Define API query URL (CSV with labels format)

headers = {"Accept": "application/json"}
url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_STES@DF_CLI/.M.LI...AA...H?startPeriod=2023-02&dimensionAtObservation=AllDimensions&format=json"

# Fetch data
response = requests.get(structure_query , headers=headers)

if response.status_code == 200:
    data = response.json() # parsed json if returned as json in response
    #print("JSON Response:", data)
    print("Type of data: -------------------", type(data)) 
    data_count, values = data.items()
    #print(data_count, values)
    print("____________________________________________________")

    data = values[1].values()
    df = pd.DataFrame(data)

    print(df.columns)
    print( df.head(5)) #df.head(5)
else:
    print("Error:", response.status_code)
