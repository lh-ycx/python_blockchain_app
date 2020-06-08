import matplotlib.pyplot as plt
from collections import defaultdict

log_dirs = ['pos.log','pow.log']
for log_dir in log_dirs:
    plt.figure()
    miner2cnt = defaultdict(int)

    with open(log_dir, 'r') as f:
        for line in f:
            if 'is mined' in line:
                miner = int(line.split()[6][1:-1])
                miner2cnt[miner]+=1
    data = []
    for _ in miner2cnt.keys():
        data.append(miner2cnt[_])
    data.sort()
    # print(data)
    s = sum(data)
    cdf_x = [_ for _ in data]
    cdf_y = [data[0]/s]
    for _ in range(1,len(data)):
        data[_] += data[_-1]
        cdf_y.append(data[_]/s)

    # print(cdf_y)

    plt.plot(cdf_x,cdf_y)
    plt.xlabel("Block Count",fontsize=20)
    plt.ylabel("CDF",fontsize=20)
    plt.title("{}".format(log_dir[:-4]),fontsize=25)
    plt.savefig("{}.png".format(log_dir))

