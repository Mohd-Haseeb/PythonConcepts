from database import Database


class User:
    def __call__(self, username, password) -> None:
        self.username = username
        self.password = password

    def login(self):
        return 'Logged In!!'

    def __repr__(self) -> str:
        return f"<User {self.username}>"
