import requests
import pandas as pd

reponse=requests.get("https://jsonplaceholder.typicode.com/users")
data=reponse.json()

df=pd.DataFrame(data)
df=df[["id","name"]]
print(df)