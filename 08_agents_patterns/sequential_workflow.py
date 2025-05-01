from agents import Agent, Runner
import asyncio

code_agent = Agent(
    name = "Code Agent",
    instructions = "You are a code agent and help in generating code in python"
)

validator_agent = Agent(
    name = "Validator Agent",
    instructions = "You are a validator agent. You will receive code from the code agent. " \
    "Your task is to validate the code and check if it is correct or not.",
)

async def main():
    message = "Write a function to calculate the factorial of a number in python."

    code_output = await Runner.run(code_agent, message)
    print(f"Code Output : {code_output.final_output}")

    validation_output = await Runner.run(
        validator_agent,
        f"Code:\n{code_output.final_output}",
    )

    print(f"Validation Output : {validation_output.final_output}")

if __name__ == "__main__":
    asyncio.run(main())