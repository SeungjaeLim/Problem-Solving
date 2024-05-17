def solution(numbers, target):
    answer = bfs(numbers[0], numbers[1:], target) + bfs(-numbers[0], numbers[1:], target)
    return answer

def bfs(n, left, target):
    if not left:
        if n == target:
            return 1
        else:
            return 0
    else:
        return bfs(n + left[0], left[1:], target) + bfs(n - left[0], left[1:], target)