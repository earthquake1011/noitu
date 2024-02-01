from http.server import BaseHTTPRequestHandler
import os
from urllib.parse import urlparse, parse_qs

all = {}

def prepareDic():
    file1 = open('all.txt', 'r', encoding="utf8")
    Lines = file1.readlines()
    for line in Lines:
        splited = line.split(' ')
        if (all.get(splited[0]) != None):
            all[splited[0]][splited[1]] = 1
        else : all[splited[0]] = { splited[1] : 1 }        


prepareDic()

def existedOnIgnore(text):
    rs = False
    listIg = {}
    file2 = open('ignore.txt', 'r', encoding="utf8")
    ignores = file2.readlines()
    for ignore in ignores:
        listIg[ignore.lower().strip()] = 1
    if listIg.get(text.lower().strip()) != None:
        rs = True
    file2.close()
    return rs

def insertIgnore(ignoreToInsert):
    listIg = {}
    file2 = open('ignore.txt', 'r', encoding="utf8")
    ignores = file2.readlines()
    for ignore in ignores:
        listIg[ignore.strip()] = 1
    listIg[ignoreToInsert] = 1
    print(listIg)
    with open('ignore.txt', 'w', encoding="utf8") as f:
        for line in listIg:
            print(listIg)
            f.writelines(f"{line}\n")
    file2.close()

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return
        result = ''
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            prepareDic()
             # Parse query parameters
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            # self.wfile.write(parsed_url.path)

            # Extract the value of the "text" parameter
            text_param = query_params.get('text', [''])[0]
            text_param = text_param.lower().strip()
            ignore = query_params.get('ignore', [''])[0]
            if ignore: insertIgnore(ignore)
            lrs = list(all[text_param])
            min = 10000
            textmin = 'toi chiu'
            for rs in lrs:
                if '-' in rs: continue
                if existedOnIgnore(text_param + ' ' +rs) == False:
                    rs = rs.strip()
                    if (all.get(rs) == None):
                        textmin = rs
                        break
                    else:
                        if (list(all[rs]).__len__() < min):
                            textmin = rs.strip()
                            min = list(all[rs]).__len__()
                            if min ==0 : break
            result = textmin
        except Exception as e:
            print(str(e))
            print('xxxxxxx')
            result = 'Toi chiu'
        self.wfile.write(result.strip().encode('utf-8'))

