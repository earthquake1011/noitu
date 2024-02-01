import time
from http.server import HTTPServer
from server import Server
import re

HOST_NAME = 'localhost'
PORT = 6969
FILES = {
    'tudien.txt' : '^(.*)\n$',
    'words.txt': '^{"text": "(.*)", "source".*\n$'
}

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
    for file,regex in FILES.items():
        process(file,regex)
    
    lines = list(all.keys())
    with open('all.txt', 'w', encoding="utf8") as f:
        for line in lines:
            if line != '':
                f.write(f"{line}\n")


if __name__ == "__main__":
    httpd = HTTPServer((HOST_NAME,PORT),Server)
    print(time.asctime(), "Start Server - %s:%s"%(HOST_NAME,PORT))
    try:
        preprocess()
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(),'Stop Server - %s:%s' %(HOST_NAME,PORT))
