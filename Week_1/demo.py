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

def main():
    greet()
    decidePerson()

if __name__ == "__main__":
    main()



