from agents import Agent , Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerStdio
import asyncio, os, shutil

async def run (file_mcp_server, time_mcp_server):
    agent = Agent(
        name = "Assistant",
        instructions="Use the tools to help users finding the answers.",
        mcp_servers= [file_mcp_server, time_mcp_server],
        model="o3-mini"
    )

    # Ask a question that reads then reasons.
    message = "Look at my favorite songs. Suggest one new song that I might like"
    print(f"\n\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)

      # Ask a question that reads then reasons.
    message = "When it's 4 PM in New York, what time is it in London?"
    print(f"\n\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)


async def main():

    async with MCPServerStdio(
        name = "FileSystem server", 
        params = {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "sample_files"]
        },
        cache_tools_list=True,
    ) as file_mcp_server, MCPServerStdio(
        name = "Time server", 
        params = {
            "command": "python",
            "args": ["-m", "mcp_server_time", "--local-timezone=America/New_York"]
        },
        cache_tools_list=True,
    ) as time_mcp_server:
    
        
        print("Starting MCP server...")
        await run(file_mcp_server, time_mcp_server)

if __name__ == "__main__":
    print("Started Running..")
    asyncio.run(main())