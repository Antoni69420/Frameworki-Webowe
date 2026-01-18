class UsersStorage:
    def __init__(self):
        self._users = []
        self._next_id = 1

    def get_all(self):
        return self._users

    def get_by_id(self, user_id):
        return next((u for u in self._users if u["id"] == user_id), None)

    def create(self, name, lastname):
        user = {"id": self._next_id, "name": name, "lastname": lastname}
        self._users.append(user)
        self._next_id += 1
        return user

    def update(self, user_id, name, lastname):
        user = self.get_by_id(user_id)
        if user:
            user["name"] = name
            user["lastname"] = lastname
        else:
            self._users.append({"id": user_id, "name": name, "lastname": lastname})

    def patch(self, user_id, data):
        user = self.get_by_id(user_id)
        if not user:
            return False
        user.update(data)
        return True

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        if not user:
            return False
        self._users.remove(user)
        return True
