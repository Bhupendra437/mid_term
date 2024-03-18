# history.py

history = []

def add_to_history(expression, result):
    history.append({"expression": expression, "result": result})

def get_history():
    return history
