
import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)

df = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv")
df.head(5)
print(df.head(2))
print(df.tail(2))
df = pd.read_csv("C:\\Users\\NEAK\\Documents\\Automobile_data.csv", na_values={
    'price':["?", "n.a"],
    'stroke':["?", "n.a"],
    'horsepower':["?", "n.a"],
    'peak-rpm':["?", "n.a"],
    'average-mileage':["?", "n.a"]})
print(df)

