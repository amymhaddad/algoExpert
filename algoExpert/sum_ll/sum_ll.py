"""
https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
"""


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    linked1_ints = get_digits(linkedListOne)
    linked2_ints = get_digits(linkedListTwo)
    sum_of_lists = str(linked1_ints + linked2_ints)[::-1]

    return store_digits(sum_of_lists)


def store_digits(num):

    new_list = LinkedList(int(num[-1]))
    num = num[:-1]

    while num:
        last_digit = int(num[-1])
        new_list.value, new_list.next = last_digit, LinkedList(
            new_list.value, new_list.next
        )
        num = num[:-1]

    return new_list


def get_digits(linked_list):

    total_numbers = []

    while linked_list is not None:
        number = linked_list.value
        total_numbers.append(str(number))
        linked_list = linked_list.next
    return int("".join(total_numbers[::-1]))
