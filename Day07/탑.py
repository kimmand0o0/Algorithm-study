#https://www.acmicpc.net/problem/2493

n = int(input())
towers = list(map(int, input().split()))
biggist = [(0, 0)]
answer = []

for i in range(len(towers)):
    if biggist[-1][0] < towers[i]:
        while biggist[-1][0] < towers[i]:
            biggist.pop()
            if len(biggist) == 0:
                answer.append(0)
                break
        if biggist:
            answer.append(biggist[-1][1])
        biggist.append((towers[i], i+1))
    else:
        biggist.append((towers[i], i+1))
        answer.append(i)

print(*answer)