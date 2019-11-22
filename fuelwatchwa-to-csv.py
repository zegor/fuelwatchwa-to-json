# Import required libraries
import datetime
import csv
import urllib.request
import shutil
import xml.etree.ElementTree as et

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

# Declare CSV file path
pathCSV = "files/csv/" + str(tomorrowDate) + "/fuelWatchRSS_" + str(tomorrowDate) + ".csv"

# Open FuelWatch CSV file for writing and create writer object
saveCSV = open(pathCSV, "w", newline="\n", encoding="utf-8")
saveCSVWriter = csv.writer(saveCSV, quoting=csv.QUOTE_ALL)

# Declare empty FuelWatch stations list
fwStations = [["date", "product", "brand", "price", "trading-name", "location", "address", "phone", "latitude", "longitude"]]

# Loop through all Products and State Regions and get tomorrow's prices
for x in Product:
    for y in StateRegion:
        rssURL = rssBase + "?Product=" + str(Product[x]) + "&StateRegion=" + str(StateRegion[y]) + "&Day=" + Day["tomorrow"]

        # Open FuelWatch RSS feed and save as XML file
        pathXML = "files/xml/" + str(tomorrowDate) + "/fuelWatchRSS_" + x + "_" + y + ".xml"
        with urllib.request.urlopen(rssURL) as response, open(pathXML, "wb") as saveXML:
            shutil.copyfileobj(response, saveXML)

        # Open FuelWatch XML file and store required data for saving as CSV
        with open(pathXML) as inXML:
            # Parse XML tree and declare root XML variable
            treeXML = et.parse(inXML)
            rootXML = treeXML.getroot()

            # Loop through items (i.e. stations) in XML and extract required values
            for item in rootXML.find("channel").findall("item"):
                fwItem = []
                fwItem.append(str(tomorrowDate))
                fwItem.append(x)
                fwItem.append(item.find("brand").text)
                fwItem.append(item.find("price").text)
                fwItem.append(item.find("trading-name").text)
                fwItem.append(item.find("location").text)
                fwItem.append(item.find("address").text)
                fwItem.append(item.find("phone").text)
                fwItem.append(item.find("latitude").text)
                fwItem.append(item.find("longitude").text)

                # Append station values to FuelWatch stations list
                fwStations.append(fwItem)
            
# Write rows to CSV file
saveCSVWriter.writerows(fwStations)

# Close CSV file
saveCSV.close()