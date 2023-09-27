from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import threading
from horse import horserun

PORT = 1488
HORSE_COUNT = 8

class HorseList:
    def __init__(self):
        self.horses = [0.0] * HORSE_COUNT
        self.frame = 0

    def get_posistions(self):
        return self.horses
    
    def update(self, list):
        self.horses = list

    def update_random(self):
        self.horses = [x + random.random() * 0.05 for x in self.horses]
        self.horses = [1 if x > 1 else x for x in self.horses]
        print(str(self.horses))

        if all(h == 1.0 for h in self.horses):
             self.horses = [0.0] * HORSE_COUNT

horse_rankings = HorseList()

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
    

def cycle():
    horse_rankings.update_random()

class GServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(str(horse_rankings.get_posistions()).encode('utf-8'))

def run_server(server_class=HTTPServer, handler_class=GServer, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    # set_interval(cycle, 1 / 10)

    server_thread = threading.Thread(target = run_server)
    server_thread.start()

    horserun("horse.mp4", horse_rankings.update)
