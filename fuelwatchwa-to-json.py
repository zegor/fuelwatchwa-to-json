# Import required libraries
import json
import xmltodict
import urllib.request
import shutil

# Define FuelWatch RSS feed variables
rssBase = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS"

Product = {
    "Unleaded Petrol": 1,
    "Premium Unleaded": 2,
    "Diesel": 4,
    "LPG": 5,
    "98 RON": 6,
    "E85": 10,
    "Brand diesel": 11
}

StateRegion = {
    "Gascoyne": 1,
    "Goldfields-Esperance": 2,
    "Great Southern": 3,
    "Kimberley": 4,
    "Mid-West": 5,
    "Peel": 6,
    "Pilbara": 7,
    "South-West": 8,
    "Wheatbelt": 9,
    "Metro": 98
}

Day = {
    "today": "today",
    "tomorrow": "tomorrow", # Only available after 2:30PM
    "yesterday": "yesterday"
}

# Loop through all Products and State Regions and get today's prices
for x in Product:
    for y in StateRegion:
        rssURL = rssBase + "?Product=" + str(Product[x]) + "&StateRegion=" + str(StateRegion[y]) + "&Day=" + Day["today"]

'''
# Open FuelWatch RSS feed and save as XML file
with urllib.request.urlopen("http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS") as response, open("fuelWatchRSS.xml", "wb") as xmlSave:
    shutil.copyfileobj(response, xmlSave)

# Open FuelWatch XML file and save as JSON file
with open("fuelWatchRSS.xml") as xmlIn:
    jsonSave = json.dumps(xmltodict.parse(xmlIn.read()), indent=4)
    jsonFile = open("fuelWatchRSS.json", "w")
    jsonFile.write(jsonSave)
    jsonFile.close()
'''