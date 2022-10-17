from admin import Admin
from database import Database

a = Admin('shabrez', 'vbgsg',1)

a.save()


user = Database.find(lambda x: x['username'] == 'shabrez')[0]
user_obj = Admin(**user)
print(user_obj.username)

