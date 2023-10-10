import shutil
import json                                                                 #import libraries

src=('example.json')
dest=('output.json')                                                        #create output-file

with open('example.json') as inputfile:
    inputdata = json.load(inputfile)                                        #import data from input-file

for x in inputdata:
    if x[0]:
        y = 'SusWha'
        



with open('output.json', 'w') as outputfile:                            
    json.dump(inputdata, outputfile, ensure_ascii=False, indent=4)          #write data to output-file













#print(inputdata)
#for x in inputdata:
    #print(x)
