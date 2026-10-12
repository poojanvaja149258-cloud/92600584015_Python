import re

text = "My phone number is 98765-43210 and my code is 4567."

search_result = re.search(r"\d+", text)
if search_result:
    print("1. Search Result (First match found):", search_result.group())

all_numbers = re.findall(r"\d+", text)
print("2. Findall Result (All matches):", all_numbers)

match_result = re.match(r"My", text)
if match_result:
    print("3. Match Result (Found at start):", match_result.group())
else:
    print("3. Match Result: No match at the very beginning.")
