from app.config.database import user_collection

class UserRepository:
    def __init__(self, collection=user_collection):
        self.collection = collection

    def find_by_email(self, email: str):
        return self.collection.find_one({"email": email})

    def create_user(self, user_data: dict):
        return self.collection.insert_one(user_data)