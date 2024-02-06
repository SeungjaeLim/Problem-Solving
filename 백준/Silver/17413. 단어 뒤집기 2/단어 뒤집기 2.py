s = list(input())
ans = []
tmp = []
tag = False
for i in s:

    if i == '>':
        tag = False
        ans.append(i)
    elif i == '<':
        tag = True
        tmp.reverse()
        ans.extend(tmp)
        tmp = []
        ans.append(i)
    
    elif tag:
        ans.append(i)
    elif i == " ":
        tmp.reverse()
        ans.extend(tmp)
        tmp = []
        ans.append(i)
    else:
        tmp.append(i)

if len(tmp) > 0:
    tmp.reverse()
    ans.extend(tmp)
    
print("".join(ans))