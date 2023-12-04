import graphviz
from typing import Union
from collections import deque


class Graphe_en_liste:
    """
    Classe implémentant un graphe non-orienté en tant que liste d'adjacence

    Le constructeur crée un graphe vide

    L'unique attibut est la liste d'adjacence codée sous forme d'un dictionnaire
    """

    def __init__(self, oriente=False):
        self.liste = {}
        self.oriente = oriente

    def renvoie_liste(self):
        """
        Renvoie la liste d'adjacence du graphe
        """
        return self.liste

    def renvoie_sommets(self):
        """
        Renvoie la liste des noms des sommets
        """
        return [cle for cle in self.liste]

    def ajouter_sommet(self, sommet) -> None:
        """
        Ajoute le sommet indiqué par son nom au graphe
        """
        assert sommet not in self.liste, "Un sommet portant le même nom existe déjà"

        self.liste[sommet] = []

    def ajouter_arete(self, s1, s2) -> None:
        """
        Ajoute une arête entre les sommets de noms s1 et s2
        """
        assert s1 in self.liste, "Aucun sommet ne porte ce nom"
        assert s2 in self.liste, "Aucun sommet ne porte ce nom"

        self.liste[s1].append(s2)
        if not self.oriente:
            self.liste[s2].append(s1)

    def adjacent(self, s1, s2) -> bool:
        """
        Renvoie True si s2 est voisin avec s1
        """
        assert s1 in self.liste, "Aucun sommet ne porte ce nom"
        assert s2 in self.liste, "Aucun sommet ne porte ce nom"

        return s2 in self.liste[s1]

    def voisins(self, s) -> list:
        """
        Retourne la liste des voisins de s
        """
        assert s in self.liste, "Aucun sommet ne porte ce nom"

        return self.liste[s]

    def retirer_sommet(self, s) -> None:
        """
        Retire le sommet s du graphe ainsi que les arêtes associées
        """
        assert s in self.liste, "Aucun sommet ne porte ce nom"

        del self.liste[s]

        for sommet in self.renvoie_sommets():
            if self.adjacent(sommet, s):
                self.liste[sommet].remove(s)

    def retirer_arete(self, s1, s2) -> None:
        """
        Retire l'arête s1-s2 du graphe
        """
        assert s1 in self.liste, "Aucun sommet ne porte ce nom"
        assert s2 in self.liste, "Aucun sommet ne porte ce nom"
        assert self.adjacent(s1, s2), "L'arête s1-s2 n'existe pas"

        self.liste[s1]: list.remove(s2)
        if not self.oriente:
            self.liste[s2].remove(s1)

    def dessiner(self, nom="export_graphe.png"):
        """
        Représente le graphe à l'aide de graphviz
        """
        g = graphviz.Graph(format="png", strict=True)
        aretes = []

        for s in self.liste:
            g.node(str(s))
            for v in self.liste[s]:
                if (str(s), str(v)) not in aretes:
                    g.edge(str(s), str(v))
                    aretes.append((str(v), str(s)))

        g.render(nom, view=True)

        return None

    def parcoure_profondeur(self, depart) -> list:
        pile = [depart]
        deja_vus = {s: False for s in self.retirer_sommet()}
        deja_vus[depart] = True
        resultat = []

        while len(pile) > 0:
            s = pile.pop()
            deja_vus[s] = True
            resultat.append(s)
            for v in self.voisins(s)[::-1]:
                if not deja_vus[v]:
                    deja_vus[v] = True
                    pile.append(v)
        return resultat

    def parcoure_largere(self, depart) -> list:
        file = deque([depart])
        deja_vus = {s: False for s in self.retirer_sommet()}
        deja_vus[depart] = True
        resultat = []

        while len(file) > 0:
            s = file.pop()
            deja_vus[s] = True
            resultat.append(s)
            for v in self.voisins(s):
                if not deja_vus[v]:
                    deja_vus[v] = True
                    file.appendleft(v)
        return resultat


class Graphe_en_matrice:
    """
    Classe implémentant un graphe non-orienté en tant que matrice d'adjacence

    Le constructeur crée un graphe vide

    L'objet a deux attributs :
        * la liste des noms des sommets qui permet de faire le lien entre nom et indice
            (l'indice d'un sommet dans la liste correspond à celui dans la matrice)
        * la matrice d'adjacence
    """

    def __init__(self, oriente=False):
        self.matrice = []
        self.noms = []
        self.oriente = oriente

    def renvoie_matrice(self):
        """
        Renvoie la matrice d'adjacence du graphe
        """
        return self.matrice

    def renvoie_sommets(self):
        """
        Renvoie la liste des noms des sommets
        """
        return self.noms

    def indice_de_sammet(self, s) -> int:
        """
        Renvoie la indice  == sommets
        """
        assert s in self.noms, "le sommet n' existe pas"
        return self.noms.index(s)

    def sammetp_de_indice(self, i) -> int:
        """
        Renvoie la sommets  == indice
        """
        assert 0 <= i < len(self.noms), "le sommet n' existe pas"
        return self.noms[i]

    def ajouter_sommet(self, s) -> None:
        """
        Ajoute le sommet indiqué par son nom au graphe
        """
        assert s not in self.noms, "Un sommet portant le même nom existe déjà"

        self.noms.append(s)
        for ligne in self.matrice:
            ligne.append(0)

        self.matrice.append([0 for _ in range(len(self.noms))])

    def ajouter_arete(self, s1, s2, poids: Union[int, float] = 1) -> None:
        """
        Ajoute une arête entre les sommets de noms s1 et s2
        La valeur de l'arête est par défaut 1
        Pour la modifier on utilisera set_valeur_arete
        """
        assert s1 in self.noms, "Aucun sommet ne porte ce nom"
        assert s2 in self.noms, "Aucun sommet ne porte ce nom"

        i1 = self.indice_de_sammet(s1)
        i2 = self.indice_de_sammet(s2)

        self.matrice[i1][i2] = poids

        if not self.oriente:
            self.matrice[i2][i1] = poids

    def adjacent(self, s1, s2) -> bool:
        """
        Renvoie True si s2 est voisin avec s1
        """
        assert s1 in self.noms, "Aucun sommet ne porte ce nom"
        assert s2 in self.noms, "Aucun sommet ne porte ce nom"

        i1 = self.indice_de_sammet(s1)
        i2 = self.indice_de_sammet(s2)
        return self.matrice[i1][i2] != 0

    def voisins(self, s) -> list:
        """
        Retourne la liste des voisins de s
        """
        assert s in self.noms, "Aucun sommet ne porte ce nom"

        iS = self.indice_de_sammet(s)
        voisins = []
        for i in range(len(self.noms)):
            if self.matrice[iS][i] != 0:
                voisins.append(self.sammetp_de_indice(i))

        return voisins

    def retirer_sommet(self, s) -> None:
        """
        Retire le sommet s du graphe ainsi que les arêtes associées
        """
        assert s in self.noms, "Aucun sommet ne porte ce nom"
        i_s = self.indice_de_sammet(s)
        self.noms.pop(i_s)
        self.matrice.pop(i_s)
        for ligne in self.matrice:
            ligne.pop(i_s)

    def retirer_arete(self, s1, s2) -> None:
        """
        Retire l'arête s1-s2 du graphe
        """
        assert s1 in self.noms, "Aucun sommet ne porte ce nom"
        assert s2 in self.noms, "Aucun sommet ne porte ce nom"

        i1 = self.indice_de_sammet(s1)
        i2 = self.indice_de_sammet(s2)
        self.matrice[i1][i2] = 0
        if not self.oriente:
            self.matrice[i2][i1] = 0

    def renvoie_valeur_arete(self, s1, s2):
        """
        Retourne la valeur associée à l'arête s1-s2
        (qui peut être différente de celle associée à s2-s1 si on a utilisé set_valeur_arete)
        """
        assert s1 in self.noms, "Aucun sommet ne porte ce nom"
        assert s2 in self.noms, "Aucun sommet ne porte ce nom"

        i1 = self.indice_de_sammet(s1)
        i2 = self.indice_de_sammet(s2)
        return self.matrice[i1][i2]

    def dessiner(self, nom="export_graphe.png"):
        """
        Représente le graphe à l'aide de graphviz
        Par défaut le graphe est non-orienté.
        Il est possible de changer cela avec la variable oriente

        oriente : Le graphe est-il orienté, False par défaut (bool)
        """

        g = None
        if not self.oriente:
            g = graphviz.Graph(format="png", strict=True)
        else:
            g = graphviz.Digraph(format="png", strict=True)

        aretes = []

        for s in self.noms:
            g.node(str(s))
            i = self.noms.index(s)
            for j, v in enumerate(self.matrice[i]):
                if v != 0:
                    if (i, j) not in aretes and not self.oriente:
                        g.edge(str(s), str(self.noms[j]), label=str(v))
                        aretes.append(sorted([j, i]))
                    else:
                        g.edge(str(s), str(self.noms[j]), label=str(v))
        g.render(nom, view=True)

        return None

    def parcoure_profondeur(self, depart) -> list:
        pile = [depart]
        deja_vus = {s: False for s in self.retirer_sommet()}
        deja_vus[depart] = True
        resultat = []

        while len(pile) > 0:
            s = pile.pop()
            deja_vus[s] = True
            resultat.append(s)
            for v in self.voisins(s)[::-1]:
                if not deja_vus[v]:
                    deja_vus[v] = True
                    pile.append(v)
        return resultat

    def parcoure_largere(self, depart) -> list:
        file = deque([depart])
        deja_vus = {s: False for s in self.retirer_sommet()}
        deja_vus[depart] = True
        resultat = []

        while len(file) > 0:
            s = file.pop()
            deja_vus[s] = True
            resultat.append(s)
            for v in self.voisins(s):
                if not deja_vus[v]:
                    deja_vus[v] = True
                    file.appendleft(v)
        return resultat
    def parcoure_c(self, depart) -> list:
        file = deque([depart])
        deja_vus = {s: False for s in self.retirer_sommet()}
        deja_vus[depart] = True
        parents = {s: None for s in self.retirer_sommet()}
        while len(file) > 0:
            s = file.pop()
            deja_vus[s] = True
            
            for v in self.voisins(s):
                if not deja_vus[v]:
                    deja_vus[v] = True
                    file.appendleft(v)
                    parents[v] = s
                
                elif deja_vus[v] and parents[v] != s :
                    return True
        return False

if __name__ == "__main__":
    # Essai du graphe en tant que matrice
    g = Graphe_en_matrice()
    g.ajouter_sommet("Essai")
    g.ajouter_sommet("Hello")
    g.ajouter_sommet("World")
    g.ajouter_sommet("Bonjour")
    g.ajouter_sommet("Le")
    g.ajouter_sommet("Monde")
    g.ajouter_arete("Hello", "World")
    g.ajouter_arete("Essai", "Hello")
    g.ajouter_arete("Essai", "Bonjour")
    g.ajouter_arete("Le", "Bonjour")
    g.ajouter_arete("Le", "Monde")
    g.ajouter_arete("Le", "World")
    print(g.renvoie_sommets())
    g.retirer_arete("Le", "World")
    g.retirer_arete("Essai", "Hello")
    g.retirer_arete("Essai", "Bonjour")
    g.retirer_sommet("Essai")
    print(g.renvoie_sommets())
    g.dessiner(oriente=True)

    # Essai du graphe en tant que liste
    g = Graphe_en_liste()
    g.ajouter_sommet("Essai")
    g.ajouter_sommet("Hello")
    g.ajouter_sommet("World")
    g.ajouter_sommet("Bonjour")
    g.ajouter_sommet("Le")
    g.ajouter_sommet("Monde")
    g.ajouter_arete("Hello", "World")
    g.ajouter_arete("Essai", "Hello")
    g.ajouter_arete("Essai", "Bonjour")
    g.ajouter_arete("Le", "Bonjour")
    g.ajouter_arete("Le", "Monde")
    g.ajouter_arete("Le", "World")
    print(g.renvoie_sommets())
    g.retirer_arete("Le", "World")
    g.retirer_arete("Essai", "Hello")
    g.retirer_arete("Essai", "Bonjour")
    g.retirer_sommet("Essai")
    print(g.renvoie_sommets())
    g.dessiner()
