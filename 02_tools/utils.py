from agents import Agent, Runner
from tools import get_current_weather
from pydantic import BaseModel 

class Weather(BaseModel):
    location : str
    temperature : float

# create agent 
agent = Agent(
    name = "weather_agent",
    instructions = " You are an expert in providing weather information",
    tools = [get_current_weather],
    model = "gpt-4o-mini",
    output_type= Weather
)

response = Runner.run_sync(agent, "What is the weather in London?")

print(response.final_output)