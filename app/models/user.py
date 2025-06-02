from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    birthdate: str
    age: int
