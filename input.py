from typing import List


class BaseModel:
    """
    Base class for all models, providing a basic structure
    for data storage and retrieval.
    """
    pass


class Student(BaseModel):
    """
    Represents a student with a name and a list of marks.
    """

    def __init__(self, name: str, marks: List[int] = None):
        """
        Initialize a student with name and optional marks list.
        """
        self.name = name
        self.marks = marks or []

    @staticmethod
    def grade(score: int) -> str:
        """
        Return grade based on score.
        'A' if score > 90, otherwise 'B'.
        """
        return "A" if score > 90 else "B"

    @classmethod
    def create_default(cls):
        """
        Create a default student with name 'Unknown'
        and an empty marks list.
        """
        return cls("Unknown", [])

    def average(self) -> float:
        """
        Calculate and return average marks.
        Returns 0.0 if no marks are present.
        """
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)


def outer_function(x: int):
    """
    Demonstrates a nested function.
    """

    def inner_function(y: int):
        """
        Multiply input by 2.
        """
        return y * 2

    return inner_function(x)


async def fetch_data(url: str):
    """
    Simulate async data fetch.
    """
    return {"status": "ok", "url": url}
