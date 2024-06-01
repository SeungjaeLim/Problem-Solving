def solution(phone_book):
    answer = True
    phoneBook = {}
    for i in phone_book:
        phoneBook[i] = 0
    for i in phone_book:
        for j in range(len(i) - 1):
            if i[0:j+1] in phoneBook:
                answer = False
    return answer