#!/usr/bin/python3
import xml.etree.ElementTree as ET
tree = ET.parse('original.xml')

# Things get ugly when searching for the node due to the presence of
# namespaces. This broke the XML file after saving!

providers_node = tree.find('.//{urn:jboss:domain:keycloak-server:1.1}subsystem/{urn:jboss:domain:keycloak-server:1.1}providers')

print('printing children')
for child in providers_node:
  print(child.text.strip())

providers_node.append(ET.fromstring('<provider xmlns="urn:jboss:domain:keycloak-server:1.1">wingedrhino</provider>'))

print('printing children')
for child in providers_node:
  print(child.tag, child.text.strip())

tree.write('modified.xml')