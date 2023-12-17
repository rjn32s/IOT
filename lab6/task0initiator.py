import socket

PORT = 11153
s = socket.scket(socket.AF_INET , socket.SOCK_STREAM)

s.bind(('' , PORT))

print("1")
s.listen(10)
print("2")

conn , addr = s.accept()
print("Now Sever Will send the data")

while True:
    conn.sendall(bytes("Hello Form ESP0" , "utf-8"))
    conn.close()
    break