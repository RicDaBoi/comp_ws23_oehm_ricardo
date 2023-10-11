import sys
import numpy as np
import shutil
import json                                                                                                                                     #import libraries

y=[0]
iarg1=sys.argv[1]                                                                                                                               #save input-name as variable
print("Input file = \"" +iarg1 +"\"")
iarg2=sys.argv[2]                                                                                                                               #save output-name as variable
varg1=sys.argv[3]
value1=sys.argv[4]
varg2=sys.argv[5]
value2=sys.argv[6]                                                                                                                              #save commandline arguments as variables 


src=(iarg1)
dest=(iarg2)                                                                                                                                    #create output-file

with open(iarg1) as inputfile:
    inputdata = json.load(inputfile)                                                                                                            #import data from input-file

if inputdata['interval_in_minutes'] > int(value1):
    print("new interval is shorter")
elif inputdata['interval_in_minutes'] < int(value1):
    #y=[list(itertools.chain.from_iterable(itertools.repeat(x, inputdata['interval_in_minutes'] // int(value1)) for x in inputdata['data']))]

inputdata[varg1] = value1
inputdata[varg2] = value2



inputdata['data'] = y                                                                                                                           #convert data       



with open(iarg2, 'w') as outputfile:                            
    json.dump(inputdata, outputfile, ensure_ascii=False, indent=4)                                                                              #write data to output-file

print("Data conversion completed. New file saved as \"" +iarg2 +"\".")                                                                          #print final message
