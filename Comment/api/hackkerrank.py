# if __name__ == "__main__":
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     i = [int(i) for i in range(0, x + 1)]
#     j = [int(j) for j in range(0, y + 1)]
#     k = [int(k) for k in range(0, z + 1)]
#     lists = [[a, b, c] for a in i for b in j for c in k if a + b + c != n]

# print(lists)


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
