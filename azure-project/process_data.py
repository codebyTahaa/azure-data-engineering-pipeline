import pandas as pd

# STEP 1: Load clean data
df = pd.read_csv("clean_crypto_data.csv")

# STEP 2: Top 10 coins by market cap
top_10 = df.sort_values(by="market_cap", ascending=False).head(10)

# STEP 3: High volume coins
high_volume = df[df["volume"] > 10000000]

# STEP 4: Save processed files
top_10.to_csv("top_10_coins.csv", index=False)
high_volume.to_csv("high_volume_coins.csv", index=False)

print("✅ Processed data created!")