import re
import pyperclip

# Create phone number regex.

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex.

emailRegex = re.compile(r'''(

# some.+_thing@some._+thing

[a-zA-Z0-9.+_]+       # username
 @       # @ symbol
 [a-zA-Z0-9.+_]+      # domain name

)''', re.VERBOSE)

# TODO: Find matches in clipboard text.

dataCopied = str(pyperclip.paste())

phoneNumbers = []

extractedPhn = phoneRegex.findall(dataCopied)
for data in extractedPhn :
    phoneNumbers.append(data[0])

extractedEmail = emailRegex.findall(dataCopied)

# TODO: Copy results to the clipboard.

pyperclip.copy('\n'.join(phoneNumbers) + '\n' + '\n'.join(extractedEmail) )
