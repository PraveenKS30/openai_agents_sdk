from agents import Agent, Runner
import asyncio


# define agents
german_4o_agent = Agent(
    name= "German Language Agent",
    instructions = "You are an expert in German. You need to translate the given input in German.",
    model = "gpt-4o-mini"
)

german_o3_agent = Agent(
    name= "German Language Agent",
    instructions = "You are an expert in German. You need to translate the given input in German.",
    model = "o3-mini"
)

judge_agent = Agent(
    name = "Judge Agent",
    instructions = "You are a judge agent. You will receive answers from other agents. " \
    "Your task is to evaluate the answers and pick the best one.",
)

async def main():

    message = "Hello, how are you? It has been a long time since we last met. " \
        "I hope you are doing well. I wanted to catch up with you and see how things are going."

    out_1, out_2 = await asyncio.gather (
        Runner.run(german_4o_agent, message),
        Runner.run(german_o3_agent, message),
    )

    print(out_1.final_output)
    print(out_2.final_output)

    translations = "\n\n".join([out_1.final_output, out_2.final_output])
    #print(translations)

    best_translation = await Runner.run(
        judge_agent,
        f"Input: {message}\n\nTranslations:\n{translations}",

    )

    print(f"Best Translation : {best_translation.final_output}")

if __name__ == "__main__":
    asyncio.run(main())