class Node:
    __slots__ = ['sum', 'previous']
    def __init__(self, sum, previous):
        self.sum = sum
        self.previous = previous

def main():
    import sys
    input = sys.stdin.readline

    N = int(sys.stdin.readline())
    nodes = [Node(sum=0, previous=None)]  # nodes[0]: deck state after action 0 (initial empty deck)
    current_node = nodes[0]

    for action_number in range(1, N + 1):
        line = sys.stdin.readline().strip()
        if line.startswith('push'):
            _, x = line.split()
            x = int(x)
            current_sum = x + (current_node.sum if current_node else 0)
            current_node = Node(sum=current_sum, previous=current_node)
            nodes.append(current_node)
        elif line == 'pop':
            if current_node is None:
                # According to the problem, pop is not given when the deck is empty
                pass  # Or handle error
            else:
                current_node = current_node.previous
                nodes.append(current_node)
        elif line.startswith('restore'):
            _, i = line.split()
            i = int(i)
            # Ensure i is within bounds
            if 0 <= i <= action_number - 1:
                current_node = nodes[i]
                nodes.append(current_node)
            else:
                # Handle invalid restore index
                pass
        elif line == 'print':
            print(current_node.sum if current_node else 0)
            nodes.append(current_node)  # Deck state doesn't change
        else:
            # Handle invalid action
            pass

main()
