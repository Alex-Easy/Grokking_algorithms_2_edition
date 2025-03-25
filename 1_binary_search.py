def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


# Exercises

'''
1.1 You have a sorted list of 128 names and you are searching the list for a value using the binary search method. 
What is the maximum number of checks this may require?
Solution:
The maximum number of checks = log2(n)
n is the number of items in the list
log2(128) = 7
Answer: 7 checks

1.2 Suppose the size of the list is doubled. How will the maximum number of checks change?
new list size = 256
log2(256) = 8
Answer: the maximum number of checks will increase to 8. 

Give the “Big O” runtime for each of the following scenarios.

1.3 Got a last name, need to find the number in the phone book.
Answer: In most real-world scenarios, the phonebooks are sorted, so a binary search with a run time of 
O(log n)

1.4 You know the number, you need to find the last name in the phone book. (Hint: you will have to search the whole book!)
Answer: The phone book is usually sorted by last name, not by phone number. This means that the phone number is not directly 
related to the order of entries in the book. To find a last name by number, you have to check every entry in the phone book 
because the numbers are not in order.
This requires an O(n) linear search

1.5 It is necessary to read each entry in the phone book to get the phone numbers of all people.
Answer: The number of operations depends directly on the number of entries 
n in the phone book. Thus, the execution time is O(n).

1.6 You need to read the phone numbers of all the people whose last names start with the letter “A”. (Trick question! It 
involves concepts that are discussed in more detail in Chapter 4. Read the answer - it will probably surprise you!)
Answer: O(n)

'''
