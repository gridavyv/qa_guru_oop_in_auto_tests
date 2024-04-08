import pytest
import os.path
import csv
from models.users import User
from models.users import USER_ADULT_AGE
from models.users import Status
# from providers import UserProvider
# from providers import CsvUserProvider

# def user_provider() -> UserProvider:
#     return CsvUserProvider()  # class CsvUserProvider inherit class UserProvider

# def users(user_provider: UserProvider) -> list[User]:
#     return user_provider.ger_users()

def users() -> list[User]:
    """
    open csv file from the current direcotry
    create a list of User objects based on data from read csv file
    """
    CUR_PATH = os.path.dirname(os.path.abspath(__file__)) # get directory of current file
    with open(CUR_PATH + "/"+ "testing_dataset.csv", "r") as file:
        users = csv.DictReader(file, delimiter=",")
        # create users list of User objects, utilizing list comprehension
        # for each dictionary (user) in users, create a User object with the dictionary values
        return [User(name=user["name"], age=int(user["age"]), status=Status(user["status"]), items=user["items"]) for user in users] # return list of User objects

def workers() -> list[User]:
    """
    gets list of objects "user", filter workers from users and return list of User objects
    """
    workers = [user for user in users() if user.status == Status.worker]  # list comprehension to return all users that are workers
    return workers  # return list of User objects
    

def young_users():
    # list comprehension, take on object from list of objects of User class, name them worker and 
    # add to the lsit attribute "name" of all objects (called workers) that have attribute "age" below 18
    # utilize the User class function ".is_adult()" as a condition
    young_workers = [user.name for user in workers() if not user.is_adult()]  
    return young_workers


def test_workers_are_adults_v3():
    """
    Check that all workers are adults
    """
    assert not young_users(), f"Workers {young_users()} below {USER_ADULT_AGE}"
    # # same as above
    # assert len(young_users(workers)) == 0, f"Workers {young_users(workers)} blow 18"


if __name__ == "__main__":
    """
    When the script is run as a standalone program, 
    the code under the if __name__ == "__main__" block will execute. 
    When the script is imported as a module in another script, 
    only the function and class definitions
    """
    test_workers_are_adults_v3()

