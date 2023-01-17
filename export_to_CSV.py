import xml.etree.ElementTree as ET
import csv

# Open the dobot playback file and parse the XML
tree = ET.parse(r"C:\Users\andre\Syddansk Erhvervsskole\projekt 2 mekatronikk - Dokumenter\DOBOT\2 - Kopi.playback")
root = tree.getroot()

# Create a list to store the data
data = []


# Loop through each row in the XML and add the data to the list
for row in root.findall("*"):
    row_data = []
    for item in row:
        row_data.append(item.text)
    data.append(row_data)

# Delete the last two columns and the first row
data = [row[:-2] for row in data[2:]]

print(data)

# Save the data to a CSV file
#with open("dobot_playback.csv", "w") as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerows(data)