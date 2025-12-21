import requests
import zipfile
import io

url = "https://donnees.roulez-eco.fr/opendata/instantane"

response = requests.get(url)

# Dézipper
zip_data = zipfile.ZipFile(io.BytesIO(response.content))
xml_filename = zip_data.namelist()[0]

with zip_data.open(xml_filename) as xml_file:
    xml_content = xml_file.read()

# Sauvegarde XML brut
with open("prix_carburants.xml", "wb") as f:
    f.write(xml_content)

print(" Données carburant récupérées (XML)")
