from agents import Agent , Runner
from helper import User, get_user_preference

user_info = User(name = "James", weather_preference = "sunny", id = 1)

agent = Agent(
    name = "explorer_agent",
    instructions = """
        You are an expert in providing travel guidance to users.
        You are going to provide 2 cities name for the exploration.
    """,
    tools = [get_user_preference],
)


response = Runner.run_sync(agent, "Where should James go in India?" , context=user_info)
print(response.final_output)