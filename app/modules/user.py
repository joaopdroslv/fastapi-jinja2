from faker import Faker

from app.models.user import User

faker = Faker()


def get_all_users():
    """Simulating a database connection to retrieve all users."""
    users = []
    for i in range(10):
        users.append(
            User(
                id=i + 1,
                name=faker.name(),
                email=faker.email(),
                birthdate=str(faker.date_of_birth(minimum_age=18, maximum_age=70)),
                age=faker.random_int(min=18, max=70),
            )
        )

    return users
