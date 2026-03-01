# # class Solution:
# #     def twoSum(self, nums, target):
# #         for i in range(0, len(nums)):
# #             for j in range(i + 1, len(nums)):
# #                 print(i, j)
# #                 if nums[i] + nums[j] == target:
# #                     return i, j


# # s = Solution()
# # print(s.twoSum([3, 2, 4], 6))


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         n = len(nums)
#         dic = {}
#         for i in range(n):
#             required = target - nums[i]
#             if required in dic:
#                 return [dic[required],i]
#             else:
#                 dic[nums[i]] = dic.get(nums[i], 0) + i
#                 print (dic)
#         return []


class Solution:
    def innerLoop(self, i, nums, target):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j, True
        return None, None, False

    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            ii, jj, isreturn = self.innerLoop(i, nums,target)
            if isreturn:
                return ii, jj


s = Solution()
print(s.twoSum([3, 2, 5, 6, 7, 4], 6))
