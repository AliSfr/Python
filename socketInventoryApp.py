import socket
port_list = []
banner_list = []
with open("inventoryIP.txt","r",encoding="utf-8") as file:
    icerik = file.read()
for ip in icerik.splitlines():
    print(ip)
    for port in range(1,25):
        try:
            soket=socket.socket()
            soket.connect((str(ip),int(port)))
            banner=soket.recv(1024)
            banner_list.append(str(banner))
            port_list.append(str(port))
            soket.close()
            print(port)
            print(banner)
            if "SSH" in str(banner):
                print("System can be Linux or Network device!") 
                log = str(ip)+"\n"
                with open("linux.txt","a",encoding="utf-8") as file:
                    file.write(log)
        except:
            pass
print(port_list)
print(banner_list)
