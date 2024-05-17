def solution(n, costs):
    return prim(n, costs)

def prim(n, costs):
    edges = []
    ctot = 0
    while len(edges) < n:
        edges, c, costs = concat(edges, costs)
        ctot += c
        if len(edges[0]) == n:
            break
    return ctot
        

def concat(edges, costs):
    m, midx = 10001, -1
    for i, v in enumerate(costs):
        if is_internal(edges, v[0], v[1]):
            continue
        else:
            if v[2] < m:
                midx = i
                m = v[2]
    edges = concat_graph(edges, costs[midx][0], costs[midx][1])
    del costs[midx]
    return edges, m, costs

def is_internal(edges, a, b):
    for i, v in enumerate(edges):
        if a in v and b in v:
            return True
    return False

def concat_graph(edges, a, b):
    a_idx = -1
    b_idx = -1
    
    for i, v in enumerate(edges):
        if a in v:
            a_idx = i
        if b in v:
            b_idx = i

    if a_idx == -1 and b_idx == -1:
        edges.append([a, b])
    elif a_idx == -1:
        edges[b_idx].append(a)
    elif b_idx == -1:
        edges[a_idx].append(b)
    else:
        new_edges = []
        for i, v in enumerate(edges):
            if i == a_idx or i == b_idx:
                continue
            new_edges.append(v)
        new_edges.append(edges[a_idx] + edges[b_idx])
        edges = new_edges
    return edges
        
