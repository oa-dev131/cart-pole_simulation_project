Cart-Pole Numerical Simulation and Control Engine
Final project for the Introduction to Numerical Algorithms course at BME.

Team Members: Omer Awan (FNQC14) & Adil Muhammad (BU9TKF)

Project Overview
This project models and simulates an inverted pendulum on a cart (cart-pole system), a classic problem in dynamics and control engineering.

The system is naturally unstable, meaning the pendulum will fall unless the cart moves appropriately to keep it balanced. Our goal is to model the system, solve its equations of motion numerically, analyze its stability, and investigate control strategies.

Methods Used
The project focuses on three main numerical topics:

Euler Method
A simple numerical integration method used as a baseline for comparison.

Runge-Kutta 4th Order (RK4)
A more accurate numerical method used to solve the nonlinear equations of motion.

Jacobian Linearization & Eigenvalue Analysis
Used to study the stability of the system near its upright equilibrium.

Additional Extension: Energy-Shaping Control for swinging the pendulum upright and stabilizing it.

Project Goals
Derive the cart-pole equations of motion.
Simulate the system using Euler and RK4 methods.
Compare the accuracy and stability of both methods.
Analyze system stability using linearization and eigenvalues.
Implement an energy-based control strategy.
Visualize and interpret the results using plots.
Project Structure
INM-Final-Project_T3_P10/
│
├── README.md
├── requirements.txt
├── main.py
│
├── src/
│   ├── physics.py
│   ├── solvers.py
│   ├── stability.py
│   └── control.py
│
└── visualization/
    └── plots.py