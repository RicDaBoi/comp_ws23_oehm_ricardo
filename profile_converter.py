import sys
import shutil
import json                                                                                                                                         #import libraries

if len(sys.argv) < 7:
    print("Error: Missing arguments.")
else:

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

        y=[]
        z=int(inputdata['interval_in_minutes'])
   
        print("Converting data...")

    if z > int(value1):                                                                                                                             #convert data 
        z=z // int(value1)  
        for x in inputdata['data']:
            y.extend([x] * z)
    
    elif z < int(value1):                                                                                                                                   
        z=int(value1) // z
        for x in range(len(inputdata['data']) - (z-1)):
            a=sum(inputdata['data'][x:x+z]) / z
            y.append(a)
    

    inputdata[varg1] = int(value1)                                                                                                                  #write data to file
    inputdata[varg2] = str(value2)



    inputdata['data'] = y                                                                                                                                 



    with open(iarg2, 'w') as outputfile:                            
        json.dump(inputdata, outputfile, ensure_ascii=False, indent=4)                                                                              #dump output-file

    print("Data conversion completed. New file saved as \"" +iarg2 +"\".")                                                                          #print final message
