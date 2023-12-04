from graphes import *

clas = Graphe_en_liste
for i in ["l","v","m","i","r","n"]:
    clas.ajouter_sommet(i)
clas.ajouter_arete("l","v")
clas.ajouter_arete("m","I")
clas.ajouter_arete("I","R")

clas.dessiner()

gaf = Graphe_en_matrice(True)

for i in ["a","b","c","d"]:
    gaf.ajouter_sommet(i)

gaf.ajouter_arete( "a","c",12)
gaf.ajouter_arete( "a","D",12)
gaf.ajouter_arete( "a","c",12)
gaf.ajouter_arete( "a","c",12)
gaf.ajouter_arete( "a","c",12)
