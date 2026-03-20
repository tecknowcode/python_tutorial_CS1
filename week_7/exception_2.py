from exception import MyException
import sys
from logger import logging

def main():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2
        print("Result:", result)

    except Exception as e:
        raise MyException(e, sys)

if __name__=="__main__":
    main()

