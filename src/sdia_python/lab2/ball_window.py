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
        return np.linalg.norm(x - self.center.squeeze())

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

    def volume(self):
        """Computes the volume of the ball.

        Returns:
            float: volume of the ball window.
        """
        # Using the gamma function to compute the volume of the ball
        return np.power(np.pi,
                        len(self) / 2) * np.power(
                            self.radius, len(self)) / gamma(len(self) / 2 + 1)

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BallWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.

        Returns:
            returns a float array with points in the bounds of the box
        """
        rng = get_random_number_generator(rng)

        # Using the Muller Method in d dimensions
        # first computing for a ball centered in O
        u = rng.normal(
            0, 1, (n, len(self))
        )  # an array of n x dimension normally distributed random variables

        norm = np.linalg.norm(u)
        r = self.radius * rng.random()**(1.0 / len(self))
        p = r * u / norm

        # we offset the points by the center of the ball
        return self.center + p


class UnitBallWindow(BallWindow):
    def __init__(self, center):
        """Create new unit ball window.

        Args:
            center (float array): coordinates of the center of the ball window.
        """
        super(UnitBallWindow, self).__init__(center, radius=1)
