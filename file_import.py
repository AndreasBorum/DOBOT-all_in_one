import xml.etree.ElementTree as ET

def import_playback(filename):
    # Open the dobot playback file and parse the XML
    tree = ET.parse(filename)
    root = tree.getroot()

    # Create a list to store the data
    data = []


    # Loop through each row in the XML and add the data to the list
    for row in root.findall("*"):
        row_data = []
        for item in row:
            row_data.append(item.text)
        data.append(row_data)
        if row_data[-1] == '0':
            data.append([ "5", "Suck off", "", "", "", "", "", ""])
        elif row_data[-1] == '1':
            data.append([ "4", "Suck on", "", "", "", "", "", ""])

    #print(data)
    
    # Delete the last two columns and the first two rows
    data = [row[:-2] for row in data[2:]]

    return data
