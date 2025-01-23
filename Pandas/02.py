# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a)
# print(myvar)
# print(myvar[0])

# there is column of given data on certain index number , indexing starts from 0



# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)
# print(myvar["y"])



# key value pair acts as labels and its values assigned to it

# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)

# print(myvar)




# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)



# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)