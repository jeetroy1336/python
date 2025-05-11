# What is a regular expression
# Given a string "abc123xyz456" containing alphanumeric characters,
# write a regular expression to extract all the digits (0–9) from the string.

import re

text = "abc123xyz456"

digits = re.findall(r'\d', text)

print(digits)



# practice questions
#----------------------------------------------------------------

# 1. Extract all digits from the string: "order123invoice456total789".
# import re

# text = "order123invoice456total789"

# digits = re.findall(r'\d', text)
# print(digits)

#----------------------------------------------------------------

# 2. Find all words in the sentence: "Python is fun and powerful!".
# import re

# text = "Python is fun and powerful!"

# result = re.findall(r'\w+', text)
# print(result)

#----------------------------------------------------------------

# 3. Check if a string starts with "Hello"
# import re

# text = "Hello this is some text"

# if(re.findall(r'^Hello', text)):
#     print("Found")
# else:
#     print("Not found")

#----------------------------------------------------------------

# 4. Split a string by one or more spaces: "Split this sentence"

# import re

# text = "Split this sentence"

# result = re.split(r'\s', text)

# for i in result:
#     print(i)

#----------------------------------------------------------------









































































































































