import zmq
import random
import sys
import time
try:
    # Port value is the first argument from the command line
    ip = sys.argv[1]
    port = sys.argv[2]
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://"+ip+":"+port)
    while True:
        message = "News update: something happened"
        # Print 
        print(f"Publishing: {message}")
        socket.send_string(message)
        time.sleep(2)
except KeyboardInterrupt:
    context.destroy()
    socket.close()