#https://leetcode.com/problems/group-anagrams/
#
# strings 배열이 주어지면 철자 바꾸기를strs 함께 그룹화하십시오 . 어떤 순서로든 답변을 반환할 수 있습니다 .
#
# 아나그램은 일반적 으로 모든 원래 문자를 정확히 한 번 사용하여 다른 단어나 구문의 문자를 재배열하여 형성된 단어나 구문입니다.
#
#
#
# 예시 1:
#
# 입력: strs = ["eat","tea","tan","ate","nat","bat"]
#  출력: [["bat"],["nat","tan"],["eat","ate","tea"]]
# 예 2:
#
# 입력: strs = [""]
#  출력: [[""]]
# 예시 3:
#
# 입력: strs = ["a"]
#  출력: [["a"]]
#
#
# 제약:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i]영문 소문자로 구성됩니다.


# str을 알파벳 순으로 정렬했을 때를 키값으로 묶어주는 객체를 생성한 후 값만 return

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 객체 생성
        str_dict = {}

        for string in strs:
            # 알파벳 순으로 sort
            sorted_string = str(sorted(string))

            # sort 한 값이 있다면 값 배열에 추가. 아니면 생성
            if sorted_string in str_dict:
                str_dict[sorted_string].append(string)
            else:
                str_dict[sorted_string] = [string]

        # key는 버리고 values를 배열로 return
        return str_dict.values()