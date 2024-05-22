class DAOAdapter:
    def __init__(self):
        self.data = []

    def create(self, obj):
        self.data.append(obj)

    def read(self, ID):
        for item in self.data:
            if item.ID == ID:
                return item
        return None

    def update(self, ID, **kwargs):
        item = self.read(ID)
        if item:
            for key, value in kwargs.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            return True
        return False

    def delete(self, ID):
        item = self.read(ID)
        if item:
            self.data.remove(item)
            return True
        return False
