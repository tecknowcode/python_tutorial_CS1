def greet():
    print("Hi!!!! Hello World!!1")

def decidePerson():
    age_of_person = int(input("Enter age of person: "))
    if age_of_person < 18:
        print("teenager")
    elif age_of_person < 60 and age_of_person >= 18:
        print("adult")
    else:
        print("Senior Citizen")

def takeNumber():
    number = int(input("Enter a number: "))
    return number

def checkNumber(num):
    return bool(num % 2)

def checkOddEven(number):
    # number = takeNumber()
    if checkNumber(number):
        print(f"{number} - odd")
    else:
        print(f"{number} - even")    
    
def checkOddEvenList():
    upper_limit = int(input("Enter a number: "))
    for num in range(1, upper_limit + 1):
        checkOddEven(num)

def main():
    greet()
    # decidePerson()
    # checkOddEven()
    checkOddEvenList()


if __name__ == "__main__":
    main()



