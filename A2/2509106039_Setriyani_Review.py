# class Repository:
#     def __add__(self, velue):
#         pass
    
#     def remove(self):
#         pass
    
# class UserRepository(Repository):
#     def add(self, velue):
#         print("Add User")
        
#     def remove(self, value):
#         print("Remove User")
from abc import ABC, abstractmethod

class UserRepositor(ABC):
    @abstractmethod
    def add(self, value):
        pass
    
class UserRepositoryImplSql(UserRepositor):
    def add(self, value):
        print(f"add user sql {value}")
        
class UserRepositoryImplPortgreSql(UserRepositor):
    def add(self, value):
        print("add user postgresql")

class UserService():
    def __init__(self, user_repository):
        self.user_repository = UserRepositoryImplSql
    
    def add_user(self):
        self.user_repository.add("Eko")  
        
user_repo = UserRepositoryImplSql()