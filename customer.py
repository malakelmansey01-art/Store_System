from user import User

class Customer(User):
    def __init__(self, user_id, name, points=0):
        super().__init__(user_id, name)
        self.points = points

    def show_role(self):
        print("Role: Customer")