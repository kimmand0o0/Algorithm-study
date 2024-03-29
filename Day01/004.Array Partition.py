#https://leetcode.com/problems/array-partition/
#
#nums정수 의 정수 배열이 주어지면 모든 정수의 합이 최대가 되도록 2n이러한 정수를 n쌍 으로 그룹화합니다 . 최대화된 합계를 반환합니다 .(a1, b1), (a2, b2), ..., (an, bn)min(ai, bi)i
#
# 예시 1:
# 입력: nums = [1,4,3,2]
#  출력: 4
#  설명: 가능한 모든 쌍(요소 순서 무시)은 다음과 같습니다.
# 1. (1, 4), (2, 3) -> 최소(1, 4) + 최소(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> 최소(1, 3) + 최소(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> 최소(1, 2) + 최소(3, 4) = 1 + 3 = 4
# 따라서 가능한 최대 합은 4입니다.
#
# 예 2:
# 입력: nums = [6,2,6,5,1,2]
#  출력: 9
#  설명: 최적의 쌍은 (2, 1), (2, 5), (6, 6)입니다. 최소(2, 1) + 최소(2, 5) + 최소(6, 6) = 1 + 2 + 6 = 9.