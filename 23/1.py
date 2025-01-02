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

    #print(data)
    
    answer = 0

    connections = {}
    three = []

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

    for key in connections:
        for k in connections[key]:
            if k in connections:
                for x in connections[key]:
                    if x in connections[k]:
                        l = [key, k, x]
                        l.sort()
                        if l not in three:
                            if key.startswith('t') or k.startswith('t') or x.startswith('t'):
                                answer += 1
                                three.append(l)

    print(len(three))
    print(three)
    
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
