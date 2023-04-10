

Connecting Langchain OpenAI and RIVT API

Need to start with langchain Chains. 

## Chains 

If you are just getting started, and you have relatively simple apis, you should get started with chains. Chains are a sequence of predetermined steps, so they are good to get started with as they give you more control and let you understand what is happening better.

## Agents

Agents are more complex, and involve multiple queries to the LLM to understand what to do. The downside of agents are that you have less control. The upside is that they are more powerful, which allows you to use them on larger and more complex schemas.


API Chains
This notebook showcases using LLMs to interact with APIs to retrieve relevant information.


API Chains Eamples
from langchain.chains.api.prompt import API_RESPONSE_PROMPT
from langchain.chains import APIChain
from langchain.prompts.prompt import PromptTemplate


from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

OpenMeteo Example
from langchain.chains.api import open_meteo_docs
chain_new = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)
chain_new.run('What is the weather like right now in Munich, Germany in degrees Farenheit?')

TMDB Example
import os
os.environ['TMDB_BEARER_TOKEN'] = ""
from langchain.chains.api import tmdb_docs
headers = {"Authorization": f"Bearer {os.environ['TMDB_BEARER_TOKEN']}"}
chain = APIChain.from_llm_and_api_docs(llm, tmdb_docs.TMDB_DOCS, headers=headers, verbose=True)
chain.run("Search for 'Avatar'")
