import sys
import os
import time
import random
if len(sys.argv) < 4:
    print 'argv[1]: queryFile'
    print 'argv[2]: resultDir'
    print 'argv[3]: restart'
    exit()

# read queryFile
queryFile = open(sys.argv[1],'r')
line_count = 0
while True:
    line = queryFile.readline()
    if not line:break
    line_count += 1
    if line_count < int(sys.argv[3]):continue
    query = line.strip().split('\t')
    print 'current process line: ' + query[0] 
    resultFileName = sys.argv[2] + '/' + query[0] + '.res'
    print 'result file: ' + resultFileName 
    command = 'python gsearch.py "' + query[1] + '" ' + resultFileName
    os.system(command)
    randomTime = random.randint(1,3)
    #break;
    time.sleep(randomTime)
