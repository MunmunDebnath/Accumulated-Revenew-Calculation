from fileinput import filename
from urllib import request
import xml.etree.cElementTree as ET 

def xmlGeneration(root, element,banner,total_price, events, filename):
    ban = ET.SubElement(root, element,Banner_id=str(banner), revenues=str(total_price))
    event=ET.SubElement(ban, "Events")
    for key in events:
        ET.SubElement(event, "Event", id=key).text = str(events[key])
    tree = ET.ElementTree(root)
    tree.write(filename)    
