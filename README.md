# Cart-Pole Numerical Simulation and Stability Analysis

Final project for **Introduction to Numerical Algorithms** at BME.

**Team Members:**
* Omer Awan (FNQC14)
* Adil Muhammad (BU9TKF)

---

## Project Overview
This project models and simulates an inverted pendulum on a cart (cart-pole system). Because the upright position is naturally unstable, the pendulum falls unless the cart moves to balance it.

Our goal is to derive the equations of motion, solve them numerically, test how step size affects accuracy and stability, analyze local stability around equilibrium points, and examine basic stabilization.

---

## Methods Used
1. **Euler Method:** A simple first-order numerical solver used as a baseline to see how step size affects accuracy and energy drift.
2. **Runge-Kutta 4th Order (RK4):** A higher-order numerical solver used for accurate simulation of the nonlinear equations of motion.
3. **Jacobian Linearization & Eigenvalue Analysis:** Linearizes the system around equilibrium points (hanging down and standing up) and uses eigenvalues to check local stability.
4. **Linear Stabilization Control:** A basic feedback controller around the upright position to keep the pole balanced for small deviations.

---

## What We Will Test and Compare
* **Step size and accuracy:** Running Euler and RK4 with different time steps (for example, dt = 0.1, 0.01, and 0.001 s) and comparing how fast the error shrinks.
* **Energy behavior:** Checking whether total mechanical energy stays constant when there is no friction and no push force on the cart, or drifts due to numerical error.
* **Linear vs. nonlinear behavior:** Comparing the linearized model against the full nonlinear simulation for small vs. larger tilt angles.

---

## Project Structure
INM-Final-Project_T3_P10/
├── README.md
├── requirements.txt
├── main.py
├── src/
│   ├── physics.py
│   ├── solvers.py
│   ├── stability.py
│   └── control.py
└── visualization/
    └── plots.py

---

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the main script:
   python main.py

---

## Task Breakdown
* **Omer Awan (FNQC14):** Equations of motion (`src/physics.py`), linearization and eigenvalues (`src/stability.py`), and stabilization logic (`src/control.py`).
* **Adil Muhammad (BU9TKF):** Euler and RK4 solvers (`src/solvers.py`), step-size and energy tests, and plots (`visualization/plots.py`).
* **Together:** Connecting everything in `main.py`, checking results, and preparing the presentation.