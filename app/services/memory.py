class Memory:
    def __init__(self):
        self.data = {}

    def get(self, user_id):
        return self.data.get(user_id, "")

    def update(self, user_id, message, response):
        prev = self.data.get(user_id, "")
        self.data[user_id] = prev + f"\nUser: {message}\nBot: {response}"