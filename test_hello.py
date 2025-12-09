import sys
sys.path.insert(0, '.')

# Direct function call
def say_hello(name: str = "World") -> str:
    return f"Hello, {name}!"

result = say_hello("Oumeima")
print(result)
