# # Fibonacci Sequence 
# n=int(input("Enter the number of terms: "))
# a, b = 0, 1
# print("Fibonacci Sequence:")
# for i in range(n):
#     print(a)
#     a, b = b, a + b

# Tribonacci Sequence
# n = int(input("Enter the number of terms: "))
# a, b, c = 0, 1, 1
# print("Tribonacci Sequence:")
# for i in range(n):
#     print(a)
#     a, b, c = b, c, a + b + c

# # List
# #  list indexing
# list1 = [1, 2, 3, 4, 5]
# print(list1[0]) 

#  List slicing
# syntex: list[start index:stop index]
# print(list1[1:4])

#  List operations
#    1)concatenation operation(+)
# a=[1, 2, 3]
# b=[4, 5, 6]
# c=a+b
# print(c)
# #      2)repetition operation(*)
# d = [1, 2, 3]
# print(d * 3)
# #     3)membership operation(in,not in)
# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits)  
# print("grape" not in fruits)

# #     4)comparison operation
# list2 = [1, 2, 3, 4, 5]
# list3= [6, 7, 8]
# print(list2==list3)
# print(list2!=list3)
# print(list2<list3)
# print(list2>list3)


# example of list operations
# listA = [1, 2, 3, 4, 5]
# listB = [6, 7, 8, 9, 10]
# print("a list index of 3 is", listA[3])
# print(" a list slice of listB[2:5] is", listB[2:5])
# print("listA + listB is", listA + listB)
# print("listA * 2 is", listA * 2)
# print("3 in listA is", 3 in listA)
# print("11 not in listB is", 11 not in listB)
# print("listA == listB is", listA == listB)
# print("listA != listB is", listA != listB)
# print("listA < listB is", listA < listB)
# print("listA > listB is", listA > listB)

#  List methods
#  1)append() method - adds an element to the end of the list.
# list1 = [1, 2, 3]
# list1.append(4)
# print(list1)

# # 2)insert() method - adds an element at a specific index in the list.
# # syntex: list.insert(index, element)
# list1.insert(1, 10) 
# print(list1)

# # 3)extend() method - adds all elements of an iterable (like another list) to the end of the list.
# list2 = [5, 6, 7]   
# list1.extend(list2)
# print(list1)

# # 3)remove() method - removes the first occurrence of a specified element from the list.
# list1.remove(5)
# print(list1)

# # 4)pop() method - removes and returns the element at a specified index (or the last element if no index is provided).
# popped_element = list1.pop(2)
# print("Popped element:", popped_element)
# print("List after popping:", list1)

# # 5)clear() method - removes all elements from the list, resulting in an empty list.
# list1.clear()
# print("List after clearing:", list1)

# # 6)index() method - returns the index of the first occurrence of a specified element in the list.
# list3 = [1, 2, 3, 4, 5] 
# index_of_3 = list3.index(3)
# print("Index of 3 in list3:", index_of_3)

# # 7)count() method - returns the number of occurrences of a specified element in the list.
# list4 = [1, 2, 2, 3, 4, 5]
# count_of_2 = list4.count(2) 
# print("Count of 2 in list4:", count_of_2)

# # 8)sort() method - sorts the elements of the list in ascending order (or in descending order if specified).
# list5 = [5, 2, 9, 1, 5]
# list5.sort()
# print("Sorted list5:", list5)
# list5.sort(reverse=True)
# print("Sorted list5 in descending order:", list5)

# # 9)reverse() method - reverses the order of the elements in the list.
# list6 = [1, 2, 3, 4, 5]
# list6.reverse()
# print("Reversed list6:", list6)

# # 10)copy() method - returns a shallow copy of the list.
# list7 = [1, 2, 3, 4, 5]
# list8 = list7.copy()
# print("List7:", list7)
# print("List8 (copy of list7):", list8)

#  map, filter, reduce

