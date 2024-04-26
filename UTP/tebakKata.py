# def main():
#     n = int(input())
#     kata_tebakan = input()
#     nyawa = n

#     if n <= 0 or n > 10:
#         print("INPUTAN SALAH")
#         return

#     for i in range(n):
#         tebakan = input()
#         if tebakan == kata_tebakan:
#             print("MENANG", nyawa)
#             return
#         nyawa -= 1

#     print("KALAH 0")

# if __name__ == "__main__":
#     main()

def main():
    jumlah_percobaan = int(input())
    kata_tebakan = input()
    sisa_nyawa = jumlah_percobaan

    if jumlah_percobaan <= 0 or jumlah_percobaan > 10:
        print("INPUTAN SALAH")
        return

    for _ in range(jumlah_percobaan):
        tebakan = input()
        if tebakan == kata_tebakan:
            print("MENANG", sisa_nyawa)
            return
        sisa_nyawa -= 1

    print("KALAH 0")

if __name__ == "__main__":
    main()
