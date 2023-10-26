import queue
def convert_adjacent_list(data: list[int]) -> list[int]:
    n = len(data)
    graph = []
    for row in data:
        col = []
        for i in range(0,n):
            if row[i] == 1: col.append(i)
        graph += [col]
    return graph
def convert_tuple_list(data: list[int]) -> list[tuple[int,int]]:
    n = len(data)
    graph = []
    for row in data:
        gr = []
        for i in range(n):
            if row[i] > 0:
                gr.append((row[i],i))
        graph += [gr]
    return graph
def load_data(file_name : str) -> tuple[int,int,int]:
    f = open(file_name,'r')
    lines = f.read().split('\n')
    start_end = (lines[1].split())
    start, end = (int) (start_end[0]), (int) (start_end[1])
    data = []
    for i in range(2,len(lines)):
        dt = []
        for val in lines[i].split(): dt.append(int (val))
        data += [dt]
    f.close()
    return start,end,data
def Path(s: int,t: int,trace: list[int]) -> list[int]:
    trace_path = []
    trace[s] = -1
    if trace[t] == -1: return []
    while t!=-1:
        trace_path.append(t)
        t = trace[t]
    trace_path.reverse()
    return trace_path
def recursion(graph: list[int],trace: list[int],s: int,t: int,check: list[bool]) -> None:
    if s == t: return
    check[s] = 1
    for u in graph[s]:
        if check[u] == 0:
            trace[u] = s
            recursion(graph,trace,u,t,check)
def dfs_use_recursion(graph: list[int],s: int,t: int) -> list[int]:
    n = len(graph)
    trace = [-1] * (n + 1)
    check = [0] * (n + 1)
    recursion(graph,trace,s,t,check)
    return Path(s, t, trace)
def dfs_use_stack(graph: list[int],s: int,t: int) -> list[int]:
    n = len(graph)
    trace = [-1]*(n+1)
    check = [0]*(n+1)
    stack = queue.LifoQueue()
    stack.put(s)
    check[s] = 1
    while not stack.empty():
        u = stack.get()
        if u == t:
            break
        for v in graph[u]:
            if check[v] == 0:
                stack.put(v)
                check[v] = 1
                trace[v] = u
    return Path(s, t, trace)

def bfs(graph: list[int],s: int,t: int) -> list[int]:
    n = len(graph)
    trace = [-1] * (n + 1)
    check = [0] * (n + 1)
    q = queue.Queue()
    q.put(s)
    check[s] = 1
    while not q.empty():
        u = q.get()
        if u == t:
            break
        for v in graph[u]:
            if check[v] == 0:
                check[v] = 1
                trace[v] = u
                q.put(v)
    return Path(s, t, trace)
def ucs(graph: list[tuple[int,int]],s: int,t: int) -> tuple[list[int],int]:
    n = len(graph)
    trace = [-1]*(n+1)
    Cost = [1000000000]*(n+1)
    q = queue.PriorityQueue()
    q.put((0,s))
    Cost[s] = 0
    path_found = 0
    while not q.empty():
        tup = q.get()
        (du,u) = tup
        if u == t:
            path_found = 1
            break
        if du != Cost[u]: continue
        for v in graph[u]:
            if Cost[v[1]] > (du + v[0]):
                Cost[v[1]] = du + v[0]
                trace[v[1]] = u
                q.put((du+v[0],v[1]))
    if path_found == 0: return [],-1
    return Path(s, t, trace),Cost[t]

def print_dfs_and_bfs() -> None:
    s, t, data = load_data('INPUT.txt')
    graph = convert_adjacent_list(data)
    print("Result DFS_Recurdion Algorithm")
    path = (dfs_use_recursion(graph, s, t),dfs_use_stack(graph, s, t),bfs(graph, s, t))
    if path[0] == []: print(f"No have path from {s} to {t}")
    else:
        print(f"One path from {s} to {t}: {'->'.join([str(u) for u in path[0]])}")

    print("Result DFS_Stack Algorithm")
    if path[1] == []:
        print(f"No have path from {s} to {t}")
    else:
        print(f"One path from {s} to {t}: {'->'.join([str(u) for u in path[1]])}")
    print()

    print("Result BFS Algorithm")
    if path[2] == []:
        print(f"No have path from {s} to {t}")
    else:
        print(f"One path from {s} to {t}: {'->'.join([str(u) for u in path[2]])}")
    print()
def print_ucs() -> None:
    s, t, data = load_data('INPUT_UCS.txt')
    graph = convert_tuple_list(data)

    print("Result UCS Algorithm")
    path = ucs(graph, s, t)
    if path[0] == []:
        print(f"No have path from {s} to {t}")
    else:
        print(f"One path from {s} to {t}: {'->'.join([str(u) for u in path[0]])}\nCost = {path[1]}")
if __name__ == '__main__':
    print_dfs_and_bfs()
    print_ucs()