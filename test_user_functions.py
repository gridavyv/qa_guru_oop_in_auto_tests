import pytest
import os.path
import csv

USER_ADULT_AGE = 18

@pytest.fixture
def users():
    """
    open csv file from the current direcotry
    """
    CUR_PATH = os.path.dirname(os.path.abspath(__file__)) # get directory of current file
    with open(CUR_PATH + "/"+ "testing_dataset.csv", "r") as file:
        users = csv.DictReader(file, delimiter=",")
        users = list(users)
    return users


@pytest.fixture
def workers(users):
    """
    filter workers from users
    """
    workers = [user for user in users if user["status"] == "worker"]  # list comprehension to return all users that are workers
    # # same as above
    # workers = []
    # for user in users:
    #     if user["status"] == "worker":
    #         workers.append(user)
    return workers
    

def young_users(workers):
    young_users = []
    for worker in workers:
        if int(worker["age"]) < USER_ADULT_AGE:
            young_users.append(worker["name"])
    return young_users


def test_workers_are_adults(workers):
    f"""
    Check that all workers are {USER_ADULT_AGE} years old
    """
    assert not young_users(workers), f"Workers {young_users(workers)} blow {USER_ADULT_AGE}"
    # # same as above
    # assert len(young_users(workers)) == 0, f"Workers {young_users(workers)} blow 18"