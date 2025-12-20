import requests
import xml.etree.ElementTree as ET
import pandas as pd
import io
import zipfile

url = "https://donnees.roulez-eco.fr/opendata/instantane"
r = requests.get(url)

z = zipfile.ZipFile(io.BytesIO(r.content))
xml_file = z.namelist()[0]

tree = ET.parse(z.open(xml_file))
root = tree.getroot()

rows = []

for pdv in root.findall("pdv"):
    for price in pdv.findall("prix"):
        rows.append({
            "carburant": price.get("nom"),
            "prix": float(price.get("valeur"))  # ✅ DÉJÀ EN EUROS
        })

df = pd.DataFrame(rows)

# Normalisation
df["carburant"] = df["carburant"].str.upper().str.strip()

# Filtrage essence
fuel_df = df[df["carburant"].str.contains("SP95|E10", na=False)]

print("Nb lignes carburant retenues :", len(fuel_df))
print("Prix moyen carburant (€ / L) :", round(fuel_df["prix"].mean(), 2))
