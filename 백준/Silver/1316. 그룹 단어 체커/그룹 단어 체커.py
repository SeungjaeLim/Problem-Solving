def is_group_word(word):
    alphabet_log = []
    mem = ''
    for char in word:
        if mem == char:
            continue
        else:
            if char in alphabet_log:
                return False
            mem = char
            alphabet_log.append(char)
    return True


n = int(input())
cnt_group_word = 0
for _ in range(n):
    word = input().strip()
    cnt_group_word += is_group_word(word)
print(cnt_group_word)

