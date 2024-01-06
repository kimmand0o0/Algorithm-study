# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 만약 문자열이 2보다 작으면 그대로 반환
        if len(s) < 2:
            return len(s)

        q = deque()
        answer = {}

        # 배열만큼 순회하면서 찾음
        for i in range(len(s)):
            # 만약 q에 같은 값이 없다면 값을 추가
            if s[i] not in q:
                q.append(s[i])
            # 같은 값이 있다면
            else:
                key = q.popleft()
                q.append(s[i])
                answer[key] = len(q)

        max_length = len(q)

        if len(answer) != 0 and max_length < max(answer.values()):
            max_length = max(answer.values())

        return max_length


