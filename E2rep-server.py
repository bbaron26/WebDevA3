import zmq
import time
try: 
    context = zmq.Context()
    socket = context.socket(zmq.REP) 
    socket.setsockopt(zmq.LINGER, 0)
    socket.bind("tcp://127.0.0.1:5558")
    while True: 
        message = socket.recv()
        print("Received request: ", message)
        time.sleep (1)
        socket.send_string("Hello, client!")
except KeyboardInterrupt: 
    context.destroy()
    socket.close()