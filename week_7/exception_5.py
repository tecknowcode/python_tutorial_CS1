class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError("Negative number is not allowed")

    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Error:", e)