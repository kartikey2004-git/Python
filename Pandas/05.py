# Get a quick overview by printing the first 10 rows of the DataFrame:

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.head(10))



# Print the first 5 rows of the DataFrame:

# import pandas as pd

# df = pd.read_csv('data.csv')

# # Print the last 5 rows of the DataFrame:
# print(df.tail())

# # print(df.head())






# Print information about the data:

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.info()) 



# returns


# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 11 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   ID           5 non-null      int64
#  1   Name         5 non-null      object
#  2   Age          5 non-null      int64
#  3   Gender       5 non-null      object
#  4   Math         5 non-null      int64
#  5   Science      5 non-null      int64
#  6   English      5 non-null      int64
#  7   History      5 non-null      int64
#  8   Total Marks  5 non-null      int64
#  9   Percentage   5 non-null      float64
#  10  Grade        5 non-null      object
# dtypes: float64(1), int64(7), object(3)
# memory usage: 572.0+ bytes
# None