import pandas as pd
import requests

url="https://api.themoviedb.org/3/trending/movie"
headers = {
    "Authorization": "Bearer eyJ92pegqX6I"
}

response=requests.get(url,headers=headers)
data=response.json()

df=pd.DataFrame(data)
print(df)