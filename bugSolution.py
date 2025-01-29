def my_function(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif x == 0:
        return 1
    else:
        return x * my_function(x-1)

print(my_function(5)) # Output: 120
try:
    print(my_function(-1))
except ValueError as e:
    print(e) # Output: Factorial is not defined for negative numbers.