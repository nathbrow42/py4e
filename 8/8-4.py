fileName = input('Enter a file: ')
try:
    fileHandle = open(fileName)
except:
    print('Cannot open file', fileName)
    exit()
wordList = list()
for line in fileHandle:
    line = line.strip()
    line = line.split()
    for word in line:
        if word not in wordList:
            wordList.append(word)
wordList.sort()
print(wordList)