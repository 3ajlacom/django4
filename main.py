from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="sayHello")

@mcp.tool()
def say_hello(name: str = "World") -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

@mcp.tool()
def add(a: float, b: float) -> float:
    """Addition de deux nombres"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Soustraction de deux nombres"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplication de deux nombres"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Division de deux nombres"""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

if __name__ == "__main__":
    mcp.run()
