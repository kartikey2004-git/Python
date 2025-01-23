Pandas Introduction

Pandas is a Python library.

Pandas is used to analyze data.


CSV stands for "comma-separated values..

File format

A CSV file is a text file that stores data in a table-structured format.

A dataframe is a data structure constructed with rows and columns, similar to a database or Excel spreadsheet

Load a CSV file into a Pandas DataFrame



What is Pandas?

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.


The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.


Why Use Pandas?

Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant

Relevant data is very important in data science.

Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

What Can Pandas Do?

Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?

Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.


Installation of Pandas

If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Import Pandas

Once Pandas is installed, import it in your applications by adding the import keyword:

```bash
import pandas
```

Pandas as pd

Pandas is usually imported under the pd alias.

alias: In Python alias are an alternate name for referring to the same thing.

Create an alias with the as keyword while importing:

Now the Pandas package can be referred to as pd instead of pandas.


Checking Pandas Version

The version string is stored under __version__ attribute.

Pandas Series

What is a Series?

A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.


Labels

If nothing else is specified, the values are labeled with their index number.

First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.


n pandas, 
dtype: int64 means that the data type of the elements in the Series or DataFrame column 
is a 64-bit integer. 

This is the default integer type in pandas, allowing it to store large integer values efficiently. 


The int64 type supports integer values ranging from  
(-2 to the power 63) to [(2 to the power 63)-1]


Create Labels

With the index argument, you can name your own labels.

When you have created labels, you can access an item by referring to the label.


Key/Value Objects as Series

You can also use a key/value object, like a dictionary, when creating a Series.

Note: The keys of the dictionary become the labels.


To select only some of the items in the dictionary, 
use the index argument and specify only the items you want to include in the Series.


DataFrames

Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.


Pandas DataFrames

What is a DataFrame?

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.


Locate Row

As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)

Note: This example returns a Pandas Series.


Note: When using [], the result is a Pandas DataFrame.


Named Indexes

With the index argument, you can name your own indexes.

Locate Named Indexes

Use the named index in the loc attribute to return the specified row(s).


Load Files Into a DataFrame

If your data sets are stored in a file,
Pandas can load them into a DataFrame.


Pandas Read CSV


 The with statement is typically used for resource management, like opening files, where it ensures that resources are properly cleaned up after use.

 The open() function opens a file named data.csv in write mode ("w"), which means it will either create the file if it doesn't exist or overwrite it if it already exists.

 The newline="" argument is used to prevent extra blank lines between rows when writing to the CSV file, especially on Windows systems.


 This creates a writer object using the csv.writer() method. The writer object is responsible for writing rows of data to the file

 The writerows() method writes multiple rows to the file. It takes a list of lists (or similar iterable) called data, where each inner list represents a row of data to be written to the CSV file.


 
 The pd.read_csv() function automatically parses the CSV file and converts it into a tabular form (DataFrame).

The df.to_string() method converts the entire DataFrame into a string format 


Tip: use to_string() to print the entire DataFrame.

If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

max_rows

The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the statement.

```bash
 pd.options.display.max_rows 
 ```
 

In my system the number is 60, which means that if the DataFrame contains more than 60 rows, 

the print(df) statement will return only the headers and the first and last 5 rows.


You can change the maximum rows number with the same statement.


Pandas Read JSON

Read JSON

Big data sets are often stored, or extracted as JSON.


JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.


In our examples we will be using a JSON file called 'data.json'.


Tip: use to_string() to print the entire DataFrame.


Dictionary as JSON

JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:



Pandas - Analyzing DataFrames

Viewing the Data

One of the most used method for getting a quick overview of the DataFrame, is the head() method.


The head() method returns the headers and a specified number of rows, starting from the top.



Note: if the number of rows is not specified, the head() method will return the top 5 rows.


There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom.



Info About the Data

The DataFrames object has a method called info(), that gives you more information about the data set.



Null Values


The info() method also tells us how many Non-Null values there are present in each column, and in our data 

In our data set it seems like there are 5 of 5 Non-Null values in the "Name" column.


Which means that there are 0 rows with no value at all, in the "Name" column, for whatever reason.


Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data


Pandas - Cleaning Data

Data Cleaning

Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates



The index=False parameter in the to_csv() function is used to prevent pandas from writing row numbers (the index) to the CSV file.



The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).

The data set contains wrong format ("Date" in row 26).

The data set contains wrong data ("Duration" in row 7).

The data set contains duplicates (row 11 and 12).





Empty Cells

Empty cells can potentially give you a wrong result when you analyze data.


Remove Rows

One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.


Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

If you want to change the original DataFrame, use the 

inplace = True argument:


Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.


Replace Empty Values

Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:


Replace Only For Specified Columns

The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:



Replace Using Mean, Median, or Mode


A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Mean = the average value (the sum of all values divided by number of values).


Median = the value in the middle, after you have sorted all values ascending.

Mode = the value that appears most frequently.