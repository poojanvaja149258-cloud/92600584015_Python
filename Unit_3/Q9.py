import re


text = "Python is fun. I love Python 3.13!"

pattern = "Python"


match_obj = re.match(pattern, text)
print("1. re.match() result :", match_obj.group() if match_obj else "No match at start")

search_obj = re.search(pattern, text)
print("2. re.search() result:", search_obj.group() if search_obj else "No match found")


findall_list = re.findall(pattern, text)
print("3. re.findall() result:", findall_list)
