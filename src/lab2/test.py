import numpy as np

from lab2.box_window import UnitBoxWindow

# uB = BallWindow([0, .3, 4, 0], 10)
# x = np.array([5, 13, 5.3, 4])
# print(uB.dist_to_center(x))

# print(x in uB)
# print(len(uB))
# print(uB)

uB = UnitBoxWindow(5, np.array([[2.5, 50, 4]]))

print(uB.volume())
print(uB.indicator_function(np.array([[2, 3], [0, 0], [3, 2]])))
