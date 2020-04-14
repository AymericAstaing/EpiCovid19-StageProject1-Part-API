import Api as api
import os
import signal

HOST, PORT = '127.0.0.1', 5000

def to_dict():
    d = {}
    d['width'] = 100
    d['height'] = 200
    return d

if __name__ == '__main__':
    api.start(host=HOST, port=PORT)
    try:
        while True:
            api.data = to_dict()
    except KeyboardInterrupt:
        os.kill(os.getpid(), signal.SIGINT)
