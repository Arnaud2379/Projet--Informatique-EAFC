
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simulation_interactive_flambage():
    print("--- Configuration de la Colonne Métallique ---")
    
    try:
        # --- Entrées Utilisateur ---
        L = float(input("Longueur de la colonne L (m) [ex: 5.0] : "))
        E = float(input("Module de Young E (Pa) [ex: 210e9 pour l'acier] : "))
        diametre = float(input("Diamètre de la section (m) [ex: 0.1] : "))
        P_appliquée = float(input("Charge axiale appliquée P (N) [ex: 50000] : "))
        
        # --- Calculs de Section ---
        I = (np.pi * diametre**4) / 64  # Moment d'inertie pour une section circulaire
        
        # --- Théorie d'Euler ---
        # On considère ici le cas rotule-rotule (K=1) selon le cahier des charges
        P_crit = (np.pi**2 * E * I) / (L**2)
        
        print(f"\n--- Résultats de l'Analyse ---")
        print(f"Charge critique théorique (P_cr) : {P_crit:.2f} N")
        
        # --- Calcul du Déplacement Latéral (Approximation non-linéaire) ---
        # Si P < P_cr, le déplacement est théoriquement nul (équilibre stable)
        # Pour la visualisation, on illustre la tendance du flambage
        ratio = P_appliquée / P_crit
        if ratio >= 1:
            print("ATTENTION : La charge dépasse la charge critique ! Flambage imminent.")
            amplitude = 0.1 * L * ratio # Illustration de la déformation importante
        else:
            print(f"La structure est stable (Ratio P/P_cr : {ratio:.2%}).")
            # Petit déplacement résiduel illustratif pour la visualisation
            amplitude = 0.01 * L * ratio 

        # --- Génération de la Géométrie 3D ---
        n_points = 50
        z = np.linspace(0, L, n_points)
        # Mode 1 : sin(pi * z / L)
        x_def = amplitude * np.sin(np.pi * z / L)
        y_def = np.zeros_like(z)

        # --- Visualisation 3D ---
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')

        # Colonne déformée (Rouge) et Axe initial (Gris)
        ax.plot(x_def, y_def, z, color='red', linewidth=4, label='Déformée (Mode 1)')
        ax.plot([0,0], [0,0], [0,L], color='grey', linestyle='--', label='Axe non-chargé')

        # Création d'une enveloppe cylindrique pour le rendu
        theta = np.linspace(0, 2*np.pi, 15)
        for i in range(0, n_points, 10):
            cx = x_def[i] + (diametre/2) * np.cos(theta)
            cy = y_def[i] + (diametre/2) * np.sin(theta)
            cz = np.full_like(theta, z[i])
            ax.plot(cx, cy, cz, color='blue', alpha=0.2)

        # Paramètres d'affichage
        ax.set_title(f"Simulation de Flambage\nCharge: {P_appliquée}N / Critique: {P_crit:.0f}N")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")
        ax.set_zlabel("Hauteur Z (m)")
        
        # Forcer des axes proportionnels
        limit = max(amplitude * 2, diametre * 2)
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(0, L)
        
        ax.legend()
        plt.show()

    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")

if __name__ == "__main__":
    simulation_interactive_flambage()
    
    
    
    
    

# Test 1 : Colonne stable

# Entre :

# Longueur L = 3
# Module de Young E = 210e9
# Diamètre = 0.08
# Charge appliquée = 50000


# Test 2 : Proche du flambage

# Entre :

# Longueur L = 5
# Module de Young E = 210e9
# Diamètre = 0.05
# Charge appliquée = 90000


# Test 3 : Dépassement de la charge critique

# Entre :

# Longueur L = 5
# Module de Young E = 210e9
# Diamètre = 0.05
# Charge appliquée = 120000