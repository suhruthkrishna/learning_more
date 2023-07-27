# Exceptions as you know are used to catch run time exceptions
try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    result = num1 / num2
except ZeroDivisionError as e:
    error = str(e)
    err = error.capitalize()
    print(err)  # prints the error statement that the console might have generated
    print("Cant divide by zero")
except ValueError as e:
    error = str(e)
    err = error.capitalize()
    print(err)
    print("Has to have the same type")
except Exception as e:
    error = str(e)
    err = error.capitalize()
    print(err)
    print("Dont know but some error")
else:  # reaches this block if except shows no errors
    print(result)
finally:  # just like java
    print("Errors handled")
