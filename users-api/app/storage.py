class UserStorage:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def list_users(self):
        return list(self.users.values())

    def get_user(self, user_id):
        return self.users.get(user_id)

    def create_user(self, name, lastname):
        user = {
            "id": self.next_id,
            "name": name,
            "lastname": lastname,
        }
        self.users[self.next_id] = user
        self.next_id += 1
        return user

    def update_user(self, user_id, name, lastname):
        self.users[user_id] = {
            "id": user_id,
            "name": name,
            "lastname": lastname,
        }

    def patch_user(self, user_id, data):
        if user_id not in self.users:
            return False
        self.users[user_id].update(data)
        return True

    def delete_user(self, user_id):
        return self.users.pop(user_id, None)