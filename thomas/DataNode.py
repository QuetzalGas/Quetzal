class DataNode:
    def __init__(self, searchKey, data):
        self.searchKey = searchKey
        self.data = data

    def __del__(self):
        self.searchKey = None
        self.data = None