def monkey_trouble(a, b):
    if a and b or not a and not b:
        return True
    else:
        return False

print(monkey_trouble(True, False))