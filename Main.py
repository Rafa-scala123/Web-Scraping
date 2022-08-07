
from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np


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
#Numbers representing totals
rojo = 0
azul = 0
otro = 0

print()
print("Proven method")
for i in range(len(reps)):
    rep = reps[i]
    names.append(rep.find(class_="name").get_text())
    
    p_party.append(rep.find(class_="partido").get_text())
    partido = rep.find(class_="partido").get_text()
    if partido == "Partido Popular Democrático" :
        rojo  = rojo + 1
    elif partido == "Partido Nuevo Progresista":
        azul = azul + 1
    else:
        otro = otro + 1
        
        

    # position.append(rep.find(class_="position").get_text())
    


content = {
    "Nombre" : names,
    "Partido Político" : p_party,
    # "Posición" : position
    }
"""Extract total numbers and create a graphical representation of the number of people in congress
"""

df = pd.DataFrame(content)
print(df)
df.to_csv("Test_run.csv")

#Print out pi graph with parties
partidos = np.array([azul, rojo, otro])
plt.pie(partidos)
plt.show()


# print()
# print("Total por partidos")
# print("PNP: ", )
# print("Popular: ", )
# print("MVC: ", )
# print()
"""Add political leanings"""

    

