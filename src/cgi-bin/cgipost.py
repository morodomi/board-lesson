#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector

# MySQLへの接続
conn = mysql.connector.connect(
  host='mysql',
  port='3306',
  user='user',
  password='password',
  database='board'
)
conn.ping(reconnect=True)
isConnected = conn.is_connected()

# 接続できているかどうか確認
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
text = form.getvalue('text')

htmlText = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Received Data</title>
</head>
<body>
    <h1>%s</h1>
    <div>
        Database Connection:%s
    </div>
</body>
</html>
'''

print("Content-Type:text/html;charset=utf-8\n")    # HTML is following
print()                             # blank line, end of headers
print(htmlText % (text, isConnected))
