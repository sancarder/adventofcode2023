#december 1

def testData():

    otest = open('test.txt', 'r')
    test = otest.read()

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
    
    rows = []

    fits = 0

    keys = []
    locks = []

    all_keys = []
    all_locks = []

    #print(data)
    schematics = data.split('\n\n') # A list with schematics as strings

    for schem in schematics:
        if schem[0] == '#':
            locks.append(schem)
        elif schem[0] == '.':
            keys.append(schem)

    #print(locks)
    #print(keys)

    for lock in locks:
        lock_heights = calc_lock(lock)
        all_locks.append(lock_heights)

    for key in keys:
        key_heights = calc_key(key)
        all_keys.append(key_heights)

    total = len(lock_heights)

    for key in all_keys:
        for lock in all_locks:
            fits += check_fit(key, lock, total)

    print(fits)
    return fits

def check_fit(key, lock, total):
    print(key, lock, total)
    for j in range(len(lock)):
        if int(lock[j]) + int(key[j]) > total:
            return 0
    return 1

def calc_lock(lock):

    rows = lock.split('\n')

    #print(rows)
    pin_heights = []    

    columns = []
    nr_of_cols = len(rows)

    for i in range(nr_of_cols):
        columns.append([])

    for line in rows:
        for j in range(len(line)):
            columns[j].append(line[j])

    for col in columns:
        for c in col:
            if c == '.':
                pin = col.index(c)-1
                #print(c, pin)
                pin_heights.append(pin)
                break
    print(pin_heights)

    return pin_heights

def calc_key(key):

    rows = key.split('\n')

    #print(rows)
    pin_heights = []  
 
    columns = []
    nr_of_cols = len(rows)

    for i in range(nr_of_cols):
        columns.append([])

    for line in rows:
        for j in range(len(line)):
            columns[j].append(line[j])

    for col in columns:
        for c in col:
            if c == '#':
                pin = col.index(c)-1
                #print(c, pin)
                pin_heights.append(5-pin)
                break
    print(pin_heights)

    return pin_heights

#Runs testdata
testResult = testData()

if testResult == True:
    print("Test data parsed. Tries to run puzzle.")
    opuzzle = open('input.txt', 'r')
    puzzle = opuzzle.read()
    finalResult = runCode(puzzle)
    print(finalResult)
else:
    print("Test data failed. Code is not correct. Try again.")
