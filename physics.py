import numpy as np

def equations(t, state):
    """
    Taylor 4D: Here we tell solve_ivp how to calculate the next step.

    PARAMETERS YOU RECEIVE:
    
    t -> Current time in seconds. It is the 'x' of your expTaylor(x, x0, nmax)
    solve_ivp moves it: t=0, t=0.01, t=0.02...

    state -> List with 4 values = Taylor's TU x0. The starting point.
    state = [θ1, θ2, ω1, ω2]

    θ1 = Angle of pendulum 1 in radians. 0 = hanging down
    θ2 = Angle of pendulum 2 in radians. Relative to pendulum 1
    ω1 = Angular velocity of pendulum 1. How fast it rotates
    ω2 = Angular velocity of pendulum 2. How fast it rotates

    CONSTANTS WE USE:

    g -> Gravity = 9.81 m/s^2. Pull everything down
    L1 -> Length of pendulum 1 in meters
    L2 -> Length of pendulum 2 in meters

    WHAT SHOULD RETURN: [dθ1_dt, dθ2_dt, dω1_dt, dω2_dt]

    dθ1_dt -> Derivative of θ1. That is, the speed ω1. Therefore dθ1_dt = ω1
    dθ2_dt -> Derivative of θ2. That is, the speed ω2. Therefore dθ2_dt = ω2
    dω1_dt -> Derivative of ω1. That is, the angular acceleration 1. Here goes Newton
    dω2_dt -> Derivative of ω2. That is, the angular acceleration 2. Here goes Newton

    RULE: solve_ivp uses these 4 returns to make Taylor order 4-5
    and predict state at t + dt
    """

    θ1, θ2, w1, w2 = state
    g, L1, L2 = 9.81, 1.0, 1.0
    m1, m2 = 1.0, 1.0  # masas

    # Ecuaciones del péndulo doble
    num1 = -g * (2 * m1 + m2) * np.sin(θ1)
    num2 = -m2 * g * np.sin(θ1 - 2 * θ2)
    num3 = -2 * np.sin(θ1 - θ2) * m2 * (w2 * 2 * L2 + w1 * 2 * L1 * np.cos(θ1 - θ2))
    den = L1 * (2 * m1 + m2 - m2 * np.cos(2 * θ1 - 2 * θ2))
    dw1_dt = (num1 + num2 + num3) / den

    num1 = 2 * np.sin(θ1 - θ2)
    num2 = w1 ** 2 * L1 * (m1 + m2)
    num3 = g * (m1 + m2) * np.cos(θ1)
    num4 = w2 ** 2 * L2 * m2 * np.cos(θ1 - θ2)
    den = L2 * (2 * m1 + m2 - m2 * np.cos(2 * θ1 - 2 * θ2))
    dw2_dt = num1 * (num2 + num3 + num4) / den

    dθ1_dt = w1
    dθ2_dt = w2

    return [dθ1_dt, dθ2_dt, dw1_dt, dw2_dt]

