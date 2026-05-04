import os
import copy
import matplotlib.pyplot as plt
import math


def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        adj = {}
        for i in range(n):
            row = list(map(int, f.readline().split()))
            adj[i] = {j for j in range(n) if row[j] == 1}
    return n, adj

def rm_v(adj, v):
    del adj[v]
    for u in adj:
        adj[u].discard(v)
    return adj

def rm_vs(adj, vertices):
    for v in vertices:
        rm_v(adj, v)
    return adj

counter = 0

def r0(adj):
    global counter
    counter += 1

    if not adj:
        return 0

    isolated = [v for v in adj if len(adj[v]) == 0]
    if isolated:
        return len(isolated) + r0(rm_vs(adj, isolated))

    v = max(adj, key=lambda v: len(adj[v]))
    a1 = copy.deepcopy(adj)
    for u in (adj[v] | {v}):
        rm_v(a1, u)
    a2 = copy.deepcopy(adj)
    rm_v(a2, v)
    return max(1 + r0(a1), r0(a2))


folder = 'lab2data/'
results = []
print(os.listdir(folder))

r0_files = ['g30.in', 'g50.in', 'g40.in','g60.in','g4.in']
for filename in r0_files:
    
    n, adj = read_graph(os.path.join(folder, filename))
    counter = 0
    mis = r0(adj)
    results.append((n, counter))
    print(f"{filename}: n={n}, MIS={mis}, calls={counter}")

sizes = [r[0] for r in results]
log_calls = [math.log10(r[1]) for r in results]

plt.scatter(sizes, log_calls)
plt.xlabel("Vertex count (n)")
plt.ylabel("log10(recursive calls)")
plt.title("R0: Recursive calls vs instance size")
plt.savefig("r0_calls.png")
plt.show()