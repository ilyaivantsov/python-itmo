from src.database import Db
from src.user.user_model import UserModel
from faker import Faker

us = Db[UserModel]()

for _ in range(10):
    fake = Faker()
    user = UserModel(
        username=fake.user_name(),
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        password=fake.password(),
    )
    us.insert(user)

print(us.fetch())


def get_user_service():
    return us
