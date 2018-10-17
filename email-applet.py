#!/usr/bin/env python

import imaplib
import sys

icon = ""

with open('config', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if 'password' in line:
            line = line.strip().split(' ')
            password = line[1]
        if 'username' in line:
            line = line.strip().split(' ')
            username = line[1]

obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
obj.login(username, password)
obj.select()
unread = len(obj.search(None,'UnSeen')[1][0].split())

if unread > 0:
    print(f'{icon}({unread})')
    sys.exit(0)
else:
    sys.exit(0)
