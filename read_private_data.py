import pandas as pd
import requests

url="https://api.themoviedb.org/3/trending/all"
headers: {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYTgyOGJmYWQ4ZGZiYTM1MWUyOTgyOWUyOTFhZWQ2MiIsIm5iZiI6MTY5MTQ2NjExMS4zNDgsInN1YiI6IjY0ZDFiOTdmNmQ0Yzk3MDBlYzU4ZTRiMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ptdKEYNeZGI2o8wzhlBesFF5hEdDSS5s7J92pegqX6I"
}

response=requests.get(url,headers=headers)
data=response.json()

df=pd.DataFrame(data)
df=df[["id", "title", "original_title"]]
print(df)