#december 1

def testData():

    otest = open('test.txt', 'r')
    test = otest.readlines()

    oanswer = open('answer.txt', 'r')    
    answer = oanswer.readline()

    status = False
    print("Runs test data")
    result = runCode(test)

    if result == answer: #not always int
        status = True
 
    print("Correct answer: " + answer + "My answer: " + str(result))
    return status
    

def runCode(data):
    print("Runs code")
    
    answer = 'co'

    connections = {}

    for line in data:
        #print(line)
        a, b = line.strip().split('-')
        if a in connections:
            connections[a].append(b)
        else:
            connections[a] = [b]

        if b in connections:
            connections[b].append(a)
        else:
            connections[b] = [a]

    #print(connections)

    #sort dictionary after size of list
    sortedConnections = sorted(connections, key=lambda k: len(connections[k]), reverse=True)
    #print(sortedConnections)

    for sc in sortedConnections:
        print(sc + " " + str(connections[sc]))

    
    return answer

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
