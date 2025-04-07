def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([2, 7, 25, 0, 3, 45, -1, 20, 73, 4]))

# Exercises

"""
2.2 Let's say you are writing an application to take orders from restaurant customers. The application must store a list of orders. Waiters add orders to the list, and cooks read orders from the list and fulfill them. Orders form a queue: waiters add orders to the end of the queue, and the cook takes the first order from the queue and starts cooking. Which data structure would you use to implement this queue: an array or a linked list? (Hint: linked lists are good for insertion/deletion, and arrays are good for random access to items. Which of these would be needed in this case?)
Solution:
The linked list is more efficient for FIFO queuing because the basic operations (enqueue and dequeue) are performed in constant time without the overhead of moving data.

2.3 Let's do a thought experiment. Suppose Facebook stores a list of usernames. When someone tries to log in to Facebook, the system tries to find the username. If the name is in the list of registered user names, then login is allowed. Users come to Facebook quite often, so the list of usernames will be searched frequently. We will assume that Facebook uses a binary search to search the list. Binary search needs random access - the algorithm must instantly access the middle element of the current part of the list. Knowing this fact, how would you implement a list of users: as an array or as a linked list?
Solution:
For frequent searches of a sorted list (as in the case of Facebook), an array is preferred because:
Supports the fast random access (O(1)) required for binary search.
Is more efficient at sorting and maintaining sorted state.
Runs faster due to cache friendliness.

2.4 Users also create new Facebook accounts quite often. Suppose you decide to use an array to store a list of users. What are the disadvantages of using an array to perform insertion? Suppose you use binary search to find credentials. What happens when you add new users to the array?
Solution:
Inserting into an array is slow. Also, if you use binary search to find user names, the array must be sorted.

2.5
In reality, Facebook uses neither an array nor a linked list to store information about users. Consider a hybrid data structure: an array of linked lists. There is an array of 26 elements. Each element contains a reference to a linked list. For example, the first element of the array points to a linked list of all usernames beginning with the letter A. The second element points to a linked list of all usernames beginning with the letter B, and so on.
Suppose a user named Adit B registers on Facebook and you want to add him to a list. You access element 1 of the array, find the linked list of element 1 and add Adit B to the end of the list. Now suppose you want to register the user Zakhir H. You access element 26 which contains the linked list of all names starting with Z and check whether Zakhir H is present in this list.
Now compare this hybrid data structure with arrays and linked lists. Will it be faster or slower than each original structure when searching and inserting? You don't need to cite O-big, just choose one of the two: faster or slower.
Solution:
Hybrid structure compromise:
? Better than a pure list when searching (spacing is faster).
? Better than an array when inserting (no need to move elements).
? Worse than array when searching (binary search is still faster).
? Slightly worse than a pure list when inserting (because of the sublist selection).

In practice, this structure (similar to a hash table with chains) is often used in simple databases or dictionaries where balancing between search and insertion is important.
"""
