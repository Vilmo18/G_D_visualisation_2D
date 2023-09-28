import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Créez une figure et un /
fig, ax = plt.subplots()

# Créez une ligne représentant la courbe
x = np.linspace(-4, 4, 100)
y = x**2
line, = ax.plot(x, y)

# Créez le point que vous souhaitez animer
point, = ax.plot([], [], 'ro')


# Algorithme de la descente de gradient
def gradient(x0, l_rate=0.1, iter=100):
    def f(z): return 2*z
    x1 = x0
    abs = []
    ord = []
    for i in range(iter):
        x1 = x1-l_rate*f(x1)
        y1 = x1**2
        abs.append(x1)
        ord.append(y1)
        print("x", x1, "---- y  ", y1)
    return abs, ord


# Liste de nouvelles positions du point
abs, ord = gradient(-3, 0.1, 50)
new_positions = [(x_val, y_val) for x_val, y_val in zip(abs, ord)]

# Ajouter un nuage de point
scatter = ax.plot(abs, ord,marker='x',color="yellow")

# Fonction d'initialisation de l'animation


def init():
    point.set_data([], [])
    return point,

# Fonction d'animation pour mettre à jour la position du point


def animate(frame):
    x_val, y_val = new_positions[frame]
    point.set_data(x_val, y_val)
    return point,


# Afficher la grille
ax.grid(True)

# Créez l'animation
ani = FuncAnimation(fig, animate, frames=len(
    new_positions), init_func=init, blit=True)
# Affichez l'animation
plt.show()
