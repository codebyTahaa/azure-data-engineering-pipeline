import requests
import json
from azure.storage.blob import BlobServiceClient

# STEP 1: API se data lo
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
response = requests.get(url)

# check API working
if response.status_code == 200:
    data = response.json()
else:
    print("API error")
    exit()

# STEP 2: JSON format me convert
data_json = json.dumps(data)

# STEP 3: Azure connection
connection_string = ""

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# STEP 4: Container + file path
container_name = "raw"
blob_name = "crypto_data.json"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# STEP 5: Upload
blob_client.upload_blob(data_json, overwrite=True)

print("✅ Data successfully uploaded to Azure!")