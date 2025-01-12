What is Matplotlib?

Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.


The source code for Matplotlib is located at this github repository 

https://github.com/matplotlib/matplotlib


Most of the Matplotlib utilities lies under the pyplot submodule,
and are usually imported under the plt alias


NumPy is a Python library.
NumPy is used for working with arrays.

matplotlib.pyplot: This is a collection of functions that allow you to create different types of plots. In this case, it is used to plot the line graph.

numpy: A library for numerical computing. Here, it is used to create the arrays xpoints and ypoints which represent the x and y coordinates of the points on the plot.



Matplotlib Plotting

Plotting x and y points

The plot() function is used to draw points (markers) in a diagram.

the plot() function draws a line from point to point.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.


Matplotlib Markers

You can use the keyword argument marker to emphasize each point with a specified


Format Strings fmt

You can also use the shortcut string notation parameter to specify the marker.


This parameter is also called fmt, and is written with this syntax:

marker|line|color


more details on w3schools python about marker refrence, color reference and line reference 

https://www.w3schools.com/python/matplotlib_markers.asp

Marker Size

You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:

Marker Color

You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers

