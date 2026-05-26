import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z]{1}[a-z']+\s{0,1}[A-Z]{1}[A-za-z-']*"
name_regex = re.compile(name)

phone_number = r"\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}"
phone_regex = re.compile(phone_number)

email_address = r"(?!(^\d.))(?!.*\.{2})[a-z0-9\.]+@[a-z]+.[a-z]+"
email_regex = re.compile(email_address)
