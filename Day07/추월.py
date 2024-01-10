# https://www.acmicpc.net/problem/2002

from collections import deque

n = int(input())
in_tunnel = deque()


for i in range(n):
    in_tunnel.append(input())

answer = 0

for i in range(n):
    out_tunnel = input()
    if out_tunnel == in_tunnel[0]:
        in_tunnel.popleft()
    else:
        in_tunnel.remove(out_tunnel)
        answer += 1

print(answer)