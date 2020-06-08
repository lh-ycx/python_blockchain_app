from multiprocessing import Process,Lock
import os, time, random
import subprocess
import requests
import numpy as np
import threading
from readerwriterlock import rwlock

clients_num = 100
default_port = 8000
total_blocks = 10000
cur_blocks = 0
f = open('pow.log', 'a')
lock = threading.Lock()


def client_task(port,performance):
    global f
    global total_blocks
    global cur_blocks
    
    client_name = "worker #{}".format(port-default_port)
    f.write('Run task {}, performance: {}\n'.format(port-default_port,performance))
    print('Run task {}, performance: {}'.format(port-default_port,performance))
    time.sleep(2)

    while cur_blocks < total_blocks:
        time.sleep(1/performance) # simulate mining
        lock.acquire()
        t = time.asctime()
        print("{} {}: block #{} is mined".format(t,client_name, cur_blocks) )
        f.write("{} {}: block #{} is mined.\n".format(t,client_name, cur_blocks))
        f.flush()
        cur_blocks+=1
        lock.release()

    
if __name__ == "__main__":
    pool = []
    temp_f = open('pow.log','w')
    temp_f.close()
    performances = np.random.pareto(2,clients_num)
    for c in range(clients_num):
        threading.Thread(target=client_task, args=(default_port+c,performances[c])).start()