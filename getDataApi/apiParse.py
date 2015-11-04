import urllib2
from xml.etree import ElementTree as ET
requestURL = 'http://api.eia.gov/series/?api_key=D7448759E3B234C54606C2E410368612&series_id=PET.EMM_EPM0_PTE_NUS_DPG.W&out=xml'
tree = ET.parse(urllib2.urlopen(requestURL))
root = tree.getroot()
print root.tag
print root.attrib
for child in root:
    print(child.tag, child.attrib)
series = tree.find("series")
row = series.find("row")
data = row.find("data")
row2 = data.findall("row")
for row in row2:
    date = row.find('date').text
    value = row.find('value').text
    print ('DURING THE WEEK OF:', date,  'GAS WAS: $', value)
