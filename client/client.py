import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    # Configuration to run the Docker container
    # We use 'docker run' with '-i' (interactive) to keep stdin open
    server_params = StdioServerParameters(
        command="docker",
        args=["run", "-i", "--rm", "mcp-docker-demo"],
        env=None
    )

    print("Starting Docker container and connecting...")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(f"\nConnected! Found {len(tools.tools)} tools:")
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            # Call the 'add' tool
            print("\nCalling 'add' tool with x=10, y=20...")
            result = await session.call_tool("add", arguments={"x": 10, "y": 20})
            print(f"Result: {result.content[0].text}")

            # Call the 'get_environment_info' tool
            print("\nCalling 'get_environment_info' tool...")
            info = await session.call_tool("get_environment_info", arguments={})
            print(f"Environment Info:\n{info.content[0].text}")

if __name__ == "__main__":
    # Check if image exists (optional manual check reminder)
    print("Ensure you have built the image: 'docker build -t mcp-docker-demo ..'")
    asyncio.run(run())
