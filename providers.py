from models.users import User
from models.users import Status
import os.path
import csv

# # this implementation described polymorfism
# # create different classed for different data sources: csv, data base, api

# class UserProvider:
#     def ger_users(self) -> list[User]:
#         raise NotImplementedError
    
# class CsvUserProvider(UserProvider):
#     def get_users(self) -> list[User]:
#         """
#         open csv file from the current direcotry
#         create a list of User objects based on data from read csv file
#         """
#         CUR_PATH = os.path.dirname(os.path.abspath(__file__)) # get directory of current file
#         with open(CUR_PATH + "/"+ "testing_dataset.csv", "r") as file:
#             users = csv.DictReader(file, delimiter=",")
#             # create users list of User objects, utilizing list comprehension
#             # for each dictionary (user) in users, create a User object with the dictionary values
#             return [User(name=user["name"], age=int(user["age"]), status=Status(user["status"]), items=user["items"]) for user in users] # return list of User objects

# class DataBaseUserProvider(UserProvider):
#     def ger_users(self) -> list[User]:
#         pass
    
# class ApiUserProvider(UserProvider):
#     def ger_users(self) -> list[User]:
#         pass