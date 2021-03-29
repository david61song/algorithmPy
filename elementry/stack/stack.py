

class stack:
    
    def __init__(self):
        self.array = []
    
    def push(self,data):
        self.array.append(data)
    
    def pop(self):
        return self.array.pop()


mystack = stack()

mystack.push(33)
mystack.push(44)


