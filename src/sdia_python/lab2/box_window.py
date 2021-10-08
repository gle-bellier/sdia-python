import matplotlib.pyplot as plt
import numpy as np

from sdia_python.lab2.utils import get_random_number_generator


class BoxWindow:
    def __init__(self, args):
        """Create bow window

        Args:
            args (list of N float array): [a, b] bounds for each of the N dimensions of the window box.
        """

        assert (args[:, 0] <= args[:, 1]).all()

        self.bounds = args

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str: string representation of the box window.
        """
        # * Nice try!
        l_str = list(map(lambda x: f"[{x[0]}, {x[1]}]", self.bounds))
        l_str = [f"[{a}, {b}]" for a, b in self.bounds]
        return "BoxWindow: " + " x ".join(l_str)

    def __len__(self):
        return len(self.bounds)

    def __contains__(self, x):
        assert len(x) == len(self)
        return all(self.bounds[:, 0] <= x) and all(x <= self.bounds[:, 1])
        # return all(a <= p <= b for (a, b), p in zip(self.bounds, x))

    def dimension(self):
        """Returns the number of dimension of the window box

        Returns:
            int: number of dimensions.
        """
        return len(self)

    def volume(self):
        """Returns the volume of the window box defined as the product of size of each dimension.

        Returns:
            float: volume of the window box.
        """
        return np.prod(np.diff(self.bounds, axis=1))

    def indicator_function(self, args):
        """Returns if args is in the window box.

        Args:
            args (float array): The window box [description]

        Returns:
            bool: True if point in window box, else False.
        """
        return args in self

    # todo test it
    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.

        Returns:
            returns a float array with points in the bounds of the box
        """
        rng = get_random_number_generator(rng)
        return np.array([[rng.uniform(*bound) for bound in self.bounds]
                         for i in range(n)])

    def center(self):
        """Compute center of the box window.

        Returns:
            float array: center coordinates of the box window.
        """

        return 0.5 * (self.bounds[:, 0] + self.bounds[:, 1])


class UnitBoxWindow(BoxWindow):
    def __init__(self, dimension, center):
        """Unit box of a given dimension (hypercube box) at a given center point

        Args:
            dimension (float): [description]
            center (float array, optional): center of the window.
        """
        # * exploit numpy vectorization power
        # ? how about np.add.outer
        bounds = np.array([[c - dimension / 2, c + dimension / 2]
                           for c in center])

        super(UnitBoxWindow, self).__init__(bounds)


# * Nice implementation!
# todo write more comments and document the code, for now it's not cristal clear
def estimate_pi(n=int(1e5)):  # todo add a rng argument as in self.rand
    """Estimating pi using the rejection sampling method

    Args:
        n (int, optional): number of iterations for pi estimation. Defaults to int(1e5).
    Returns:
        float list: list of all estimations of pi (last should be the more accurate)
    """
    center = np.array([0, 0])

    ball = BallWindow(center, 1)
    unit_box = UnitBoxWindow(2, center)

    # * exploit numpy vectorization power,
    # using unit_box.rand, ball.indicator_function and np.cumsum
    # c = 0
    # l_sum = []
    # for i in range(n):
    #     c += unit_box.get_random_point_inside() in ball
    #     l_sum += [4 * c / (i + 1)]
    # return l_sum

    print(unit_box.rand(n))
    s = ball.indicator_function(unit_box.rand(n))
    l_sum = np.cumsum(4 * s) / np.arange(1, n, 1)
    return l_sum


if __name__ == "__main__":
    # Estimating pi using the rejection sampling method
    plt.plot(estimate_pi(), label="estimated pi")
    plt.title("Estimation of pi over iterations")
    plt.legend()
    plt.show()
