# Double Pendulum — Chaotic System Simulation in Python

![Double Pendulum Chaotic Motion](assets/pendulo_pro.gif)

Numerical solution of the system of four coupled nonlinear ODEs describing the motion of a double pendulum. Developed to understand numerical integration, chaotic systems, and sensitivity to initial conditions.

## Result

### Dynamic Visualization
Chaotic trajectory where small differences in initial conditions generate completely divergent paths — hallmark of chaos.

### Temporal & Phase Analysis
![Temporal Analysis](pendulum_analysis.png)
*Trajectories in phase space and time evolution. Energy conservation validation and divergence analysis.*

## 🧠 Methodology — Parametric Experimentation
1. **Base model:** Lagrangian formulation of double pendulum
2. **Intentional modification:** Masses, lengths, and initial conditions varied
3. **Analysis:** Chaotic regimes and numerical stability limits identified

Each commit reflects an experimental change to understand underlying physics.

## Performance Optimization
- Frame reduction: 1000 → 250 frames (`range(0, len(t), 4)`)
- Lightweight render: pillow writer, 30fps, dpi 70, `blit=True`
- Result: LinkedIn-ready GIF <5MB

## 🛠 Technical Stack
- **Language:** Python 3.10+
- **Libraries:** NumPy, Matplotlib (FuncAnimation)
- **Integrator:** Custom RK4 in `physics.py` + adaptive tolerance for non-stiff chaotic systems
- **Structure:** `main.py` (orchestration), `physics.py` (ODEs), `assets/` (media)

## 🚀 How to Run It
```bash
# Clone
git clone https://github.com/Jorge55Espino88/DoublePendulum.git
cd DoublePendulum

# Install
pip install -r requirements.txt

```
**Author:** Jorge Espino — Mechatronics Engineer (B.Eng., Licensed) | Flight Mechanics & Simulation | Python, Numerical Methods

# Run
python main.py
# Output: pendulo_pro.gif + pendulum_analysis.png
