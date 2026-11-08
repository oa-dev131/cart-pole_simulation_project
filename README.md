# Cart-Pole Numerical Simulation and Control Engine

Welcome to our final project repository for the **Introduction to Numerical Algorithms** course at BME! 

- **Team Members:** Omer Awan (FNQC14) & Adil Muhammad (BU9TKF)
- **Repository:** INM-Final-Project_T3_P10

---

## What is this project?
In this project, we are modeling and simulating a classic control problem: an **inverted pendulum on a cart (the cart-pole system)**. Imagine a pole balanced on top of a moving cart. Because it is underactuated and naturally unstable, keeping it upright requires clever physics and numerical algorithms. 

We built everything from scratch in Python (using NumPy, SciPy, and Matplotlib) to fully understand how numerical methods work under the hood, without relying on black-box libraries.

---

## What methods are we using?
To satisfy our course requirements, our project implements three main numerical techniques:
1. **Coupled Non-Linear ODE Integration (Runge-Kutta 4th Order / RK4):** Step-by-step numerical integration to solve the equations of motion for the cart's position and the pole's angle over time.
2. **Jacobian Matrix Linearization & Eigenvalues:** Analyzing the stability of the system near its unstable upright equilibrium point using linear algebra.
3. **Numerical Energy-Shaping Control:** Controlling the system's total mechanical energy to swing the pendulum up from hanging down and stabilize it at the top.

---

## Project Structure
Here is how our code is organized so you can easily navigate it:

```text
INM-Final-Project_T3_P10/
│
├── README.md               # You are reading this right now!
├── requirements.txt        # Python package dependencies
├── main.py                 # Main script to run simulations and generate plots
│
├── src/
│   ├── physics.py          # Lagrangian equations of motion and state-space setup
│   ├── solvers.py          # Custom numerical integration solvers (Euler & RK4)
│   ├── stability.py        # Jacobian matrix calculations and eigenvalue analysis
│   └── control.py          # Energy-shaping and feedback control logic
│
└── visualization/
    └── plots.py            # Code for generating time-series, phase portraits, and energy plots