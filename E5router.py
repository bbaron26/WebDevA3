import zmq

context = zmq.Context()
socket = context.socket(zmq.ROUTER)
socket.bind("tcp://127.0.0.1:5566")  

print("Server is running...")

clients = []

while True:
    client_id, message = socket.recv_multipart()

    # Convert client_id from bytes to a string safely
    client_id_str = client_id.decode(errors="ignore")

    # Add the client to the list if it's not already there
    if client_id not in clients:
        clients.append(client_id)
        print(f"New client connected: {client_id_str}")
    
    print(f"Received message from {client_id_str}: {message.decode()}")
    
    # Broadcast the message to all clients except the sender
    for client in clients:
        if client != client_id:
            print(f"Sending message to {client.decode(errors='ignore')}")
            socket.send_multipart([client, message])
