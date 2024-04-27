import sys
input = sys.stdin.read

data = input().split()
index = 0

# Read n
n = int(data[index])
index += 1

children = [[] for _ in range(n)]
x = [0] * n
par = [0] * n

# Read x[i] and par[i], build children list
for i in range(n):
    x[i] = int(data[index])
    par[i] = int(data[index + 1]) - 1
    index += 2
    if par[i] != -2:
        children[par[i]].append(i)

inf = 10**17
dp_valid_max = [-inf] * n
dp_all_max = [-inf] * n
dp_without_valid = [-inf] * n

# dfs for valid max
def dfs_valid_max(i):
    dp_valid_max[i] = x[i]
    for to in children[i]:
        child_ret = dfs_valid_max(to)
        dp_valid_max[i] += max(0, child_ret)
    return dp_valid_max[i]

dfs_valid_max(0)

# dfs for all max
def dfs_all_max(i):
    dp_all_max[i] = dp_valid_max[i]
    for to in children[i]:
        child_ret = dfs_all_max(to)
        dp_all_max[i] = max(dp_all_max[i], child_ret)
    return dp_all_max[i]

dfs_all_max(0)

# dfs without valid
def dfs_without_valid(cur):
    for i in range(len(children[cur])):
        c = children[cur][i]
        k = dfs_without_valid(c)
        if dp_valid_max[c] <= 0:
            dp_without_valid[cur] = max(dp_without_valid[cur], dp_all_max[c])
        else:
            dp_without_valid[cur] = max(dp_without_valid[cur], k)
    return dp_without_valid[cur]

dfs_without_valid(0)

# Calculate answer
ans = -inf
for i in range(n):
    ans = max(ans, dp_valid_max[i] + dp_without_valid[i])
    if len(children[i]) >= 2:
        sorted_children = sorted(children[i], key=lambda j: dp_all_max[j], reverse=True)
        ans = max(ans, dp_all_max[sorted_children[0]] + dp_all_max[sorted_children[1]])

print(ans)
