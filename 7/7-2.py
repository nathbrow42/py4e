fileName = input('Enter a file name: ')
fileHandle = open(fileName)
dspamCount = 0
dspamTotal = 0
for line in fileHandle:
    if line.find('X-DSPAM-Confidence:') != -1:
        confidenceValue = line[line.find(':')+1:]
        confidenceValue = float(confidenceValue)
        dspamCount = dspamCount + 1
        dspamTotal = dspamTotal + confidenceValue
print('Average spam confidence:',dspamTotal/dspamCount)