import os.path
import csv


def test_workers_are_18_years_old():
    """
    Check that all workers are 18 years old
    """
    CUR_PATH = os.path.dirname(os.path.abspath(__file__)) # get directory of current file
    with open(CUR_PATH + "/"+ "testing_dataset.csv", "r") as file:
        users = csv.DictReader(file, delimiter=",")
        workers = [user for user in users if user["status"] == "worker"]  # list comprehension to return all users that are workers
        # # same as above
        # workers = []
        # for user in users:
        #     if user["status"] == "worker":
        #         workers.append(user)
        for worker in workers:
            assert int(worker["age"]) >= 18, "Not all workers are adults"
    
test_workers_are_18_years_old()
