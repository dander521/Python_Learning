#coding:utf-8

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again   ")
#

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        # raise
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 0)