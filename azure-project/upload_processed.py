from azure.storage.blob import BlobServiceClient

# Azure connection string
connection_string = ""

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "processed"

# function for upload
def upload_file(file_name):
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=file_name
    )
    with open(file_name, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"{file_name} uploaded!")

# upload both files
upload_file("top_10_coins.csv")
upload_file("high_volume_coins.csv")

print("✅ All processed files uploaded!")