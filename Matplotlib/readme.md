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

You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:

Use both the mec and mfc arguments to color the entire marker:

You can also use Hexadecimal color values


Matplotlib Line

You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line

Shorter Syntax
The line style can be written in a shorter syntax:

linestyle can be written as ls.
dotted can be written as :.
dashed can be written as --.

explore more line styles on w3schools python

Line Color

You can use the keyword argument color or the shorter c to set the color of the line:

You can also use Hexadecimal color values
Or any of the 140 supported color names.


Line Width

You can use the keyword argument linewidth or the shorter lw to change the width of the line.

The value is a floating number, in points:

Multiple Lines

You can plot as many lines as you like by simply adding more plt.plot() functions:

Draw two lines by specifying a plt.plot() function for each line:


You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)

The x- and y- values come in pairs:

Two NumPy arrays (x1, y1) define the coordinates of the first set of points to plot.

x1 = [0, 1, 2, 3]
y1 = [3, 8, 1, 10]

Two more NumPy arrays (x2, y2) define the coordinates of the second set of points.

x2 = [0, 1, 2, 3]
y2 = [6, 2, 7, 11]


Matplotlib Labels and Title

Create Labels for a Plot

With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.


Create a Title for a Plot

With Pyplot, you can use the title() function to set a title for the plot.

Set Font Properties for Title and Labels

You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.


Position the Title

You can use the loc parameter in title() to position the title.

Legal values are: 'left', 'right', and 'center'. Default value is 'center'.



Matplotlib Adding Grid Lines

Add Grid Lines to a Plot

With Pyplot, you can use the grid() function to add grid lines to the plot.



Specify Which Grid Lines to Display

You can use the axis parameter in the grid() function to specify which grid lines to display.

Legal values are: 'x', 'y', and 'both'. Default value is 'both'.


Set Line Properties for the Grid

You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).


Matplotlib Subplot

Display Multiple Plots

With the subplot() function you can draw multiple plots in one figure


The subplot() Function

The subplot() function takes three arguments that describes the layout of the figure.

The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.


So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:


You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.


Title

You can add a title to each plot with the title() function:


Super Title

You can add a title to the entire figure with the suptitle() function:


Matplotlib Scatter

Creating Scatter Plots

With Pyplot, you can use the scatter() function to draw a scatter plot.

The scatter() function plots one dot for each observation.

It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:




The observation in the example above is the result of 13 cars passing by.

The X-axis shows how old the car is.

The Y-axis shows the speed of the car when it passes.

Are there any relationships between the observations?

It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.


Compare Plots


In the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?

The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter.

By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives.


Colors

You can set your own color for each scatter plot with the color or the c argument


You can even set a specific color for each dot by using an array of colors as value for the c argument:


Note: You cannot use the color argument for this, only the c argument.


ColorMap

The Matplotlib module has a number of available colormaps.

A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

This colormap is called 'viridis' 
and as you can see it ranges from 0, which is a purple color, up to 100, which is a yellow color.


In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot:


You can include the colormap in the drawing by including the plt.colorbar() statement

Available colormaps are on w3schools python


Size

You can change the size of the dots with the s argument.

Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:



Alpha

You can adjust the transparency of the dots with the alpha argument.


Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:



Combine Color Size and Alpha

You can combine a colormap with different sizes of the dots. This is best visualized if the dots are transparent


np.random.randint() is a function from the numpy library that generates random integers.

100: This specifies the upper bound (exclusive), meaning the integers will be between 0 and 99 (not including 100).


size=(100): This specifies the shape of the output. In this case, it will generate 100 random integers, creating a one-dimensional array with 100 elements.


The np.random.randint(100, size=(100)) generates a total of 100 random numbers in the range [0, 99].



Matplotlib Bars


Creating Bars

With Pyplot, you can use the bar() function to draw bar graphs:


The bar() function takes arguments that describes the layout of the bars.

The categories and their values represented by the first and second argument as arrays.



Horizontal Bars

If you want the bars to be displayed horizontally instead of vertically, use the barh() function:


Bar Color

The bar() and barh() take the keyword argument color to set the color of the bars


Color Names

You can use any of the 140 supported color names.

Color Hex

Or you can use Hexadecimal color values


Bar Width

The bar() takes the keyword argument width to set the width of the bars

The default width value is 0.8

Note: For horizontal bars, use height instead of width.

Bar Height

The barh() takes the keyword argument height to set the height of the bars:

The default height value is 0.8



Matplotlib Histograms

Histogram

A histogram is a graph showing frequency distributions.

It is a graph showing the number of observations within each given interval.


histogram graph in png: 01.png

2 people from 140 to 145cm
5 people from 145 to 150cm
15 people from 151 to 156cm
31 people from 157 to 162cm
46 people from 163 to 168cm
53 people from 168 to 173cm
45 people from 173 to 178cm
28 people from 179 to 184cm
21 people from 185 to 190cm
4 people from 190 to 195cm


Create Histogram


In Matplotlib, we use the hist() function to create histograms.


The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10.



To generate an array of 250 random values concentrated around a mean (in this case, 170) with a given standard deviation (10), you would use numpy's np.random.normal() function. 


np.random.normal(170, 10, 250)

np.random.normal() generates random numbers from a normal (Gaussian) distribution.


170: This is the mean (also called the "center" or "average") of the distribution. It means most of the values generated will be around 170.


10: This is the standard deviation of the distribution. The standard deviation determines how spread out the numbers will be around the mean. 

A smaller standard deviation would generate values closer to 170, while a larger standard deviation would generate values that are more spread out.


250: This specifies the number of values to generate, in this case, 250 random values.


The hist() function will read the array and produce a histogram:

Matplotlib Pie Charts

Creating Pie Charts

With Pyplot, you can use the pie() function to draw pie charts:



