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
    
    answer = 0
    wires = {}
    rules = []
    zs = ''

    for line in data:
        if ':' in line:
            a, b = line.strip().split(': ')
            wires[a] = b.strip()
        elif line == '\n':
            pass
        else:
            rules.append(line.strip())

    #print(wires)
    #print(rules)

    while rules != []:
        for rule in rules:
            #print(rule)
            a, operation, b, arrow, answer = rule.split()
            
            if a in wires and b in wires:
                if operation == 'AND':
                    value = process_and(wires[a], wires[b])
                elif operation == 'OR':
                    value = process_or(wires[a], wires[b])
                elif operation == 'XOR':
                    value = process_xor(wires[a], wires[b])

                rules.pop(rules.index(rule))

                wires[answer] = value

    #sort wires by key 
    wires = dict(sorted(wires.items()))
    for wire in wires:
        print(wire, wires[wire])
        if wire.startswith('z'):
            zs += wires[wire]

    print(zs)
    #print string backwards
    zs = zs[::-1]
    #convert binary to decimal
    answer = int(zs, 2)
    return answer

def process_and(a, b):

    if a == '1' and b == '1':
        return '1'
    else:
        return '0'

def process_or(a, b):
    
    if a == '1' or b == '1':
        return '1'
    else:
        return '0'

def process_xor(a, b):
    
    if a == b:
        return '0'
    else:
        return '1'

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
