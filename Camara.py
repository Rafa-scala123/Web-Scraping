from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

"""Initial Scrape"""
page = requests.get("https://www.camara.pr.gov/page-team/")
soup = BeautifulSoup(page.content, "html.parser")

###Functions
"""Scrape: add = address, list = list of representatives"""
def scrape(add, list):
    pop1 = soup.find(class_=add)
    p1 = pop1.find_all(class_="name second_font")
    print("Populares: ")
    #First row done
    for p in p1:
        #Find name of each one
        list.append(p.get_text().strip())
        
    return list
        
        
###Scraping
"""Populares"""
populares = []

scrape("elementor-element elementor-element-eaf07b3 elementor-widget elementor-widget-ova_team", populares)
scrape("elementor-element elementor-element-a38c7a4 elementor-widget elementor-widget-ova_team", populares)

"""PNPs"""
pnps = []

scrape("elementor-element elementor-element-4d59620 elementor-widget elementor-widget-ova_team", pnps)


"""MVC"""
mvc = []
scrape("elementor-element elementor-element-d20ce33 elementor-widget elementor-widget-ova_team", mvc)

"""PIP"""
pip = []
scrape("elementor-element elementor-element-f453ae6 elementor-widget elementor-widget-ova_team", pip)

"""PD"""
pd = []
scrape("elementor-element elementor-element-a16710e elementor-widget elementor-widget-ova_team",pd)


"""Ind"""
ind = []
scrape("elementor-element elementor-element-f3eb98a elementor-widget elementor-widget-ova_team", ind)
"""Separate the representatives"""

"""Test trial"""
print("Popular: " , populares)
print("PNPS: ", pnps)
# """take this data and scrape it into a graph"""
# print("Representantes de Puerto Rico: ")
# for rep in reps:
#     print(rep.get_text().strip())

# """Take their positions"""