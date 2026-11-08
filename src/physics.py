import numpy as np


# Physical parameters
M = 1.0      # cart mass (kg)
m = 0.1      # pole mass (kg)
L = 1.0      # pole length (m)
g = 9.81     # gravity (m/s^2)


def cartpole_dynamics(state, force):
    """
    Computes the time derivatives of the cart-pole state.

    Parameters
    ----------
    state : array-like
        [x, x_dot, theta, theta_dot]

    force : float
        External force applied to cart

    Returns
    -------
    numpy array
        [x_dot, x_ddot, theta_dot, theta_ddot]
    """

    x, x_dot, theta, theta_dot = state

    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    denominator = M + m * sin_theta**2

    x_ddot = (
        force
        + m * sin_theta * (L * theta_dot**2 + g * cos_theta)
    ) / denominator

    theta_ddot = (
        -force * cos_theta
        - m * L * theta_dot**2 * cos_theta * sin_theta
        - (M + m) * g * sin_theta
    ) / (L * denominator)

    return np.array([
        x_dot,
        x_ddot,
        theta_dot,
        theta_ddot
    ])