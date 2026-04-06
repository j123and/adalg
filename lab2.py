import os


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

def r0(n,adj):
    if len(adj)==0:
        return 0
    for i in range(n):
        neighbors = [j for j in range(n) if adj[i][j] == 1]

        if len(neighbors) == 0:
            return 1+r0(n-1,rm_v(adj,i))
        
        v = max(adj, key=lambda v: len(adj[v]))
        adj1 = rm_v(adj,(adj[v]|{v}))
        adj2 = rm_v(adj, v)
        return max(1+r0(n-1, adj1), r0(n-1, adj2))

def r1(n,adj):
    pass

def r2(n,adj):
    ...


folder = 'lab2data/'

for filename in os.listdir(folder):
    if filename.endswith(".in"):
        n, adj = read_graph(os.path.join(folder, filename))
        print(f"{r0(n,adj)}: independent set")