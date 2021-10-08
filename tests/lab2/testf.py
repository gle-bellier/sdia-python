from lab2.box_window import BoxWindow

import numpy as np

bounds = np.array([[2.5, 2.5]])

box = BoxWindow(bounds)

print(box.dimension())
