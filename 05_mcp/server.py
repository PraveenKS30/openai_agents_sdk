from mcp.server.fastmcp import FastMCP
import requests

# create server 
mcp = FastMCP("Weather Server")

@mcp.tool()
def get_weather(city : str)-> str :
    endpoint = "https://wttr.in"
    response = requests.get(f"{endpoint}/{city}")
    return response.text


@mcp.tool()
def add_numbers(a : int, b : int) -> int:
    return a + b

# run the server
if __name__ == "__main__":
    mcp.run()