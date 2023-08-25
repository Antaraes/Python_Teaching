import csv,json
csvFilePath =  "CovidDeath.csv"
jsonFilePath = "CovidDeath.json"

data= {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for i in csvReader:
        id = i['location']
        data[id] = i

with open(jsonFilePath,'w') as jsonFile:
    jsonFile.write(json.dumps(data,indent=4)) # dumps use for string

with open(jsonFilePath,'r') as f:
    data = json.load(f)
    print(data['United States'])
