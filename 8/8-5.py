fileName = input('Enter a file name: ')
try:
    fileHandle = open(fileName)
except:
    print('File could not be found')
    exit()
recordCount = 0
for line in fileHandle:
    if line.startswith('From'):
        line = line.strip()
        line = line.split()
        print(line[1])
        recordCount = recordCount + 1
print('There were', recordCount,'lines in the file with From as the first word')