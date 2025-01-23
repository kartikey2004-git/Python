# Return a new Data Frame with no empty cells:

# import pandas as pd
# df = pd.read_csv('data.csv')
# new_df = df.dropna()
# print(new_df.to_string())


# Remove all rows with NULL values:


# import pandas as pd
# df = pd.read_csv('data.csv')
# df.dropna(inplace = True)
# print(df.to_string())



# Replace NULL values with the number 130

# import pandas as pd
# df = pd.read_csv('data.csv')
# df.fillna(130, inplace = True)
# print(df.to_string())



# Replace NULL values in the "Calories" columns with the number 130


# import pandas as pd

# df = pd.read_csv('data.csv')

# df["Percentage"].fillna(130, inplace = True)
# print(df.to_string())




# Calculate the MEAN, and replace any empty values with it:

# import pandas as pd

# df = pd.read_csv('data.csv')
# x = df["Percentage"].mean()


# df["Percentage"].fillna(x, inplace = True)
# print(df.to_string())




# Calculate the MEDIAN, and replace any empty values with it

# import pandas as pd

# df = pd.read_csv('data.csv')
# x = df["Percentage"].median()


# df["Percentage"].fillna(x, inplace = True)
# print(df.to_string())



# Calculate the MODE, and replace any empty values with it


# import pandas as pd

# df = pd.read_csv('data.csv')
# x = df["Percentage"].mode()[0]


# df["Percentage"].fillna(x, inplace = True)
# print(df.to_string())



# Since .mode() can return multiple modes.

#  [0] is used to select the first mode from the result (i.e., the most frequent value).

#  If there is only one mode, it will still be at index 0.