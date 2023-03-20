
import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

email = 'test@ce.va.com'
print(bool(re.fullmatch(regex, email)))