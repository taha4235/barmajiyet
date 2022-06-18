import socket
import webbrowser
taha = input("enter url site :")
ip = socket.gethostbyname(taha)
print(ip)
go = webbrowser.open("www.bing.com/search?q=ip : "+ ip)
