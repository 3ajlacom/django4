"""Test des fonctions mathématiques du serveur MCP"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

# Tests
print("=== Tests des fonctions mathématiques ===\n")

print(f"Addition: 10 + 5 = {add(10, 5)}")
print(f"Soustraction: 10 - 5 = {subtract(10, 5)}")
print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
print(f"Division: 10 / 5 = {divide(10, 5)}")

print("\n=== Tests avec décimaux ===\n")
print(f"Addition: 7.5 + 2.3 = {add(7.5, 2.3)}")
print(f"Soustraction: 7.5 - 2.3 = {subtract(7.5, 2.3)}")
print(f"Multiplication: 7.5 * 2.3 = {multiply(7.5, 2.3)}")
print(f"Division: 7.5 / 2.3 = {divide(7.5, 2.3)}")

print("\n=== Test division par zéro ===\n")
try:
    divide(10, 0)
except ValueError as e:
    print(f"Erreur capturée: {e}")


if __name__ == "__main__":
    mcp.run(transport="stdio")
