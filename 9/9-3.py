fileName = input('Enter a file name: ')
try:
    fileHandle = open(fileName)
except:
    print("File not found")
    exit()
emailCounts = dict()
for line in fileHandle:
    if line.startswith('From '):
        words = line.split()        
        emailCounts[words[1]] = emailCounts.get(words[1],0) + 1
print(emailCounts)