import pandas as pd

df = pd.read_csv("tracks.csv")

# df.head() # first 5 rows
# df.head(3) # first 3 rows
# df.info() # column names, types, and how many non-null values
# x = df.describe() # count, mean, min, max for numeric columns
# x = df.shape # (rows, columns)


# x = df["speed"] # one column (a Series)
# x = df[["id", "speed"]] # two columns (a smaller DataFrame)
# x = df["speed"].mean() # average of one column
# x = df["speed"].max()
#
# print(x)
