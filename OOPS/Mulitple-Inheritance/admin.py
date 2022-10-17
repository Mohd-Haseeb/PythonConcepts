from curses.ascii import US
from user import User
from saveable import Saveable

class Admin(User, Saveable):
    def __init__(self, username, password, access) -> None:
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self) -> str:
        return f"<Admin {self.username}, access {self.access}>"

    
    def to_dict(self):
        return {
            'username' : self.username,
            'password' : self.password,
            'access' : self.access
        }


    # What happens when .save() method is called. It first searches the Admin, then User and atlast Saveable
    