from agents import (
    Agent, OpenAIChatCompletionsModel, Runner, 
    set_default_openai_client, 
    set_default_openai_api, 
    set_tracing_disabled
)

from openai import AsyncAzureOpenAI
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("azure_openai_api_key")

# client 
client = AsyncAzureOpenAI(
    api_version = "2024-12-01-preview",
    azure_endpoint= "https://az-openai-3008.openai.azure.com/",
    api_key= api_key

)

set_default_openai_client(client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)



agent = Agent(
    name = "Explorer Agent",
    instructions = "You are an explorer agent which helps in identifying the best 2 mysterious places to visit.",
    model = "gpt-4o-mini"
)


response = Runner.run_sync(agent, "I am in India. Suggest some places to visit.")
print(response.final_output)