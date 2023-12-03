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
	lettersfront = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	lettersback = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
	indexesfront = {}
	indexesback = {}
	
	convertfront = {'one':'1', 'two'*'2', 'three''3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
	convertback = {'eno':'1', 'owt':'2', 'eerht':'3', 'ruof':'4', 'evif':'5', 'xis':'6', 'neves':'7', 'thgie':'8', 'enin':'9'}


    #a list of numbers
    for line in data:
        print(line)
        number1 = ''

        for char in line:
            if char.isdigit():
                #number1+=char
				indexesfront[line.index(char)] = char
                break
				
		for let in lettersfront:
			if let in line:
				indexesfront[line.index(let)] = let

        rev = ''.join(reversed(line))
        print(rev)

        for c in rev:
            print(c)
            if c.isdigit():
                #number1+=c
				indexesback[line.index(c)] = c
                break
				
		for l in lettersback:
			if l in line:
				indexesback[line.index(l)] = l


		first = min(indexesfront.keys())
		last = min(indexesback.keys())
		print(first, last)
		
		if first.isdigit():
			pass
		else:
			f = convertfront[first]

		if last.isdigit():
			pass
		else:
			la = convertback[last]

		numbers.append(int(first))
		numbers.append(int(last))

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
