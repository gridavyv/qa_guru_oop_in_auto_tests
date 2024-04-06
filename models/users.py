from dataclasses import dataclass

@dataclass  # decprator
class User:
    name: str
    age: int
    status: str
    items: list[str]



# # smae as above
# class User:
#     """
#     name: str
#     age: int
#     status: str
#     items: list[str]
#     """
#     def __init__(self, name: str, age: int, status: str, items: list[str]) -> None:
#         self.name = name
#         self.age = age
#         self.status = status
#         self.items = items

#     def __eq__(self, other) -> bool:
#         """
#         The __eq__ method is used to compare two objects for equality.
#         This function will wil call when we use the == operator to compare two objects.
        
#         """
#         return self.name == other.name and self.age == other.age and self.status == other.status and self.items == other.items


if __name__ == "__main__":
    """
    When the script is run as a standalone program, 
    the code under the if __name__ == "__main__" block will execute. 
    When the script is imported as a module in another script, 
    only the function and class definitions will be imported, 
    and the code under the if __name__ == "__main__" block will not execute.
    """
    # d = {"name": "Mike", "age": 16, "status": "student", "items": ["pen", "book"]}
    mike_1 = User(name="Mike", age=16, status="student", items=["pen", "book"])
    mike_2 = User(name="Mike", age=16, status="student", items=["pen", "book"])
    # assert mike.age == 20, f"{mike.name} is not 20"
    assert mike_1 == mike_2, f"{mike_1.name} is not equal to {mike_2.name}"
