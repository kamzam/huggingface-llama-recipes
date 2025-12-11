import requests
import pandas as pd 

url = "https://data360api.worldbank.org/data360/searchv2"
query = "home"  #add user policy query here -- changes 

headers = {
    "accept": "*/*",
    "Content-Type": "application/json"
}

payload = {
    "count": True,
    "select": "series_description/idno, series_description/name, series_description/database_id , series_description/database_name, series_description/definition_short, series_description/definition_long, series_description/topics",
    "search": query ,
    "top": 10
}

response = requests.post(url, headers=headers, json=payload)
print("Type of response: -------------------", type(response)) 



# Print the response as formatted JSON
if response.status_code == 200:
    data = response.json()  # parsed json if returned as json in response
    print("Type of data: -------------------", type(data)) 
    data_context, data_count, values = data.items()
    print(data_context, data_count, values)
    print("____________________________________________________")


    df = pd.DataFrame.from_dict(values[1], orient='columns')
    #print(df)
    
else:
    print(f"Error: {response.status_code}")


expanded = df['series_description'].apply(pd.Series)
expanded.columns = ['idno','name', 'database_id', 'database_name', 'definition_short', 'definition_long', 'topics' ]
# Concatenate with original DataFrame (optional)
df_final = pd.concat([df.drop(columns=['series_description']), expanded], axis=1)

print(df_final.head(3))