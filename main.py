import socket as SK

hostName = SK.gethostname()
ipaddress = SK.gethostbyname(hostName)

print(f"My IP Address : {ipaddress}")