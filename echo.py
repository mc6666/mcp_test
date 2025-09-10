from fastmcp import FastMCP

# Create server
mcp = FastMCP("Echo Server")

@mcp.tool
def echo_tool(text: str) -> str:
    """Echo the input text"""
    return text
    
# 執行主程式
if __name__ == "__main__":
    mcp.run(transport="http", port=8000)