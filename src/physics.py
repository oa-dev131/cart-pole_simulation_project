import numpy as np

# Default physical parameters (SI units)
M = 1.0      # Cart mass [kg]
m = 0.1      # Pole point-mass [kg]
L = 1.0      # Pole length from pivot to mass [m]
g = 9.81     # Gravitational acceleration [m/s^2]


def cartpole_dynamics(state, force, params=(M, m, L, g)):
    """
    Compute rates of change [x_dot, x_ddot, theta_dot, theta_ddot]
    for a frictionless cart-pole system.

    State order:
      state = [x, x_dot, theta, theta_dot]
        - x: horizontal cart position [m], positive right
        - x_dot: horizontal cart velocity [m/s], positive right
        - theta: pole angle from straight down [rad], positive counter-clockwise
                 (theta = 0 is hanging down, theta = pi is straight up)
        - theta_dot: angular velocity [rad/s], positive counter-clockwise

    force: horizontal push force on the cart [N], positive right.
    """
    x, x_dot, theta, theta_dot = np.asarray(state, dtype=float)
    cart_mass, pole_mass, pole_length, gravity = params

    s = np.sin(theta)
    c = np.cos(theta)

    # Shared denominator from the coupling between cart and pole motion
    denom = cart_mass + pole_mass * (s ** 2)

    # Horizontal acceleration of the cart (x_ddot)
    x_ddot = (
        force
        + pole_mass * pole_length * (theta_dot ** 2) * s
        + pole_mass * gravity * s * c
    ) / denom

    # Angular acceleration of the pole (theta_ddot)
    theta_ddot = (
        -force * c
        - pole_mass * pole_length * (theta_dot ** 2) * s * c
        - (cart_mass + pole_mass) * gravity * s
    ) / (pole_length * denom)

    return np.array([x_dot, x_ddot, theta_dot, theta_ddot], dtype=float)


def total_energy(state, params=(M, m, L, g)):
    """
    Compute total mechanical energy E = kinetic + potential [Joules],
    taking potential energy = 0 when the pole hangs straight down (theta = 0).
    """
    x, x_dot, theta, theta_dot = np.asarray(state, dtype=float)
    cart_mass, pole_mass, pole_length, gravity = params

    # Velocity of the pole mass in x and y directions
    vx_pole = x_dot + pole_length * theta_dot * np.cos(theta)
    vy_pole = pole_length * theta_dot * np.sin(theta)

    kinetic_cart = 0.5 * cart_mass * (x_dot ** 2)
    kinetic_pole = 0.5 * pole_mass * ((vx_pole ** 2) + (vy_pole ** 2))
    potential_pole = pole_mass * gravity * pole_length * (1.0 - np.cos(theta))

    return float(kinetic_cart + kinetic_pole + potential_pole)