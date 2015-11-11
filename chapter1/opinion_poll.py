from __future__ import division


import numpy as np
pi = np.pi
import matplotlib.pyplot as plt


def probability_approx(n, p, N):
    """Approximate probability density for a random walk.

    Args:
        n (int): Number of successes.
        p (float): Probability of success for each trial.
        N (int): Number of trials.

    Returns (float) probability density for getting n steps.
    """
    q = 1 - p
    sigma_squared = N*p*q
    return (1.0/np.sqrt(2*pi*sigma_squared)) * np.exp(
        -((n - N*p)**2)/(2*sigma_squared))


def prob(N, p, x, y):
    """Probability that number of successes is in a given range.

    Args:
        N (int): Total number of trials.
        p (float): Probability of success on each trial.
        x (float): Minimum of target range, as a fraction of N.
        y (float): Maximum of target range, as a fraction of N.

    Returns (float) probability that number of successes is between N*x and N*y.
    """
    min_val = int(x*N)
    max_val = int(y*N)
    num_vals = max_val - min_val + 1
    vals = np.linspace(min_val, max_val, num_vals)

    q = 1 - p
    sigma_squared = N * p * q
    mean = N * p

    return np.sum(probability_approx(vals, p, N))
