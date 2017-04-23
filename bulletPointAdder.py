#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text_copied = pyperclip.paste()
text_list = text_copied.split('\n')
new_text_list = []
for line in text_list:
    line = '* ' + line
    new_text_list.append(line)

new_text = '\n'.join(new_text_list)
pyperclip.copy(new_text)


