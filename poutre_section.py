import math

# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

# poutre carrée
a = 15  # en mm

# poutre ronde
d = 5  # en mm

# poutre creuse
D = 15  # en mm
d = 5  # en mm

# Calcul de l'inertie de la section
I_rectangle = (b * (h ** 3)) / 12
I_carre = (a ** 4) / 12
I_rond = (math.pi * (d ** 4)) / 64
I_creux = (math.pi * ((D ** 4) - (d ** 4))) / 64

# Création d'une liste pour comparer les I
liste_inertie = [I_rectangle, I_carre, I_rond, I_creux]

# Chercher le max puisque plus le I est élevé, plus le delta est petit
I = max(liste_inertie)

# Calcul de la déformation maximale
delta_max = (F * (L ** 3)) / (3 * E * (10 ** 3) * I)

# Arrondir la valeur de la déformation maximale à deux décimales
delta_max = str(round(delta_max, 2))

# Choix de la section dépendamment du I choisi
if I == I_rectangle:
    section = "rectangulaire"

elif I == I_carre:
    section = "carrée"

elif I == I_rond:
    section = "ronde"

elif I == I_creux:
	section = "creuse"


print ("Le type de section minimisant la déformation maximale est", section, ", avec une déformation de", delta_max,
          "mm")
