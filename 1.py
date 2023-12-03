#december 1

def testData():

    otest = open('test.txt', 'r')
    test = otest.readlines()

    oanswer = open('answer.txt', 'r')    
    answer = oanswer.readline()

    status = False
    print("Runs test data")
    result = runCode(test)

    if result == int(answer): #not always int
        status = True
 
    print("Correct answer: " + answer + "My answer: " + str(result))
    return status
    

def runCode(data):
    print("Runs code")
    
    numbers = []

    #a list of numbers
    for line in data:
        print(line)
        number1 = ''

        for char in line:
            if char.isdigit():
                number1+=char
                break

        rev = ''.join(reversed(line))
        print(rev)

        for c in rev:
            print(c)
            if c.isdigit():
                number1+=c
                break

        numbers.append(int(number1))

        print(numbers)
    total = sum(numbers)
    return total

#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.readlines()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
