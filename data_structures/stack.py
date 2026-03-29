class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            return None
    
    def peak(self):
        if not self.isEmpty():    
            return self.data[len(self.data)-1]
        else:
            return None
    
    def isEmpty(self):
        return len(self.data) == 0