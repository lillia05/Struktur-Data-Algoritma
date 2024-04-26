from collections import deque

def find_solution(arr):
    n = len(arr)
    target = list(range(n))
    visited = set()
    q = deque([(arr, 0, [])])

    while q:
        state, steps, moves = q.popleft()
        if state == target:
            return steps, moves
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        empty_index = state.index(0)
        for i in range(n):
            if i == empty_index:
                continue
            new_state = state[:]
            new_state[empty_index], new_state[i] = new_state[i], new_state[empty_index]
            q.append((new_state, steps + 1, moves + [new_state]))

    return -1, []

def main():
    case = int(input())
    initial_state = list(map(int, input().split()))

    print("Urutan awal    :", [0] + initial_state)
    steps, moves = find_solution([0] + initial_state)

    if case == 1:
        print("Jumlah langkah:", steps)
    elif case == 2:
        for i, move in enumerate(moves):
            print("Langkah -", i + 1, "   :", move)
        print("Jumlah langkah:", steps)
    else:
        print("INPUTAN SALAH")

if __name__ == "__main__":
    main()
