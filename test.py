def factorial_recursive(n):
    print("asf")
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)
    
num = 3
print(factorial_recursive(num))
