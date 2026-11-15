import socket

def start_client():
    host = 'REPLACE_WITH_ACTUAL_SERVER_IP'
    port = 5000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    while True:
        msg = input("Client: ")
        s.send(msg.encode())
        
        data = s.recv(1024).decode()
        if not data:
            break
        print(f"Server: {data}")
        
    s.close()

if __name__ == '__main__':
    start_client()