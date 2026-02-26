# import heapq

# pq=[]

# heapq.heappush(pq,3)
# heapq.heappush(pq,1)
# heapq.heappush(pq,2)

# print("priority Queue",pq)

# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))

# def missingNumber(self,nums):
#     num=[0,1,2,3,5]
#     n=len(nums)
#     total_sum=n*(n+1)//2
#     array_sum=sum(nums)
#     return total_sum-array_sum


# def remove_dublicate(self,head):
#     current = head

#     while current and current.next:
#         if current.val == current.next.val:
#                 current.next = current.next.next
#         else:
#                 current = current.next
#     return head

class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reversed_words = []

        for word in words:
            reversed_words.append(word[::-1])

        return " ".join(reversed_words)