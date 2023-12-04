"""
Utilisation basique des classes de graphe
"""

import graphes

g = graphes.Graphe_en_liste()

g.ajouter_sommet("a")
g.ajouter_sommet("b")
g.ajouter_sommet("c")
g.ajouter_sommet("d")
g.ajouter_sommet("e")
g.ajouter_arete("a", "b")
g.ajouter_arete("a", "d")
g.ajouter_arete("a", "c")
g.ajouter_arete("b", "c")
g.ajouter_arete("b", "d")
g.ajouter_arete("c", "d")
g.ajouter_arete("c", "e")
g.ajouter_arete("d", "e")

g.dessiner()
