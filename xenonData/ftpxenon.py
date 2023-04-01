import os
import vars_setup
import socket

hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
port = 8080

os.chdir(vars_setup.newPath(vars_setup.dataBasePath,"temp"))
os.system("title FTP Xenon v0.3")
print(f"Start browser in your device which conneced to the same wifi ({hostname})\nType http://{ip}:{port}")
print("Don't forget to stop your FTP Xenon v0.3 server: Type:- c-ftp")
os.system(f"python -m http.server {port} --bind {ip}")