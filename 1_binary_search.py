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


# ����������
# Exercises

'''
RU
1.1 ������� ��������������� ������ �� 128 ����, � �� ����� � ��� �������� ������� ��������� ������. 
����� ������������ ���������� �������� ��� ����� ����� �������������?
�������:
������������ ���������� ��������= log2(n)
n - ���������� ��������� � ������
log2(128) = 7
�����: 7 ��������

EN
1.1 You have a sorted list of 128 names and you are searching the list for a value using the binary search method. 
What is the maximum number of checks this may require?
Solution:
The maximum number of checks = log2(n)
n is the number of items in the list
log2(128) = 7
Answer: 7 checks

RU
1.2 �����������, ������ ������ ���������� �����. ��� ��������� ������������ ���������� ��������?
����� ������ ������ = 256
log2(256) = 8
�����: ������������ ���������� �������� ���������� �� 8

EN
1.2 Suppose the size of the list is doubled. How will the maximum number of checks change?
new list size = 256
log2(256) = 8
Answer: the maximum number of checks will increase to 8.

'''