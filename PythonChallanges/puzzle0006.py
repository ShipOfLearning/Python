# find the total no of word count.
# str = "Today is wonderfull day"
# result = 4
import re
str = "Today is wonderfull day 1234_  "
# result = len(str.split(' '))
# print(f"the total no of words is {result}")
result = len(re.findall(r"\w+",str))
print(f"the total no of words is {result}")
