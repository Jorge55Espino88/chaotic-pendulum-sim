import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp
from physics import equations


def main():
    # Initial conditions [θ1, θ2, ω1, ω2]
    initial_state = [1.5, 0, 0, 0] # Pendulum

    # Time from 0 to 10 seconds, 1000 points
    t_span = (0, 10)
    t_eval = np.linspace(0, 10, 1000) # Mejor que tu for

    solution = solve_ivp(equations, t_span, initial_state, t_eval=t_eval)

    # ===== GRÁFICA ESTÁTICA: LA QUE YA TIENES =====
    plt.figure(figsize=(10,4))
    plt.plot(solution.t, solution.y[0], label="θ1 - Pendulum above")
    plt.plot(solution.t, solution.y[1], label="θ2 - Pendulum below")
    plt.xlabel("Time [s]")
    plt.ylabel("Angle [rad]")
    plt.title("Double Pendulum: Pure Chaos - Temporal Analysis")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('pendulum_analysis.png', dpi=150) # Guárdala
    plt.show()

    # ===== ANIMACIÓN NUEVA: EL WOW FACTOR =====
    L1, L2 = 1.0, 1.0 # Tus longitudes
    θ1, θ2 = solution.y[0], solution.y[1]
    t = solution.t

    # Vectorizado: calcula TODAS las posiciones de una
    x1 = L1 * np.sin(θ1)
    y1 = -L1 * np.cos(θ1)
    x2 = x1 + L2 * np.sin(θ2)
    y2 = y1 - L2 * np.cos(θ2)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.set_title('Double Pendulum: Dynamic Visualization')
    ax.grid(alpha=0.3)

    linea, = ax.plot([], [], 'o-', lw=3, color='#00BFFF') # Brazos
    traza, = ax.plot([], [], '-', color='red', alpha=0.5, lw=1) # Estela
    tiempo = ax.text(0.05, 0.95, '', transform=ax.transAxes)

    def animar(i):
        linea.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
        traza.set_data(x2[:i], y2[:i]) # Estela acumulada
        tiempo.set_text(f't = {t[i]:.2f} s')
        return linea, traza, tiempo

    ani = animation.FuncAnimation(fig, animar, frames=len(t),
                                  interval=20, blit=True)

    # ani.save('pendulo.gif', fps=50) # Descomenta para guardar
    plt.show()


if __name__ == '__main__':
    main()