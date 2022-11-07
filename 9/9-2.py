fileName = input('Enter a file name: ')
try:
    fileHandle = open(fileName)
except:
    print("File not found")
    exit()
dayCount = dict()
for line in fileHandle:
    if line.startswith('From '):
        words = line.split()        
        dayCount[words[2]] = dayCount.get(words[2],0) + 1
print(dayCount)