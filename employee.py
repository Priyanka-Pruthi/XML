import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
# read the Json file
with open('emp.json','r') as f:
    employees = json.load(f)

# create the root Element
root = ET.Element('employees')

#Iterate through JSON Objects to build the XML structure
for emp in employees:
    emp_element = ET.SubElement(root,'employee')

    # creating id element for each employee element
    id_element = ET.SubElement(emp_element,'id')
    id_element.text = str(emp['id']) # assigning/setting value for id element

    name_element = ET.SubElement(emp_element,'name')
    first_name_element = ET.SubElement(name_element,'first_name')
    first_name_element.text = str(emp['first_name']) # assigning/setting value for first_name element

    last_name_element = ET.SubElement(name_element,'last_name')
    last_name_element.text = str(emp['last_name']) # assigning/setting value for last_name element

    dept_element = ET.SubElement(emp_element,'department')
    dept_element.text = str(emp['department']) # assigning/setting value for dept_name element

    contact_element = ET.SubElement(emp_element,'contacts')
    email_element = ET.SubElement(contact_element,'email')
    email_element.text = str(emp['email']) # assigning/setting value for first_name element

#Convert the xml structure to Xml string
xml_string = ET.tostring(root, encoding='utf-8', method='xml').decode()

xml_pretty = minidom.parseString(xml_string).toprettyxml(indent= " ")

# write the xml string to file
with open('emp_with_new_structure.xml','w') as f:
    f.write(xml_pretty)

print("XML Docuemnt is created with name emp.xml")    
