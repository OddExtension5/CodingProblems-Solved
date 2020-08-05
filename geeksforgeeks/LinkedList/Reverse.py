"""
Date: - 05-08-2020
Author: - SUSHIL SINGH
Problem : - Reverse a linked list
Input: 1 -> 2 -> 3 -> 4 -> NULL
Output: 4 -> 3 -> 2 -> 1 -> NULL

Time Complexity: O(n)
Space Complexity: O(1)
"""

# solution

# node class
class Node:
    # constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    # function to initialize head 
    def __init__(self):
        self.head = None
    
    # function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        
        while ( current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    # function to insert a new node at the beginning    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next

llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
