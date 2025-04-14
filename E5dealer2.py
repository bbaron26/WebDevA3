import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.connect("tcp://127.0.0.1:5566")  

client_id = f"client_{random.randint(1, 1000)}"
socket.setsockopt(zmq.IDENTITY, client_id.encode())

print(f"Client {client_id} connected")

while True:
    message = f"Hello from {client_id}"
    socket.send_string(message)
    print(f"Sent message: {message}")
    
    response = socket.recv_string()
    print(f"Received message: {response}")
    
    time.sleep(1)
