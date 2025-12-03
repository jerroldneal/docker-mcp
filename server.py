from mcp.server.fastmcp import FastMCP
import platform
import os
import sys

mcp = FastMCP("Dockerized Tool")

@mcp.tool()
def add(x: int, y: int) -> int:
    """Add two numbers"""
    return x + y

@mcp.tool()
def get_environment_info() -> dict:
    """Returns information about the running environment (OS, Python version)"""
    return {
        "platform": platform.platform(),
        "node": platform.node(),
        "os_name": os.name,
        "python_version": sys.version,
        "cwd": os.getcwd()
    }

if __name__ == "__main__":
    mcp.run()
