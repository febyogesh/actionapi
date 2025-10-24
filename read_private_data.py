import pandas as pd
import requests

url="https://api.themoviedb.org/3/trending/all"
headers = {
    "Authorization": "Bearer wrwrewrerw"
}

response=requests.get(url,headers=headers)
data=response.json()

df=pd.DataFrame(data)
df=df[["id", "title", "original_title"]]
print(df)