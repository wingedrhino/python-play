#!/usr/bin/python3
from bs4 import BeautifulSoup
from pathlib import Path

file_path = Path('original.xml')
  
new_provider_key = 'module:wingedrhino-plugin-keycloak-ejb'

# Read XML file and parse in Soup
with open(file_path, 'r') as fp:
  standalone_ha_text = fp.read()
standalone_ha_soup = BeautifulSoup(standalone_ha_text, 'xml')

# Find a subsystem element such that it's
# xmlns attribute is urn:jboss:domain:keycloak-server:1.1
# Then find the providers element inside that file.
providers_node = standalone_ha_soup.find(
  'subsystem',
  attrs={'xmlns':'urn:jboss:domain:keycloak-server:1.1'}
).find('providers')

for provider in providers_node.findAll('provider'):
  provider_key = provider.text.strip()
  print(f'Found provider {provider_key}')

new_provider_node = standalone_ha_soup.new_tag('provider')
new_provider_node.string = new_provider_key
providers_node.append(new_provider_node)
file_path = Path('modified.xml')
with open(file_path, 'w') as fp:
  fp.write(str(standalone_ha_soup))