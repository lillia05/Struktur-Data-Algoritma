def MinimumSwaps(arr):
    swap = 0
    n = len(arr)
    
    for i in range(n):
        while arr[i] != i + 1: 
            swap += 1
            indeks_benar = arr[i] - 1
            arr[i], arr[indeks_benar] = arr[indeks_benar], arr[i]
    
    return swap

def main():
    n = int(input())
    bilangan = list(map(int, input().split()))
    
    min_tukar = MinimumSwaps(bilangan)
    print(min_tukar)

if __name__ == "__main__":
    main()
