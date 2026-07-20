# Simulation of a Chaotic Double Pendulum in Python

Numerical solution of 4 coupled nonlinear ODEs describing the motion of a double pendulum. A personal project to understand numerical integration, chaotic systems, and sensitivity to initial conditions.

![Double Pendulum Results](results_overview.png)

## 📊 Results

**1. Temporal Analysis (Top):** Evolution of θ1 and θ2 over 10s. The orange trajectory (θ2) shows strong divergence — small initial differences lead to completely different paths after t≈2s. Hallmark of deterministic chaos and energy transfer between pendulums.

**2. Phase Space (Bottom):** Phase portrait θ2 vs Ω2. The dense, non-repeating, bounded orbit is a chaotic attractor. No closed periodic orbit, confirming non-integrability of the system.

> The graph shows trajectories in phase space and time evolution. The chaotic nature of the system is evident: small differences in initial conditions generate divergent trajectories.

## 🧠 Physics & Math

- **Formulation:** Lagrangian mechanics → 4 first-order ODEs: (θ1, ω1, θ2, ω2)
- **Integrator:** SciPy `solve_ivp` with RK45 adaptive, rtol=1e-9, atol=1e-9
- **Simulation:** 20s total, evaluation step 0.02s
- **Concepts:** Deterministic chaos, sensitivity, phase space analysis

## 🔬 Learning Methodology — Parametric Experimentation Method

This project was developed using my "Parametric Experimentation Method":
1. **Transcription of base model:** The differential equations of the double pendulum were used as a starting point.
2. **Interaction of physical variables:** Masses, lengths, and initial conditions were varied to observe the system's response.
3. **Results Analysis:** Chaotic behaviors and numerical stability limits were identified. Each commit reflects an experimental change to understand the underlying physics.

## 🛠 Technical Stack
- Language: Python 3.10+
- Libraries: NumPy, SciPy (solve_ivp), Matplotlib
- Integrator: RK45 with adaptive tolerance

## 🚀 How to Run It
git clone https://github.com/Jorge55Espino88/DoublePendulum
cd DoublePendulum
pip install numpy scipy matplotlib
python double_pendulum.py

The script generates the pendulum_analysis.png graph and displays the animation.

## 💡 Key Learnings
- High sensitivity to initial conditions is the hallmark of chaotic systems.
- SciPy's RK45 method is robust for non-rigid ODEs, but requires adjustment of rtol and atol in sensitive systems.
- Visualizing phase space is crucial for interpreting nonlinear dynamics.

## 🔜 Next Step
Extend the model to include friction at the pivots and force the system to study parametric resonance.

## Author
Jorge Espino Garza — Mechatronics Engineer | Scientific Simulation with Python Transitioning to R&D in Nonlinear Dynamics and Aerospace
www.linkedin.com/in/jorge-espino-garza

Project developed as part of self-taught specialization in applied numerical methods.
---
