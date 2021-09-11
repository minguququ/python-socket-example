
import socket
import json

HOST = '127.0.0.1'    

PORT = 9999             

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
 

payload = {}
payload["0"] = "jaeil"
payload["1"] = "duckil"
payload["2"] = "mingu"

for i in range(1,10):    
    msg = json.dumps(payload)    
    #print("please input msg")
    #msg = str(input())
    data = msg.encode();    
    #data = msg
    length = len(data);

    client_socket.sendall(length.to_bytes(4, byteorder="little"));    
    client_socket.sendall(data);
    
    data = client_socket.recv(4);
    
    length = int.from_bytes(data, "little");
    
    data = client_socket.recv(length);
    
    msg = data.decode();
    
    print(i, 'Received from : ', msg);
            
client_socket.close();
