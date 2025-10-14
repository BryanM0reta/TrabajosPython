import pandas as pd

serData=pd.Series(data=[10, 20, 30, 40],index=["carlos", "jimmy", "wilson", "freddy"])
print(serData)
print(serData.index)
print(serData["jimmy"])
print("jimmy" in serData)

serData1=serData*2
print(serData1)

print ("---------------------------------------------------------")
diccionary={"one":pd.Series(data=[1,2,3],index=["juam", "carlos", "pepe"]),
            "two":pd.Series(data=[10,20,30],index=["juam", "carlos", "pepe"])}

df=pd.DataFrame(diccionary)
print(df)
print(df.index)
print(df.columns)

df["three"]= df["one"]* df["two"]
print(df)


df["filter"]=df["three"]>45
print(df)

del df["filter"]
print(df)

df.insert(1,"copu of on", df["one"])
print(df)

print ("///////IMPORTING CSV FILES///////")
movies=pd.read_csv("movies.csv")
print(movies.columns)
print(movies.shape)

print ("///////IMPORTING CSV FILES///////")
ratings=pd.read_csv("ratings.csv")
print(ratings.columns)
print(ratings.shape)
print(ratings.head(2))

print ("///////IMPORTING CSV FILES///////")
tags=pd.read_csv("tags.csv")
print(tags.columns)
print(tags.shape)
print(tags.tail(2))

del ratings["timestamp"]
del tags["timestamp"]

print("variavles of tags")
print(tags.columns)
print("variavles of raitings")
print(ratings.columns)

print(tags.iloc[[0,22,500]])
print(tags.index)

print ("---------------------------------------------------------")

print(ratings.head (5))
print(ratings["rating"].describe())
print(ratings["rating"].mean())
print(ratings["rating"].min())
print(ratings["rating"].max())

print(" mejores 5")
is_highly_rated=ratings["rating"]>=4
print(ratings[is_highly_rated].head(5))
print(ratings[is_highly_rated].shape)

print(movies.columns)
is_animation=movies["genres"].str.contains("Animation")
print(movies[is_animation].head(5))
print(movies[is_animation].shape)

print("movies")
print(movies.columns)
print("ratings")
print(ratings.columns)


