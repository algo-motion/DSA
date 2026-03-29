from data_structures.stack import Stack

def isValid(str):
    valid_map = {"{": "}", "(" : ")", "[" : "]"}
    stack = Stack()
    for ch in str:
        if ch in valid_map:
            stack.push(ch)
        elif valid_map.get(stack.pop()) != ch:
            return False
    if stack.isEmpty():
        return True
    else:
        return False