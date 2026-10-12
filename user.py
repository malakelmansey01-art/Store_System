from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def show_details(self):
        return f"ID: {self.user_id}, Name: {self.name}"

    @abstractmethod
    def show_role(self):
        pass