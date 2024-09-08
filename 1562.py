mod = 100000000
n = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n + 1)]  # 길이, 마지막 숫자, 마스크

# 초기 상태 설정: 길이가 1인 경우
for i in range(1, 10):
    dp[1][i][1 << i] = 1

# DP 테이블 채우기
for i in range(2, n + 1):
    for j in range(10):
        for k in range(1024):
            if j > 0:
                msk = k | (1 << j)
                dp[i][j][msk] = (dp[i][j][msk] + dp[i - 1][j - 1][k]) % mod
            if j < 9:
                msk = k | (1 << j)
                dp[i][j][msk] = (dp[i][j][msk] + dp[i - 1][j + 1][k]) % mod

# 최종 결과 계산
res = 0
for i in range(10):
    res = (res + dp[n][i][1023]) % mod

print(res)
