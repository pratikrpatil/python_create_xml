from lxml import etree
import random

root = etree.Element("Locations")

for _ in range(100**4):
    rec = etree.SubElement(root, "Record")
    
    loca_id = etree.SubElement(rec, "LocationID")
    loca_id.text = random.choice(['S-127176', 'S-118185', 'S-116179', 'S-128168', 'S-142167'])
    
    name = etree.SubElement(rec, "Name")
    name.text = random.choice(['HORTIFERVISA S.L.', 'MIKADO FOODS (UK) LTD', 'WILD BEER CO LIMITED', 'COPEFRUT S.A', 'OPTIBIOTIX LIMITED'])
    
    typ = etree.SubElement(rec, "Type")
    typ.text = "EXTERNAL_SUPPLIER"
    
    country = etree.SubElement(rec, "Country")
    country.text = random.choice(["ESP", "GBR", "CHL", "ITA", "TUR"])
    
    postalcode = etree.SubElement(rec, "PostalCode")
    postalcode.text = random.choice(["04740", "HP13 5RE", "BA4 6ER", "3340000", "Y010 5DG"])
    
    city = etree.SubElement(rec, "City")
    city.text = random.choice(['Almeria', 'High Wycombe', 'Shepton Mallet', 'curico', 'santiago'])
    
    actFrom = etree.SubElement(rec, "ActiveFrom")
    actFrom.text = "2021-05-27"
    
    actUpto = etree.SubElement(rec, "ActiveUpTo")
    actUpto.text = "4000-12-31" 


et = etree.ElementTree(root)
et.write('Location_Supplier.xml', pretty_print=True)