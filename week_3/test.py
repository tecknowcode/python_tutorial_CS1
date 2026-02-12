def countListElements(lst):  #[1,2,2,3,3,3]
    output = {}
    for val in lst:
        if val in output:
            output[val] = output[val] + 1
        else:
            output[val] = 1
    return output

def calculateAverage(marks):
    return round(sum(marks)/len(marks),2)

def calculateAverageScore(data):
    result = {}
    for name,marks in data:
        result[name.lower()] = calculateAverage(marks)
    return result

def main():
    input1 = [1,2,2,3,3,3]
    input2 = [4,1,6,5,4,5,5,1,4]
    result = countListElements(input1)
    print(result)
    student = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
    print(calculateAverageScore(student))

if __name__ == "__main__":
    main()

