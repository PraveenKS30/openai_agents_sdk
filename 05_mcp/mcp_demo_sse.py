from agents import Agent , Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
import asyncio

async def run (mcp_server : MCPServer):
    agent = Agent(
        name = "Assistant",
        instructions="Use the tools to help users finding the answers.",
        mcp_servers= [mcp_server],
        model="o3-mini"
    )

    # Ask a question that reads then reasons.
    message = "How to update respository in git?"
    print(f"\n\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)


async def main():

    async with MCPServerSse(
        name = "Custom SSE server", 
        params = {
            "url": "https://gitmcp.io/docs",
        },
        cache_tools_list=True,
    ) as server:
        tools_list = await server.list_tools()
        for tool in tools_list:
            print(f"Tool : ", tool.name)
    
        
        print("Starting MCP server...")
        await run(server)

if __name__ == "__main__":
    print("Started Running..")
    asyncio.run(main())