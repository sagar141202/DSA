# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The child pointer points to the head of another doubly linked list. You need to flatten this multilevel doubly linked list into a single-level doubly linked list. The nodes in the flattened list should be in the order of their appearance in the original list, and the child pointers should be ignored. For example, given the following multilevel doubly linked list:
```
 1---2---3---4---5---6
          |
          7---8---9---10
                  |
                  11---12
```
The flattened list should be:
```
1---2---3---7---8---11---12---9---10---4---5---6
```
The constraints are:
- The number of nodes in the list is between 1 and 1000.
- The value of each node is between 1 and 1000.

## Approach
To solve this problem, we can use a recursive approach to flatten the list. We start at the head of the list and iterate through each node. If a node has a child, we recursively flatten the child list and insert it into the main list.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};

class Solution {
public:
    Node* flatten(Node* head) {
        Node* curr = head;
        while (curr) {
            if (curr->child) {
                // Find the tail of the child list
                Node* childTail = curr->child;
                while (childTail->next) {
                    childTail = childTail->next;
                }
                // Insert the child list into the main list
                childTail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = childTail;
                }
                curr->next = curr->child;
                curr->child->prev = curr;
                curr->child = nullptr;
            }
            curr = curr->next;
        }
        return head;
    }
};
```

## Test Cases
```
Input: 
 1---2---3---4---5---6
          |
          7---8---9---10
                  |
                  11---12
Output: 
1---2---3---7---8---11---12---9---10---4---5---6
```

## Key Takeaways
- Recursion can be used to solve problems with nested structures.
- Iterating through a linked list and inserting nodes at specific positions can be complex, but using pointers can simplify the process.
- Understanding the constraints of the problem and the structure of the data is crucial to solving linked list problems.