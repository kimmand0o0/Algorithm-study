#https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # jewel 문자를 키로 갖는 해시테이블을 만든다
        jewel_table = {jewel : 0 for jewel in jewels}

        # stones를 순회하며 jewel과 같으면 해당 테이블 value에 +1
        for stone in stones:
            if stone in jewel_table:
                jewel_table[stone] += 1

        return sum(jewel_table.values())