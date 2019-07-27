import json
import xmltodict
with open("fuelWatchRSS.xml") as xmlFile:
    doc = json.dumps(xmltodict.parse(xmlFile.read()), indent=4)
print(doc)