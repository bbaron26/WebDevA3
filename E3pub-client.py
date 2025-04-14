import sys, zmq

ip = sys.argv[1]
port = sys.argv[2]

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://" + ip + ":" + port)
socket.setsockopt_string(zmq.SUBSCRIBE, "")  

try:
    while True:
        message = socket.recv_string()
        print(f"Received: {message}")
except KeyboardInterrupt:
    context.destroy()
    socket.close()
