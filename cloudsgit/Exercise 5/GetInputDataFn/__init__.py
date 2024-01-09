# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

import os
from azure.storage.blob import BlobServiceClient
from typing import List, Tuple

def main(input: str):
    try:
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=mapcounter;AccountKey=rUaGQ24qu2C59/Re5A/pSRepmfStesC8iSU9WnoF9l0WprpPeajGY2ZH8eCd9p/e8WpsKjJd3nDX+AStwWfFgw==;EndpointSuffix=core.windows.net")

        # Get container client
        container_client = blob_service_client.get_container_client(container= "my-map-container")

        # List blobs in the container
        blobs = container_client.list_blobs()

        res = ""

        for blob in blobs:
            # Download the blob to a local file
            res += container_client.download_blob(blob.name).readall().decode().replace('\r','')+'\n'

        return res

    except Exception as ex:
        print('Exception:')
        print(ex)
        return []
    
