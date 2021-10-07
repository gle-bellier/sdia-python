import matplotlib.pyplot as plt
import numpy as np

from lab2.utils import get_random_number_generator


# todo clean up the docstrings
# todo test the whole class
class BoxWindow:
<<<<<<< HEAD
    """[This class create Boxes]"""
=======
    """[summary]"""
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6

    def __init__(self, args):
        """Create bow window

        Args:
<<<<<<< HEAD
            args (array of int): the array have dimmensions 2x1, 2x2 or 3x2, each sub array represent the coordinate of the two points on the x, y or z axis.
=======
            args (list of N float array): [a, b] bounds for each of the N dimensions of the window box.
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6
        """
        self.bounds = args

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
<<<<<<< HEAD
            string
=======
            str: string representation of the box window.
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6
        """
        # * Nice try!
        # ? how about a list comprehension using for a, b in self.bounds
        l_str = list(map(lambda x: f"[{x[0]}, {x[1]}]", self.bounds))
        return "BoxWindow: " + " x ".join(l_str)

    # todo test it
    def __len__(self):
        return len(self.bounds)

<<<<<<< HEAD
    # def __contains__(self, args):
    #     for i in range(len(args)):
    #         if not (self.bounds[i][0] <= args[i] <= self.bounds[i][1]):
    #             return False
    #     return True

    # def __contains__(self, point):
    #     assert len(point) = len(self)
    #     for (a,b), x in zip(self.bounds, point):
    #           if not (a<= x <= b):
    #             return False
    #     return True

    def __contains__(self, point):
        return all(a<= x <= b) for (a,b), x in zip(self.bounds, point)

    # def __contains__(self, point):
    #     a = self.bounds([:,0])
    #     b = self.bounds([:,1])
    #     return np.all(np.logical_and(a<=point, point <= b))
=======
    # ! this method is not used
    # todo convert it to a static method
    def in_segment(self, x, segment):
        """Tool function indicating if a point is in a given segment or not.

        Args:
            x (float array): point of interest
            segment (float array): segment considered

        Returns:
            bool: True if point is in the segment else False
        """
        return segment[0] <= x < segment[1]

    def __contains__(self, x):
        # ! be careful, x is used twice in different context
        # * consider argument x -> point, or in iteration x -> coor
        return all(a <= x <= b for (a, b), x in zip(self.bounds, x))
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6

    # todo test it
    def dimension(self):
<<<<<<< HEAD
        """[summary]"""
        dim = []
        for (a, b) in self.bounds:
            dim += [b - a]
        return dim
=======
        """Returns the number of dimension of the window box

        Returns:
            int: number of dimensions.
        """
        return len(self)
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6

    # todo test it
    def volume(self):
<<<<<<< HEAD
        """[summary]"""
        vol = 0
        for elm in self.dimension():
            vol *= elm
        return vol

    def indicator_function(self, args):
        """We check if a point is in a box

        Args:
            args (array of int of size 1x2): we give the coordinate of a point
=======
        """Returns the volume of the window box defined as the product of size of each dimension.

        Returns:
            float: volume of the window box.
        """
        # * exploit numpy vectors, use - or np.diff, and np.prod
        v = 1
        # * consider for a, b in self.bounds
        for dim in self.bounds:
            v *= np.abs(dim[0] - dim[1])
            # ? why using abs, isn't dim[1] > dim[0], is this tested
        return v

    def indicator_function(self, args):
        """Returns if args is in the window box.

        Args:
            args (float array): The window box [description]

        Returns:
            bool: True if point in window box, else False.
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6
        """
        # ? how would you handle multiple points
        return args in self

    def get_random_point_inside(self):  # todo add a rng argument
        """Returns a point at random in the window box

        Returns:
            float array: random point in the bow window
        """
        # ! USE rng
        # * exploit numpy, rng.uniform(a, b, size=n)
        # ! naming: dim -> bound or segment ?
        return np.array([np.random.uniform(*dim) for dim in self.bounds])

    # todo test it
    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.

        # ? Returns:
        """
        rng = get_random_number_generator(rng)
        # * Interesting try using get_random_point_inside
        # ! however the output points are all the same
        # * exploit numpy, rng.uniform(a, b, size=n)
        # ! USE rng
        return [self.get_random_point_inside()] * n

    def center(self):
        """Compute center of the box window.

        Returns:
            float array: center coordinates of the box window.
        """
        # * interesting use of a lambda function
        # * exploit numpy vectors, use - or np.diff, +, or np.mean
        mid = lambda x: (x[0] + x[1]) / 2
        c = list(map(mid, self.bounds))
        return np.array(c)


class UnitBoxWindow(BoxWindow):
    def __init__(self, dimension, center):
        """Unit box of a given dimension (hypercube box) at a given center point

        Args:
            dimension (float): [description]
            center (float array, optional): center of the window.
        """
<<<<<<< HEAD

        bounds = np.array([[c - dimension / 2, c + dimension / 2]
                           for c in center])

        super(self.__class__, self).__init__(bounds)
=======
        # * exploit numpy vectorization power
        # ? how about np.add.outer
        bounds = np.array([[c - dimension / 2, c + dimension / 2] for c in center])
        print(bounds)  # ! why is there a print

        super(UnitBoxWindow, self).__init__(bounds)


# ? Why this class written in box_window.py
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
        # ? how about np.linalg.norm
        return np.sqrt(np.sum(np.power(x - self.center, 2)))

    # ? interesting but unused
    # todo test it
    def dist_to_ball(self, x):
        """Compute the distance of a given point to the surface of the ball window.

        Args:
            x (float array): coordinates of the point of interest.

        Returns:
            float: distance of the given point to the surface of the ball window.
        """
        # ? a distance is supposed to be positive isn't it
        return self.dist_to_center(x) - self.radius

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
        return len(self.center)

    # todo test it
    def volume(self):
        """Computes the volume of the ball.

        Returns:
            float: volume of the ball window.
        """
        # ! valid only in 3D
        return 4 * np.pi * np.power(self.radius, 3) / 3


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
    c = 0
    rslt = []  # ! naming: rslt is not clear
    for i in range(n):
        c += unit_box.get_random_point_inside() in ball
        rslt += [4 * c / (i + 1)]
    return rslt


if __name__ == "__main__":
    # Estimating pi using the rejection sampling method
    plt.plot(estimate_pi(), label="estimated pi")
    plt.title("Estimation of pi over iterations")
    plt.legend()
    plt.show()
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6
