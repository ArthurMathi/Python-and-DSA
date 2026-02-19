# # leetcode Problem no:242 valid anagram
# class Solution:
#     def isAnagram(self,s,t):
#         if len(s) != len(t):
#             return False
#         return sorted(s) == sorted(t)

# s=input("Enter the first string: ")
# t=input("Enter the second string: ")
# solution = Solution()
# if solution.isAnagram(s,t):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

# # leetcode problem no: 70 climbing stairs
# class solution(object):
#     def climbStairs(self,n):
#         if n <= 0:
#             return 0
#         elif n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         prev1, prev2 = 1, 2
#         for i in range(3, n + 1):
#             current = prev1 + prev2
#             prev1, prev2 = prev2, current
#         return prev2
# n = int(input("Enter the number of stairs: "))
# solution = solution()
# print("Number of ways to climb the stairs:", solution.climbStairs(n))

# leetcode problem no :412 fizz buzz
# class Solution(object):
#     def fizzBuzz(self,n):
#         result = []
#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))
#         return result
# n = int(input("Enter the number: "))
# sol = Solution()
# print(sol.fizzBuzz(n))

# leetcode problem no: 169 majority element
# class Solution(object):
#     def majorityElement(self, nums):
#         count = {}
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#             if count[num] > len(nums) // 2:
#                 return num
# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
# solution = Solution()
# print("Majority element:", solution.majorityElement(nums))            

# leetcode problem no: 1822 sign of the product of an array
# class Solution(object):
#     def arraySign(self, nums):
#         product_sign = 1
#         for num in nums:
#             if num == 0:
#                 return 0
#             elif num < 0:
#                 product_sign *= -1
#         return product_sign
# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
# solution = Solution()
# print("Sign of the product of the array:", solution.arraySign(nums))

# leetcode problem no: 58 length of last word
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         words = s.strip().split()
#         if not words:
#             return 0
#         return len(words[-1])
# s = input("Enter a string: ")
# solution = Solution()
# print("Length of the last word:", solution.lengthOfLastWord(s))

# leetcode problem no: 349 intersection of two arrays
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         set1 = set(nums1)
#         set2 = set(nums2)
#         return list(set1.intersection(set2))
# nums1 = [int(x) for x in input("Enter the first array : ")]
# nums2 = [int(x) for x in input("Enter the second array : ")]
# solution = Solution()
# print("Intersection of the two arrays:", solution.intersection(nums1, nums2))

# union of two arrays
# class Solution(object):
#     def union(self, nums1, nums2):
#         set1 = set(nums1)
#         set2 = set(nums2)
#         return list(set1.union(set2))
# nums1 = [int(x) for x in input("Enter the first array : ")]
# nums2 = [int(x) for x in input("Enter the second array : ")]
# solution = Solution()
# print("Union of the two arrays:", solution.union(nums1, nums2))

# leetcode problem no: 14 longest common prefix
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""
#         prefix = strs[0]
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#         return prefix
# strs = input("Enter the strings (space-separated): ").split()
# solution = Solution()
# print("Longest common prefix:", solution.longestCommonPrefix(strs))

# # leetcode problem no: 344 reverse string
# class Solution(object):
#     def reverseString(self, s):
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
# s = list(input("Enter a string: "))
# solution = Solution()
# solution.reverseString(s)
# print("Reversed string:", ''.join(s))

# leetcode problem no: 136 single number
# class Solution(object):
#     def singleNumber(self, nums):
#         result = 0
#         for num in nums:
#             result ^= num
#         return result
# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
# solution = Solution()
# print("Single number:", solution.singleNumber(nums))

# leetcode problem no: 258 add digits
# class Solution(object):
#     def addDigits(self, num):
#         if num == 0:
#             return 0
#         elif num % 9 == 0:
#             return 9
#         else:
#             return num % 9
# num = int(input("Enter a number: "))
# solution = Solution()
# print("Result after adding digits:", solution.addDigits(num))

# # leetcode problem no: 283 move zeroes
# class Solution(object):
#     def moveZeroes(self, nums):
#         non_zero_index = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[non_zero_index] = nums[i]
#                 non_zero_index += 1
#         for i in range(non_zero_index, len(nums)):
#             nums[i] = 0
# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
# solution = Solution()
# solution.moveZeroes(nums)
# print("Array after moving zeroes:", nums) 

# # leetcode problem no: 100 same tree
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution(object):
#     def isSameTree(self, p, q):
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.val != q.val:
#             return False
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# p = TreeNode(1, TreeNode(2), TreeNode(3))
# q = TreeNode(1, TreeNode(2), TreeNode(3))
# solution = Solution()
# print("Are the trees the same?", solution.isSameTree(p, q))
    
    