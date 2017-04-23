#! /usr/bin/env python3
#  passwordmanager.py - An insecure password manager program.

import sys
import pyperclip

accounts = {'abc123@gmail.com':'hkjfhvkfdhvlk', 'def456@rediffmail.com':'oiojlsamd','ghi789@yahoo.com':'8u98uhdfg'}
if len(sys.argv) < 2:
    print ('\nPlease add loginid as an argument.\nUSAGE: py.exe passwordmanager.py [loginid]\n')
    sys.exit()
else:
    loginid = sys.argv[1]

if loginid in accounts:
    pyperclip.copy(accounts[loginid])
    print ('\nPassword for '+ loginid + ' copied to clipboard.\n')
else:
    print ('\nLogin ID entered does not exist!!!\n')
    
