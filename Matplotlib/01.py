# import matplotlib

import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)


# Draw a line in a diagram from position (0,0) to position (6,250)


# To plot array in numpy

# plt.plot(x, y) creates a line plot with x and y values.

# plt.show() renders the plot, displaying it in the output.

# xpoints = np.array([0,10])
# ypoints = np.array([0,250])
# plt.plot(xpoints,ypoints)
# plt.show()


# xpoints: An array containing the x-coordinates [0, 10]. This means the line starts at x = 0 and ends at x = 10.

# ypoints: An array containing the y-coordinates [0, 250]. This means the line starts at y = 0 and ends at y = 250.



# import matplotlib
# matplotlib.use('Agg')


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()