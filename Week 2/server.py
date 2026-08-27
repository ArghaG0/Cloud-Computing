import socket

def start_server():
    host = '0.0.0.0'
    port = 5000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    
    print("Server is listening...")
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")
        
        msg = input("Server: ")
        conn.send(msg.encode())
        
    conn.close()
    s.close()

if __name__ == '__main__':
    start_server()