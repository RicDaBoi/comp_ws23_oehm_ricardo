import json

inputfile = open('example.json')
inputdata = json.load(inputfile)

for x in inputdata:
    print(x)

inputfile.close()