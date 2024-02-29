def factorial(num):
    if (type(num) == int and num >= 0):
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num - 1)
    else:
        return None
    

print(factorial(5))
print(factorial(6))
print(factorial(0))
print(factorial(-2))
print(factorial(1.2))
print(factorial('Spam spam spam spam'))
