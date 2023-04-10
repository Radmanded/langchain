import asyncio
import time
import json

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, load_chain  # Import the load_chain function
from custom_api_docs import CUSTOM_API_DOCS
from custom_api_chain import CustomAPIChain

# ... (Your original code)

# Load the chain from the chain.json file
chain_filepath = "chain.json"
chain = load_chain(chain_filepath)

# Query the custom API
response = chain.run("Get reseller data for 24/7 NETWORKS LLC")
print(response)

