from http.server import BaseHTTPRequestHandler
import os
import re

all = {}

def process(file, pattern = ''):
    file1 = open(file, 'r', encoding="utf8")
    Lines = file1.readlines()
    for line in Lines:
        if pattern != '':
            output = re.findall(pattern, line, flags=re.IGNORECASE)
            if output.__len__() > 0:
                tar = output[0]
                tar = tar.strip().lower()
                if tar.count(' ') == 1:
                    if all.get(tar) == None:
                        all[tar] = 1
        else :
            tar = line
            tar = tar.trip().lower()
            if tar.count(' ') == 1:
                if all.get(tar) == None:
                    all[tar] = 1


def preprocess() :
    process('tudien.txt', '^(.*)\n$')
    lines = list(all.keys())
    with open('all.txt', 'w', encoding="utf8") as f:
        for line in lines:
            f.write(f"{line}\n")

preprocess()

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            preprocess()
            self.path = '/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                text = getTarget()
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)


