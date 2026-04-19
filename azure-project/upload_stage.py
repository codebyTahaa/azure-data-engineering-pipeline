from azure.storage.blob import BlobServiceClient

# Azure connection string
connection_string = ""

# Create client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Container (stage layer)
container_name = "stage"

# File path in Azure
blob_name = "clean_crypto_data.csv"

# Local file
file_path = "clean_crypto_data.csv"

# Upload file
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("✅ Clean data uploaded to STAGE!")