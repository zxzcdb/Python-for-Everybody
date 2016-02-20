# Welcome XINGZHOU ZHU from Using Python to Access Web Data

# Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

#     http://www.pythonlearn.com/code/intro-short.txt

# There are three ways that you might retrieve this web page and look at the response headers:

#     Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
#     Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
#     Use the telnet program as shown in lecture to retrieve the headers and content.

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com',80))
mysocket.send(b'GET http://www.pythonlearn.com/code/intro-short HTTP/1.0\n\n')

while True:
    txt = mysocket.recv(99999)
    if ( len(txt) < 1 ):
      break
    print (txt)
mysocket.close()

# HTTP/1.1 200 OK
# Date: Sat, 20 Feb 2016 13:03:17 GMT
# Server: Apache
# Content-Location: intro-short.txt
# Vary: negotiate
# TCN: choice
# Last-Modified: Mon, 12 Oct 2015 14:55:29 GMT
# ETag: "20f7401b-1d3-521e9853a392b;52c32f8beef53"
# Accept-Ranges: bytes
# Content-Length: 467
# Cache-Control: max-age=604800, public
