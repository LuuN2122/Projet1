# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm

# Calcul de l'inertie
I = (b*(h**3)) / 12

# Calcul de la déformation maximale
delta_max = (F*(L**3)) / (3*E*(10**3)*I)

# Arrondir la valeur de la déformation maximale à deux décimales
delta_max = str(round(delta_max, 2))

print ("La déformation maximale de la poutre est", delta_max, "mm")


