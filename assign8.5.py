try:
    fh=open('mbox-short.txt')
except:
    print('Error')
    exit()
count = 0
for line in fh:
    if line.startswith('From: '):
        lineSplit = line.split()
        print (lineSplit[1])
        count = count + 1

print ('count')
