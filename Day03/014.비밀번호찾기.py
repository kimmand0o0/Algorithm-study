#https://www.acmicpc.net/problem/17219

N, M = map(int, input().split())

url_list = {}

for i in range(N):
    url, password = input().split()
    url_list[url] = password

for j in range(M):
    find_url = input()
    print(url_list[find_url])