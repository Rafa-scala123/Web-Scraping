
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests


"""Scrape website initially.
"""
page = requests.get("https://senado.pr.gov/index.cfm?module=senadores")
soup = BeautifulSoup(page.content, "html.parser")
print()
print("Senadores de Puerto Rico:")
print()
#Iterate through the list of items
reps = soup.find_all(class_="senator_cont")

#Set up arrays
names = []
p_party = []
position = []
print()
print("Proven method")
for i in range(len(reps)):
    rep = reps[i]
    names.append(rep.find(class_="name").get_text())
    p_party.append(rep.find(class_="partido").get_text())
    position.append(rep.find(class_="position").get_text())


content = {
    "Nombre" : names,
    "Partido Político" : p_party,
    "Posición" : position
    }

df = pd.DataFrame(content)
print(df)
df.to_csv("Test_run.csv")

# print()
# print("Total por partidos")
# print("PNP: ", )
# print("Popular: ", )
# print("MVC: ", )
# print()
"""Add political leanings"""

    

