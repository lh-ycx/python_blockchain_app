import matplotlib.pyplot as plt
from collections import defaultdict

#log_dirs = ['qianlang-3.log','qianlang-4.log','qianlang-5.log','qianlang-6.log','qianlang-7.log','qianlang-8.log','qianlang-9.log','qianlang-10.log',]
log_dirs = ['houlang-0.3.log','houlang-0.4.log','houlang-0.5.log','houlang-0.6.log','houlang-0.7.log','houlang-0.8.log','houlang-0.9.log','houlang-1.0.log',]
box_data = []
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
    box_data.append(data)
    # print(data)
    '''
    s = sum(data)
    cdf_x = [_ for _ in data]
    cdf_y = [data[0]/s]
    for _ in range(1,len(data)):
        data[_] += data[_-1]
        cdf_y.append(data[_]/s)
    '''
    # print(cdf_y)

    # plt.plot(cdf_x,cdf_y)
plt.boxplot(x=box_data, showfliers = False, labels = ["-0.7", "-0.8","-0.9","-1.0","-1.1", "-1.2","-1.3","-1.4"])
#plt.boxplot(x=box_data, showfliers = False, labels = ["1.1", "1.2","1.3","1.4","1.5", "1.6","1.7","1.8"])
plt.xlabel("Consensus Algorithms",fontsize=20)   
plt.ylabel("Block Count",fontsize=20)
# plt.title("{}".format(log_dir[:-4]),fontsize=25)
plt.savefig("houlang.png".format(log_dir))

