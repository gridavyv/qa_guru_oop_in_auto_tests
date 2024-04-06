import os.path
import csv


def test_workers_are_18_years_old(workers):
    """
    Check that all workers are 18 years old
    """
    for worker in workers:
        assert int(worker["age"]) >= 10, "Not all workers are adults"
    
test_workers_are_18_years_old()
