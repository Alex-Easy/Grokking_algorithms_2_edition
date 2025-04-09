# looking key in boxes using while loop

def look_for_key(main_box, empty=None):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_akey():
                print("found the key!")

# looking key in boxes using recursion

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key!")

# the base case and the recursive case in the function countdown

def countdown(i):
    print(i)
    if i <= 1:  # Base case
        return
    else:  # Recursive case
        countdown(i - 1)

countdown(3)

# Exercises

"""
3.1 Suppose there is a call stack of the following form:
______________
    GREET2
NAME: | MAGGIE
______________
    GREET
NAME: | MAGGIE

What can we say about the current state of the program based on this call stack?
Solution:
The program is in the process of executing two nested functions:
First, the GREET function was called (the bottom entry on the stack)
Then, from within GREET, the GREET2 function was called (the top entry)
Execution context:
At the time both functions were called, the NAME parameter with the value "MAGGIE" was passed
It could be either:
One "MAGGIE" object passed through the call chain
Two different objects with the same name
Current status:
The GREET2 function is now active (it is on top of the stack)
The GREET function is suspended and waiting to be completed

3.2 Suppose you have accidentally written a recursive function that infinitely calls itself. As you have already 
seen,  the computer allocates memory on the stack each time the function is called. What happens to the stack when 
the  recursion is infinitely executed?
Solution:
Infinite recursion will cause a Stack Overflow, which will cause the program to crash.

[Stack to overflow]
├─ Frame main()
│ └── Call infinite_recursion()
├─ Frame infinite_recursion() #1
├─ ...
├─ Frame infinite_recursion() #999
└─ 🚫 Stack space has run out → Crash

Specific implications:
Situation Result
Python: RecursionError: Maximum recursion depth exceeded
Java/C++: StackOverflowError
JavaScript: RangeError: Maximum call stack size exceeded
C: Emergency Termination (Segmentation Fault)

"""