import json

def writeToFile(parameter):
    with open(parameter, 'w') as toFile:
        json.dump(data, toFile, sort_keys=True, indent=4)
        
def readFile(parameter):
    with open(parameter) as inFile:
        data = json.load(inFile)
    
    return data 

