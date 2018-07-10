import getpass
import sys
import telnetlib

HOST = "192.168.255.134"

user = raw_input("Enter your remote account: ")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")

tn.write(user + "")

if password:
    tn.read_until("Password: ")
    tn.write(password + "")

tn.write("dir")

tn.write("exit")

print tn.read_all()

# Source: http://www.pythonforbeginners.com/code-snippets-source-code/python-using-telnet