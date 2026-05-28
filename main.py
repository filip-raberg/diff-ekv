import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definiera systemets parametrar
m = 1000.0  # Massa (kg)
k = 30000.0 # Fjäderkonstant (N/m)
c = 4000.0  # Dämpningskonstant (Ns/m) Tryck på denna för att ändra dämpning!

# 2. Definiera differentialekvationen som ett system av första ordningen
def fjaderrorsle(t, y):
    x, v = y # y innehåller både position (x) och hastighet (v)
    dxdt = v
    dvdt = (-c*v - k*x) / m
    return [dxdt, dvdt]

# 3. Startvillkor (Bilen kör över ett gupp och flyttas 0.2 meter uppåt, hastighet 0)
y0 = [2.0, 0.0]

# Tidsintervall för simuleringen (0 till 5 sekunder)
t_span = (0, 5)
t_eval = np.linspace(0, 5, 500)

# 4. Lös ekvationen numeriskt
sol = solve_ivp(fjaderrorsle, t_span, y0, t_eval=t_eval)

# 5. Rita grafen
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label='Position (meter)', color='blue', linewidth=2)
plt.axhline(0, color='black', linestyle='--', alpha=0.5)
plt.title('Dämpad fjädersvängning (Bilstötdämpare)')
plt.xlabel('Tid (sekunder)')
plt.ylabel('Position från jämviktsläge (m)')
plt.grid(True)
plt.legend()
plt.show()