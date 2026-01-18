from app.storage import UsersStorage


def test_create_user():
    storage = UsersStorage()
    user = storage.create("Jan", "Kowalski")
    assert user["id"] == 1


def test_delete_user():
    storage = UsersStorage()
    storage.create("Jan", "Kowalski")
    assert storage.delete(1) is True
