# Challenge Summary
<!-- Description of the challenge -->
### Feature Tasks Code Challenge Class 06
**Write the following methods for the Linked List class:**

- append
    - arguments: new value
    - adds a new node with the given value to the end of the list
- insert before
    - arguments: value, new value
    - adds a new node with the given new value immediately before the first node that has the value specified
- insert after
    - arguments: value, new value
    - adds a new node with the given new value immediately after the first node that has the value specified


## Whiteboard Process
<!-- Embedded whiteboard image -->

![whiteboard](./Linked-Lists-insertions.jpg)

## Code
[Linked List code](./linked_list.py)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Traversed through the list and looked for the value specified, if no value, then insert new value at head, otherwise insert either before or after or at end depending on the method

> append - Time = O(n), Space = O(1)
insert_before - Time = O(n), Space = O(1)
insert_after - Time = O(n), Space = O(1)



## Solution
<!-- Show how to run your code, and examples of it in action -->

>Linked_List.append(5)--> adds new node at the end

>Linked_List.insert_before(3,5)--> adds new node with a value of 5 before the node with a value of 3

>Linked_List.insert_after(3,5)--> adds new node with a value of 5 after the node with a value of 3


## Unit Tests
- Can successfully add a node to the end of the linked list
- Can successfully add multiple nodes to the end of a linked list
- Can successfully insert a node before a - node located i the middle of a linked list
- Can successfully insert a node before the first node of a linked list
- Can successfully insert after a node in the middle of the linked list
- Can successfully insert a node after the last node of the linked list





# Challenge Summary
<!-- Description of the challenge -->
### Feature Tasks Code Challenge Class 07
**Write the following methods for the Linked List class:**

- kth from end
    - arguments: new value
    - adds a new node with the given value to the end of the list



## Whiteboard Process
<!-- Embedded whiteboard image -->

![whiteboard](./Linked-list-KTH.jpg)

## Code
[Linked List code](./linked_list.py)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
the solution I am going to try is to check if the length -k and return the value at the point where


## Solution
<!-- Show how to run your code, and examples of it in action -->
![whiteboard](./kth-solution.png)

>Linked_List.kthFromEnd(k) -> takes in k and returns the value at k


## Unit Tests

1. Where k is greater than the length of the linked list
2. Where k and the length of the list are the same
3. Where k is not a positive integer
4. Where the linked list is of a size 1
5. “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
