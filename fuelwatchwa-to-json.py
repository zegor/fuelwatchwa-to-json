# Import required libraries
import datetime
import json
import xmltodict
import urllib.request
import shutil

# Store dates
todayDate = datetime.date.today()
tomorrowDate = todayDate + datetime.timedelta(days=1)

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

# Loop through all Products and State Regions and get tomorrow's prices
for x in Product:
    for y in StateRegion:
        rssURL = rssBase + "?Product=" + str(Product[x]) + "&StateRegion=" + str(StateRegion[y]) + "&Day=" + Day["tomorrow"]

        # Open FuelWatch RSS feed and save as XML file
        pathXML = "files/xml/" + str(tomorrowDate) + "/fuelWatchRSS_" + x + "_" + y + ".xml"
        with urllib.request.urlopen(rssURL) as response, open(pathXML, "wb") as saveXML:
            shutil.copyfileobj(response, saveXML)

        # Open FuelWatch XML file and save as JSON file
        pathJSON = "files/json/" + str(tomorrowDate) + "/fuelWatchRSS_" + x + "_" + y + ".json"
        with open(pathXML) as inXML:
            inJSON = json.dumps(xmltodict.parse(inXML.read()), indent=4)
            saveJSON = open(pathJSON, "w")
            saveJSON.write(inJSON)
            saveJSON.close()