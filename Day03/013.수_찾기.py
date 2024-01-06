#https://www.acmicpc.net/problem/1920

n = int(input())
# 찾을 범위
N = set(map(int, input().split()))
# m의 개수
number_of_M = int(input())
# 찾아야 하는 수 배열
M = map(int, input().split())

for i in M:
    if i in N:
        print(1)
    else:
        print(0)