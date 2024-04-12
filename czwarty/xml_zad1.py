from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

print(root)
product_child = root.createElement('product')
product_child.setAttribute('name', 'Geek')
xml.appendChild(product_child)

xml_str = root.toprettyxml(indent='\t')
print(xml_str)
# <xml.dom.minidom.Document object at 0x000002698F573410>
# <?xml version="1.0" ?>
# <root>
# 	<product name="Geek"/>
# </root>

with open('product.xml', 'w') as f:
    f.write(xml_str)
