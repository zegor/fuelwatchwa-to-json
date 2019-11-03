import json
import xmltodict
import urllib.request
import shutil

# Open FuelWatch RSS feed and save as XML file
with urllib.request.urlopen("http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS") as response, open("fuelWatchRSS.xml", "wb") as xmlSave:
    shutil.copyfileobj(response, xmlSave)

# Open FuelWatch XML file and save as JSON file
with open("fuelWatchRSS.xml") as xmlIn:
    jsonSave = json.dumps(xmltodict.parse(xmlIn.read()), indent=4)
    jsonFile = open("fuelWatchRSS.json", "w")
    jsonFile.write(jsonSave)
    jsonFile.close()