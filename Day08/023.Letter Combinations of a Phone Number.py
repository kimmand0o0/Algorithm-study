#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = ['']

        # 숫자를 받지 못하면 빈 배열이 나간다.
        if not digits:
            return []

        # 숫자를 차례대로 가져온다
        for digit in digits:
            first_letter = phone[digit]
            bucket = []
            #가져온 숫자에 해당하는 문자
            for letter in first_letter:
                #기존 문자에 새로운 문자 추가하기
                for combination in answer:
                    #첨에 letter를 앞에 썼는 데 순서가 상관이 있음..
                    bucket.append(combination+letter)
            answer = bucket

        return answer