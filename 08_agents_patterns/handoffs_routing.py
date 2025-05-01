from agents import Agent , Runner

# python agent 
python_agent = Agent(
    name = "python_agent",
    instructions= "You are an expert in Python programming language.",
    handoff_description= "Specialist in Python programming language"
)

# java agent 
java_agent = Agent(
    name = "java_agent",
    instructions= "You are an expert in Java programming language.",
    handoff_description= "Specialist in Java programming language"
)

# routing agent
routing_agent = Agent(
    name = "routing_agent",
    instructions= "You need to determine which agent to use based on the given query",
    handoffs=[python_agent, java_agent]

)

# run the agent
response = Runner.run_sync(routing_agent, "How to handle execeptions in Java?")
print(response.last_agent)
print(response.final_output)



