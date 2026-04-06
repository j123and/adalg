import sys
from random import randint
import numpy as np
# np.random.seed(4)
def read_input(filename):
    with open(filename) as f:
   
        n, m = map(int, f.readline().split())

        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            adj[u].append((v, w))
            adj[v].append((u, w))
        return adj, n, m

def alg_r(adj,n,m):
    r = [np.random.randint(0, 2) for _ in range(n + 1)]
    return r


def alg_s(adj,n,m):    
    rs = [0 for _ in range(n+1)]
    same = 0
    diff = 0
    new = True
    while new:
        new = False
        for u in range(1,n+1):
                same = 0
                diff = 0
                for v, w in adj[u]:

                    if rs[u] == rs[v]:
                        same += w
                    else:
                        diff += w
                if same-diff >0:
                    rs[u] = 0 if rs[u]==1 else 1
                    new = True
    return rs

def alg_rs(adj,n,m):
    rs = [np.random.randint(0, 2) for _ in range(n + 1)]
    new = True
    while new:
        new = False
        for u in range(1,n+1):
            same = 0
            diff = 0
            for v, w in adj[u]:

                if rs[u] == rs[v]:
                    same += w
                else:
                    diff += w
            if same-diff >0:
                rs[u] = 0 if rs[u]==1 else 1
                new = True
    return rs

def evaluate(adj, n, m, r):
    cut = 0
    for u in range(1, n + 1):
        for v, w in adj[u]:
            if r[u] != r[v]:
                cut += w
    return cut // 2

if __name__=='__main__':
    filename1 = 'pw09_100.9.txt'
    filename2 = 'matching_1000.txt'
    print('for ', filename1,':')
    adj,n,m = read_input(filename1)
    print('     alg_r: ', evaluate(adj, n, m, alg_r(adj,n,m)))
    print('     alg_s: ', evaluate(adj, n, m, alg_s(adj,n,m)))
    print('     alg_rs: ', evaluate(adj, n, m, alg_rs(adj,n,m)))
    print()
    print('for ', filename2,': ')
    adj,n,m = read_input(filename2)
    print('     alg_r: ', evaluate(adj, n, m, alg_r(adj,n,m)))
    print('     alg_s: ', evaluate(adj, n, m, alg_s(adj,n,m)))
    print('     alg_rs: ', evaluate(adj, n, m, alg_rs(adj,n,m)))



    rs_dict = {}
    r_sum = 0
    s_sum = 0
    rs_sum = 0
    m1, m2, m3 =0,0,0
    for i in range(100):
        adj,n,m = read_input(filename1)
        if (t1 := evaluate(adj, n, m, alg_r(adj,n,m))) >m1:
            m1 = t1
        r_sum+= t1
        if (t2 := evaluate(adj, n, m, alg_s(adj,n,m))) >m2:
            m2 = t2
        s_sum+= t2
        if (t3 := evaluate(adj, n, m, alg_rs(adj,n,m))) >m3:
            m3 = t3
        if t3 in rs_dict:
            rs_dict[t3]+=1
        else: rs_dict[t3] = 1
        rs_sum+= t3
    print(m1,m2 ,m3)
    r_avg = r_sum/100
    s_avg = s_sum/100
    rs_avg = rs_sum/100
    print(r_avg, s_avg, rs_avg)


import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.hist(rs_dict, bins=30, edgecolor='white', linewidth=0.5)
plt.title('Distribution of cuts for algorithm RS')
plt.savefig('hist.png')