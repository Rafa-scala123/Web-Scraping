
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
mvc = 0
pip = 0
proj = 0
ind = 0

print()
print("Proven method")
for i in range(len(reps)):
    rep = reps[i]
    names.append(rep.find(class_="name").get_text())
    # names.append(rep.find(class_="posición").get_text())
    p_party.append(rep.find(class_="partido").get_text())
    partido = rep.find(class_="partido").get_text()
    if partido == "Partido Popular Democrático" :
        rojo  = rojo + 1
    elif partido == "Partido Nuevo Progresista":
        azul = azul + 1
    elif partido == "Movimiento Victoria Ciudadana":
        mvc = mvc + 1
    elif partido == "Independiente":
        ind = ind + 1
    elif partido == "Partido Independentista Puertorriqueño":
        pip = pip + 1
    elif partido == "Proyecto Dignidad":
        proj = proj +1    


content = {
    "Nombre" : names,
    "Partido Político" : p_party,
    # "Posición" : position
    }
"""Extract total numbers and create a graphical representation of the number of people in congress
"""

df = pd.DataFrame(content)
df.to_csv("SenadoPR.csv")


#Print out pi graph with parties
partidos = np.array([azul, rojo, pip, mvc, ind, proj])
labels = ["PNP", "Popular", "PIP", "MVC", "Independiente", "Projecto Dignidad"]
colors = ["Blue", "Red", "Green", "Orange", "White", "#89CFF0"]
plt.pie(partidos, labels = labels, colors = colors)
plt.legend(title = "Senado de Puerto Rico")
plt.show()



