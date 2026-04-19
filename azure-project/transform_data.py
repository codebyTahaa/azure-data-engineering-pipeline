import pandas as pd
import json

# STEP 1: RAW file load karo
with open("crypto_data.json", "r") as f:
    data = json.load(f)

# STEP 2: DataFrame me convert
df = pd.DataFrame(data)

print("Original columns:")
print(df.columns)

# STEP 3: Useful columns select karo
df_clean = df[[
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "total_volume"
]]

# STEP 4: Rename columns (professional touch)
df_clean.columns = [
    "coin_id",
    "symbol",
    "name",
    "price_usd",
    "market_cap",
    "volume"
]

# STEP 5: Save cleaned data
df_clean.to_csv("clean_crypto_data.csv", index=False)

print("✅ Data cleaned & saved!")