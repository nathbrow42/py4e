fileName = input('Enter a file name: ')
fileHandle = open(fileName)
for line in fileHandle:
    line = line.strip()
    print(line.upper())