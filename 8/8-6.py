numList = list()
while True:
    userInput = input("Enter a number: ")
    try:
        userInput = float(userInput)
    except:
        if userInput == 'done':
            break
        else:
            print(userInput, 'is not a number')
            continue
    numList.append(userInput)
print('Maximum:',max(numList))
print('Minimum:', min(numList))