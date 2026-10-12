import re

with open("data.txt", "w") as f:
    f.write("Contact us at support@example.com before 25-12-2026.\n")
    f.write("For sales, email sales.help@office.org by 01-01-2027.")

email_pattern = r"[a-zA-Z0-9._+,-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
date_pattern = r"\d{2}-\d{2}-\d{4}"

with open("data.txt", "r") as file:
    content = file.read()
    
    emails = re.findall(email_pattern, content)
    dates = re.findall(date_pattern, content)

print("--- Extracted Information ---")
print("Emails Found :", emails)
print("Dates Found  :", dates)
