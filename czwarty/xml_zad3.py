import xml.etree.ElementTree as ET

file_path = 'Catalog.xml'

tree = ET.parse(file_path)
root = tree.getroot()

print(root)  # <Element 'Catalog' at 0x0000022F39410630>

for mobile in root.findall('mobile'):
    brand = mobile.find('brand').text
    price = mobile.find('price').text

    print(f"Brand: {brand}, Price: {price}")
# <Element 'Catalog' at 0x0000014E19C14680>
# Brand: Redmi, Price: 6999
# Brand: Samsung, Price: 8999
