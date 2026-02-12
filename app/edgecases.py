# 1. Empty function
def empty():
    pass


# 2. One-line function
def add(a, b): return a + b


# 3. Function with no return
def print_name(name):
    print(name)


# 4. Function with type hints
def multiply(a: int, b: int) -> int:
    return a * b


# 5. Function with default values
def greet(name="Guest"):
    return f"Hello {name}"


# 6. *args and **kwargs
def flexible(*args, **kwargs):
    return args, kwargs


# 7. Nested function
def outer():
    def inner():
        return "inside"
    return inner()


# 8. Async method
class APIClient:
    async def fetch(self, url):
        return {"data": url}


# 9. Class without methods
class Empty:
    pass


# 10. Property method
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
