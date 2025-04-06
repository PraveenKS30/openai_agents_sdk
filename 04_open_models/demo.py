from agents import (
    AsyncOpenAI, Agent, 
    OpenAIChatCompletionsModel, 
    Runner, set_tracing_disabled, 
    RunConfig, ModelProvider, Model, 
    set_default_openai_client, 
    set_default_openai_api
    
)
import os

set_tracing_disabled(True)

""" # ollama client
client = AsyncOpenAI(
    base_url="http://localhost:11434/v1"
)

# Option 1 : Set the model at Agent instance
agent = Agent(
    name = "python agent",
    instructions = "You are a helpful assistant that helps with Python programming.",
    model = OpenAIChatCompletionsModel(
        model = "llama3.2",
        openai_client= client
    )
)

result = Runner.run_sync(agent, "Write a function that takes a list of numbers and returns the sum.")
print(result.final_output) """


""" # Option 2 : Set the model at Runner instance
client = AsyncOpenAI(
    base_url="http://localhost:11434/v1"
)

class CustomModelProvider(ModelProvider):
    def get_model(self, model_name: str | None) -> Model:
        return OpenAIChatCompletionsModel(
            model = "llama3.2",
            openai_client= client
        )
    
CUSTOM_MODEL_PROVIDER = CustomModelProvider()

agent = Agent(
    name = "python agent",
    instructions = "You are a helpful assistant that helps with Python programming.",
)

result = Runner.run_sync(agent, "Write a function that takes a list of numbers and returns the sum.",
                         run_config = RunConfig(model_provider= CUSTOM_MODEL_PROVIDER))
print(result.final_output) """


""" # option 3 : Set the client at the global instance 
client = AsyncOpenAI(
    base_url="http://localhost:11434/v1"
)

set_default_openai_client(client)
set_default_openai_api("chat_completions")


agent = Agent(
    name = "python agent",
    instructions = "You are a helpful assistant that helps with Python programming.",
    model = "llama3.2"
)

result = Runner.run_sync(agent, "Write a function that takes a list of numbers and returns the sum.")
print(result.final_output) """


# Option 4 : Set the model at Agent instance using Groq
client = AsyncOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


agent = Agent(
    name = "python agent",
    instructions = "You are a helpful assistant that helps with Python programming.",
    model = OpenAIChatCompletionsModel(
        model = "llama-3.3-70b-versatile",
        openai_client= client
    )
)

result = Runner.run_sync(agent, "Write a function that takes a list of numbers and returns the sum.")
print(result.final_output)







