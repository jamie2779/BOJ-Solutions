import math
n = int(input())

squares = set(i * i for i in range(1, int(math.isqrt(n)) + 1))


if n in squares:
    print(-1)
else:
    ans = 0
    for i in range(1, int(math.isqrt(n // 2)) + 1):
        o = n - i * i
        if o in squares:
            ans += 1

    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            if (i + j) % 2 == 0:
                i = (i + j) // 2
                k = (j - i) // 2
                if k > 0 and i > k:
                    ans += 1

    print(ans)
