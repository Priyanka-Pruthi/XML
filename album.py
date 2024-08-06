import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

with open('album.json','r') as input:
    albums = json.load(input)

#define namespaces

ns = {
    'xsi': "http://www.w3.org/2001/XMLSchema-instance",
    '': "http://example.com/catalogs"
}    

# root = ET.Element('catalogs')
root = ET.Element('catalogs')

# attrib= {
#               'xmlns:xsi':"http://www.w3.org/2001/XMLSchema-instance",
#               'xmlns':"http://www.example.com/catalogs",
#               'xsi:schemaLocation':"http://www.example.com/catalogs album.xsd"
#  }

root.set('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")
root.set('xmlns',"http://www.example.com/catalogs")
root.set('xsi:schemaLocation',"http://www.example.com/catalogs album.xsd")

for album in albums:
    album_element = ET.SubElement(root, 'album')
    album_element.set('id',str(album['id']))
 

    name_element = ET.SubElement(album_element, 'title')
    name_element.text = str(album['title'])
 
    singer_element = ET.SubElement(album_element, 'artist')
    singer_element.text = str(album['singer'])

    genre_element = ET.SubElement(album_element, 'genre')
    genre_element.text = str(album['genre'])
 
    publishing_date_element = ET.SubElement(album_element, 'releaseDate')
    publishing_date_element.text = str(album['releaseDate'])
 
    price_element = ET.SubElement(album_element, 'price')
    price_element.text = str(album['price'])
 
   
 
    review_element = ET.SubElement(album_element, 'review')
    if float(album['review']) >= 4.5:
        review_element.text = "Super Hit"
    elif 4.0 <= float(album['review']) < 4.5:
        review_element.text = "Hit"
    else:
        review_element.text = str(album['review'])

xml_str = ET.tostring(root, encoding='utf-8', method='xml').decode()

xml_well_formatted= minidom.parseString(xml_str).toprettyxml(indent="  ")

with open('albums.xml','w') as outputStream:
    outputStream.write(xml_well_formatted)