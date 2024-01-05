#https://leetcode.com/problems/3sum/
#
#정수 배열 nums가 주어지면 , , 및 , 및 와 [nums[i], nums[j], nums[k]]같은 모든 삼중항을 반환합니다 .i != ji != kj != knums[i] + nums[j] + nums[k] == 0
#
# 솔루션 세트에는 중복된 삼중항이 포함되어서는 안 됩니다.
#
#Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# 별개의 삼중항은 [-1,0,1]과 [-1,-1,2]입니다.
# 출력 순서와 세 쌍의 순서는 중요하지 않습니다.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105