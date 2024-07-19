def generate_sequences(N, M):
    def backtrack(current_sequence):
        if len(current_sequence) == M:
            print(' '.join(map(str, current_sequence)))
            return
        for num in range(1, N + 1):
            if num not in current_sequence:
                current_sequence.append(num)
                backtrack(current_sequence)
                current_sequence.pop()
    
    backtrack([])

N, M = map(int, input().split())

generate_sequences(N, M)
