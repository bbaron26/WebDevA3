import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5561")

for i in range(10):
    message = f"Task {i}"
    print(f"Sending: {message}")
    socket.send_string(message)
    time.sleep(1)