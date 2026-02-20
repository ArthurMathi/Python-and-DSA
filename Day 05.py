# leetcode Problem no: 217 contains duplicate
# class Solution(object):
#     def containsDuplicate(self, nums):
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
# nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
# solution = Solution()
# print(solution.containsDuplicate(nums))

# leetcode problem no: 342 power of four
# class Solution(object):
#     def isPowerOfFour(self, num):
#         if num <= 0:
#             return False
#         while num % 4 == 0:
#             num //= 4
#         return num == 1
# num = int(input("Enter a number: "))
# solution = Solution()
# print(solution.isPowerOfFour(num))    

# # leetcode problem no: 231 power of two
# class Solution(object):
#      def isPowerOfTwo(self, num):
#          if num <= 0:
#              return False
#          return (num & (num - 1)) == 0
# num = int(input("Enter a number: "))
# solution = Solution()
# print(solution.isPowerOfTwo(num))

# leetcode problem no: 121 best time to buy and sell stock
# class Solution(object):
#     def maxProfit(self, prices):
#         min_price = float('inf')
#         max_profit = 0
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             elif price - min_price > max_profit:
#                 max_profit = price - min_price
#         return max_profit

# OPPS concept in python

# def func(a,b):
#     return a+b
# result = func(5, 10)
# print(result)

# class myClass:
#     def details(self,name,marks):
#         if marks >= 40:
#             result = "pass"
#             print(result)
#         else:
#             result = "fail"
# s1=myClass()
# s1.details("Rvs", 45)

# class ClassName:
#     def method_name(self):
# #         print("message")

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def show_result(self):
#         if self.marks >= 40:
#             result = "pass"
#         else:
#             result = "fail"
#             print("\n student name:", self.name)
#             print("marks:", self.marks)
#             print("result:", result)
                  
# name=input("Enter student name: ")
# marks=int(input("Enter student marks: "))
# s1=Student(name, marks)
# s1.show_result()              


            