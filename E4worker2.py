import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5561")

while True:
    task = socket.recv_string()
    print(f"Worker 2 processing {task}")