import argparse
import shutil
import json                                                                                                                                         #import libraries

parser=argparse.ArgumentParser()
parser.add_argument("input", help="the path to the input file")
parser.add_argument("output", help="the path to the output file")
parser.add_argument("interval", help="the interval that should be used")
parser.add_argument("unit", help="the unit that should be used")
args = parser.parse_args()


inarg=args.input                                                                                                                                    #save input-name as variable
print("Input file = \"" +inarg +"\"")
outarg=args.output                                                                                                                                  #save output-name as variable
intervalarg=str(args.interval).split(" ")[0]
outinterval=str(args.interval).split(" ")[1]
unitarg=str(args.unit).split(" ")[0]
outunit=str(args.unit).split(" ")[1]                                                                                                                #save commandline arguments as variables 




def main():
    print("Converting data...")
    inputdata, y=ConvertInterval()
    y=ConvertUnit(inputdata, y)
    Finalizing(inputdata, y)




def ConvertInterval():

    src=(inarg)
    dest=(outarg)                                                                                                                                   #create output-file

    with open(inarg) as inputfile:
        inputdata = json.load(inputfile)                                                                                                            #import data from input-file

        y=[]
        z=int(inputdata['interval_in_minutes'])
   
        

    if z > int(outinterval):                                                                                                                        #convert interval
        z=z // int(outinterval)  
        for x in inputdata['data']:
            y.extend([x] * z)
    
    elif z < int(outinterval):                                                                                                                                   
        z=int(outinterval) // z
        for x in range(len(inputdata['data']) - (z-1)):
            a=sum(inputdata['data'][x:x+z]) / z
            y.append(a)

    else: y=inputdata['data']

    return inputdata, y



def ConvertUnit(inputdata, y):

    z=str(inputdata['unit'])
    x=[]

    if z.lower()==outunit.lower():
        x=y
        return x
    
    elif z.lower()=="kwh" and outunit.lower()!="kwh":                                                                                                  #convert unit
        x=[i*3600000 for i in y]
        

    elif z.lower()=="wh" and outunit.lower()!="wh":
        x=[i*3600 for i in y]
        
    elif z.lower()=="kj" and outunit.lower()!="kj":
        x=[i*1000 for i in y]
       
    elif z.lower()=="j" and outunit.lower()!="j":
        x=y
    
    
    if outunit.lower()=="kwh" and z.lower()!="kwh":
        x=[i/3600000 for i in y]
            
    elif outunit.lower()=="wh" and z.lower()!="wh":
        x=[i/3600 for i in y]
            
    elif outunit.lower()=="kj" and z.lower()!="kj":
        x=[i/1000 for i in y]
    
    else: x=0
    

    return x


def Finalizing(inputdata, y):

    if y!=0:

        inputdata[intervalarg + "_in_minutes"] = int(outinterval)                                                                                       #write data to file
        inputdata[unitarg] = str(outunit)



        inputdata['data'] = y                                                                                                                                 



        with open(outarg, 'w') as outputfile:                            
            json.dump(inputdata, outputfile, ensure_ascii=False, indent=4)                                                                              #dump output-file

        print("Data conversion completed. New file saved as \"" +outarg +"\".")                                                                         #print final message

    else:
        print("Error: Unit not supported.")



main()