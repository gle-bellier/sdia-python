import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

from sdia_python.lab2.utils import get_random_number_generator


class BallWindow:
    def __init__(self, center, radius):
        """Create new ball window.

        Args:
            center (float array): coordinates of the center of the ball window.
            radius (float): radius of the ball window.
        """
        self.center = center
        self.radius = radius

    def dist_to_center(self, x):
        """Compute the distance of a given point to the center of the ball window.

        Args:
            x (float array): coordinates of the point of interest.

        Returns:
            float: distance of the given point to the center of the ball window.
        """
        # * Nice vectorization using numpy
        return np.linalg.norm(x - self.center)

    def __contains__(self, x):
        """Compute whether a given point is contained in the ball window or not.

        Args:
            x (float array): coordinates of the point of interest.

        Returns:
            bool: point is in ball window or not.
        """

        # we need to compute the distance of the point of interest to the center of the ball window
        return self.dist_to_center(x) < self.radius

    def __str__(self):
        """BallWindow: (center, radius)

        Returns:
            str: string representation of the ball window.
        """
        # * nice use of f-strings
        return f"BallWindow (center : {self.center}, radius : {self.radius})"

    def __len__(self):
        """Indicates the number of dimension of the ball window.

        Returns:
            int: number of dimension of the ball window.
        """
        return len(self.center[0])

    def indicator_function(self, args):
        """Returns if args is in the ball window.

    Args:
        args (float array): The ball window  [description]

    Returns:
        bool: True if point in ball window else False.
    """
        return np.array([point in self for point in args])

    # todo test it
    def volume(self):
        """Computes the volume of the ball.

        Returns:
            float: volume of the ball window.
        """
        # Using the gamma function to compute the volume of the ball
        return np.power(np.pi,
                        len(self) / 2) * np.power(
                            self.radius, len(self)) / gamma(len(self) / 2 + 1)
