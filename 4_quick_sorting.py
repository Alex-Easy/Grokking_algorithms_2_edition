# sum of numbers in array

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(sum([1, 2, 3, 4]))

# Exercises

"""
4.1 Write code for the sum function (see above).
Solution:
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

4.2 Write a recursive function to count the items in a list.
Solution:
def count(list):
    if list == []:
        return 0
    return list[0] + count(list[1:])

4.3 Write a recursive function to find the largest number in a list.
Solution:
def find_max_recursive(arr):
    if len(arr) == 1:
        return arr[0]

    max_of_rest = find_max_recursive(arr[1:])
    return arr[0] if arr[0] > max_of_rest else max_of_rest

4.4 Remember the binary search from Chapter 1? It, too, belongs to the class of divide-and-conquer algorithms. Can you
define the base and recursive cases for binary search?
Solution:
The base case for binary search is an array containing just one element. If the element you are looking for matches
the array element - you have found it! Otherwise, there is no element in the array.
In the recursive case for binary search, the array is divided in half, one half is discarded, and a binary search is
performed  for the other half.

4.5 Output the value of each element of the array.
Solution: O(n).
4.6 Doubling the value of each element of the array.
Solution: O(n).
4.7 Doubling the value of only the first element of the array.
Solution: O(1).
4.8 Create a multiplication table for all elements of the array. For example, if an array consists of elements [2, 3, 7, 8, 10], first each element is multiplied by 2, then each element is multiplied by 3, then by 7, etc.
Solution: O(n2).
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
