import ftplib
from ftplib import FTP
import os

ip, port = input("Enter the IP address and the port, separated by a space: ").split(" ")

server = FTP()
server.connect(ip, int(port))
server.login()

server.retrlines("LIST")

print(os.getcwd())

filename = input("Enter the name of the file you want to download: ")

while True:
    try:
        server.retrbinary("RETR " + filename, open(filename, "wb").write)
        break
    except ftplib.all_errors as e:
        print(e)
        filename = input("Try again: ")
        continue
