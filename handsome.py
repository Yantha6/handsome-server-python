from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("handsome")

@mcp.tool()
async def who_is_handsome() -> str:
    """Return who is the most handsome person."""
    return "杨天涵 is the most handsome person in the world! 😊"

def main():
    # Initialize and run the server
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()