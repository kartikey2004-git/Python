# import csv

# data = [
#     ["ID", "Name", "Age", "Gender", "Math", "Science", "English", "History", "Total Marks", "Percentage", "Grade"],
#     [1, "Alice Johnson", 17, "Female", 88, 92, 85, 90, 355, 88.75, "A"],
#     [2, "Bob Smith", 18, "Male", 76, 81, 79, 84, 320, 80.00, "B"],
#     [3, "Carol White", 17, "Female", 95, 89, 93, 91, 368, 92.00, "A+"],
#     [4, "David Brown", 18, "Male", 65, 74, 70, 72, 281, 70.25, "C"],
#     [5, "Eva Green", 17, "Female", 90, 94, 88, 92, 364, 91.00, "A+"],
# ]


# # Writing to CSV file
# with open("data.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("CSV file created successfully!")






# Load the CSV into a DataFrame:

# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.to_string()) 



# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df) 



# Check the number of maximum returned rows:

# import pandas as pd
# print(pd.options.display.max_rows) 

# returns no of maximum rows in pandas : 60 rows by default






# #set no of maximum rows in dataframe

# import pandas as pd
# pd.options.display.max_rows = 9999
# df = pd.read_csv('data.csv')
# print(df) 





# Load the JSON file into a DataFrame:


# import pandas as pd
# df = pd.read_json('data.json')
# print(df.to_string()) 







# import pandas as pd

# # Attempt to read the JSON file with a different encoding
# try:
#     df = pd.read_json('data.json', encoding='utf-16')
# except UnicodeDecodeError:
#     # If a UnicodeDecodeError occurs, try ISO-8859-1 encoding
#     df = pd.read_json('data.json', encoding='ISO-8859-1')

# print(df.to_string())






# import pandas as pd

# df = pd.read_json('res.json')
# print(df.to_string()) 




# Load a Python Dictionary into a DataFrame:


# import pandas as pd

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df) 




