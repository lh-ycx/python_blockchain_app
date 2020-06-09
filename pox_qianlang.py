from multiprocessing import Process,Lock
import os, time, random
import subprocess
import requests
import numpy as np
import threading
from readerwriterlock import rwlock
import random

stacks_num = 10000
clients_num = 100
default_port = 8000
total_blocks = 10000
cur_blocks = 0



if __name__ == "__main__":
    pool = []
    f = open('qianlang.log','w')
    stacks_p = np.random.pareto(3,clients_num)
    stacks_p = stacks_p/sum(stacks_p)
    stacks = set(range(stacks_num))
    clients = [set() for _ in range(clients_num)]
    for i in range(len(clients)):
        clients[i].update(random.sample(stacks, int(stacks_num*stacks_p[i])))
        stacks = stacks - clients[i]
        # print(clients)
    clients[0].update(stacks)
    stacks = set(range(stacks_num))
    for cur_blocks in range(total_blocks):
        _ = random.sample(stacks, 1)
        for i in range(clients_num):
            if _[0] in clients[i]:
                client_name = "worker #{}".format(i)
                t = time.asctime()
                print("{} {}: block #{} is mined".format(t,client_name, cur_blocks) )
                f.write("{} {}: block #{} is mined.\n".format(t,client_name, cur_blocks))
                break
    f.close()
