fileName = input('Enter the file name: ')
try:
    fileHandle = open(fileName)
except:
    if fileName == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print('File cannot be opened:',fileName)
        exit()
count = 0
for line in fileHandle:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fileName)