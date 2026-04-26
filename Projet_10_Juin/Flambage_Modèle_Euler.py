import numpy as np
import matplotlib.pyplot as plt

# Paramètres
E = 210e9       # Module d'Young (Pa)
I = 1000e-8     # Moment quadratique (m⁴)
L = 5.0         # Longueur (m)
k = 1.0         # Coefficient selon conditions aux limites

# Charge critique d'Euler
Pcr = (np.pi**2 * E * I) / (k * L)**2

# Déformée modale (cas rotule-rotule)
x = np.linspace(0, L, 200)
y = np.sin(np.pi * x / (k * L))

plt.plot(y, x)
plt.xlabel("Déflexion latérale")
plt.ylabel("Hauteur x (m)")
plt.show()


