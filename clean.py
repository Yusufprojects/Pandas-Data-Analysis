import numpy as np
import pandas as pd

raw_data = {
    'product_name': [' Laptop ', 'SMARTPHONE', ' HeadPhones ', 'Tablet', ' Keyboard '],
    'category': ['Electronics', 'elecTRONics', 'Audio', 'Electronics', 'missing'],
    'price_usd': ['$1,200', '$800', '150', 'Unknown', np.nan],
    'stock': ['15', 'None', '45', '0', '8'],
    'rating': ['4.5', '4.8', 'Not Rated', '3.9', np.nan]
}

df = pd.DataFrame(raw_data)


df["product_name"] = df["product_name"].str.strip()
df["category"] = df["category"].str.capitalize()
df.replace(["missing", "Unknown", "None", "Not Rated"], np.nan, inplace=True)
df.replace("Unknown", np.nan, inplace=True)
df["price_usd"] = df["price_usd"].str.replace("$", "", regex=False)
df["price_usd"] = df["price_usd"].str.replace(",", "", regex=False)
print(df)