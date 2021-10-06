from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[This class create Boxes]"""

    def __init__(self, args):
        """[summary]

        Args:
            args (array of int): the array have dimmensions 2x1, 2x2 or 3x2, each sub array represent the coordinate of the two points on the x, y or z axis.
        """
        self.bounds = args

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            string
        """
        l_str = list(map(lambda x: f"[{x[0]}, {x[1]}]", self.bounds))
        return "BoxWindow: " + " x ".join(l_str)

    def __len__(self):
        return len(self.bounds)

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

    def dimension(self):
        """[summary]"""
        dim = []
        for (a, b) in self.bounds:
            dim += [b - a]
        return dim

    def volume(self):
        """[summary]"""
        vol = 0
        for elm in self.dimension():
            vol *= elm
        return vol

    def indicator_function(self, args):
        """We check if a point is in a box

        Args:
            args (array of int of size 1x2): we give the coordinate of a point
        """
        return args in self

    def get_random_point_inside(self):
        return np.array([np.random.uniform(*dim) for dim in self.bounds])

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return [self.get_random_point_inside()] * n


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """

        bounds = np.array([[c - dimension / 2, c + dimension / 2]
                           for c in center])

        super(self.__class__, self).__init__(bounds)
