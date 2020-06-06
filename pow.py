from multiprocessing import Process
import os, time, random
import subprocess
import requests

clients_num = 10
default_port = 8000
block_num = 10

def client_task(port):
    client_name = "worker #{}".format(port-default_port)
    print('Run task (%s)...' % ( os.getpid()))
    CMD = "python node_server_pow.py {}".format(port)
    proc = subprocess.Popen(CMD, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, bufsize=-1)
    
    data = {"node_address": "http://127.0.0.1:8000"}
    time.sleep(2)
    res = requests.post(url="http://127.0.0.1:{}/register_with".format(port),json=data)
    print(client_name, ":", res.text)

    for cnt in range(block_num):
        res = requests.get(url="http://127.0.0.1:{}/mine".format(port))
        print(client_name, ":", res.text)


    
if __name__ == "__main__":
    pool = []
    for c in range(clients_num):
        p = Process(target=client_task,args=(default_port+c,))
        p.start()
        pool.append(p)
    for p in pool:
        p.join()