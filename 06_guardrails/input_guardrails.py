from agents import Agent, Runner, input_guardrail, RunContextWrapper, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
import asyncio
from pydantic import BaseModel, Field

class VisitInputGuardRailOutput(BaseModel):
    is_non_visit :bool
    reasoning: str


# define guardrail agent 
visit_guardrail_agent = Agent(
    name = "Visit Guardrail Check", 
    instructions= "Check if the user is asking questions other than the visits, explorations.",
    output_type = VisitInputGuardRailOutput,
)

# define guardrail agent input
@input_guardrail
async def visit_guardrail(
    ctx : RunContextWrapper, agent : Agent, input : str
        
) -> GuardrailFunctionOutput:
    result = await Runner.run(visit_guardrail_agent, input, context= ctx.context)

    return GuardrailFunctionOutput(
        output_info= result.final_output,
        tripwire_triggered= result.final_output.is_non_visit,
    )

# define agent
agent = Agent(  
    name="explorer_agent",
    instructions="""
        You are an expert in providing travel guidance to users.
        You are going to provide 2 cities name for the exploration.
    """,
    input_guardrails= [visit_guardrail]
)


async def main ():
    try :
        # run agent 
        response = await Runner.run(agent, "I like hiking, what are the best places to visit in the mountains?")
        print(response.final_output)

    except InputGuardrailTripwireTriggered :
        print("Tripwire triggered!")
   


if __name__ == "__main__":
    asyncio.run(main())