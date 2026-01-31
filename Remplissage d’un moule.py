import matplotlib.pyplot as plt

Q = 1e-6      # m³/s
S = 1e-4      # m²
L = 0.1       # m
dt = 0.01     # s

x = 0
t = 0

temps = []
positions = []

while x < L:
    x = x + (Q / S) * dt
    t = t + dt
    temps.append(t)
    positions.append(x)

print("Temps de remplissage :", t, "s")

plt.plot(temps, positions)
plt.xlabel("Temps (s)")
plt.ylabel("Position du front (m)")
plt.show()
