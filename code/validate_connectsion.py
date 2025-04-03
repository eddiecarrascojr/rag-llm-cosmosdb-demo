# Run this code to validate connections to Azure Services.
# Import the required libraries
import time
import json
import uuid
import urllib 
import ijson
import zipfile
from dotenv import dotenv_values
from openai import AzureOpenAI
from azure.core.exceptions import AzureError
from azure.cosmos import PartitionKey, exceptions
from time import sleep
import gradio as gr

# Cosmos DB imports
from azure.cosmos import CosmosClient

# Load configuration
env_name = "sample_env_file.env"
config = dotenv_values(env_name)

cosmos_conn = config['cosmos_uri']
cosmos_key = config['cosmos_key']
cosmos_database = config['cosmos_database_name']
cosmos_collection = config['cosmos_collection_name']
cosmos_vector_property = config['cosmos_vector_property_name']
comsos_cache_db = config['cosmos_cache_database_name']
cosmos_cache = config['cosmos_cache_collection_name']

# Create the Azure Cosmos DB for NoSQL async client for faster data loading
cosmos_client = CosmosClient(url=cosmos_conn, credential=cosmos_key)

openai_endpoint = config['openai_endpoint']
openai_key = config['openai_key']
openai_api_version = config['openai_api_version']
openai_embeddings_deployment = config['openai_embeddings_deployment']
openai_embeddings_dimensions = int(config['openai_embeddings_dimensions'])
openai_completions_deployment = config['openai_completions_deployment']

# Movies file url
storage_file_url = config['storage_file_url']

# Create the OpenAI client
openai_client = AzureOpenAI(azure_endpoint=openai_endpoint, api_key=openai_key, api_version=openai_api_version)