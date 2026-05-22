# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The child pointer points to the head of another doubly linked list, which can also have child pointers. The task is to flatten the multilevel doubly linked list into a single-level doubly linked list. The list should be flattened in a way that all nodes at depth i come before all nodes at depth i + 1. The nodes at each depth should be ordered from left to right. For example, given the following multilevel doubly linked list:
```
 1---2---3---4---5---6---7
        |
        8---9---10
            |
            11---12
```
The flattened list should be:
```
1---2---8---9---11---12---3---4---5---6---7
```
The constraints are:
- The number of nodes in the list is between 1 and 10^5.
- The value of each node is between 1 and 10^5.

## Approach
To solve this problem, we can use a recursive approach to flatten the multilevel doubly linked list. We will recursively traverse the list and its child pointers, appending the nodes to the end of the current list. This will ensure that all nodes at depth i come before all nodes at depth i + 1.

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
        if (!head) return head;
        Node* curr = head;
        while (curr) {
            if (curr->child) {
                // Find the tail of the child list
                Node* childTail = curr->child;
                while (childTail->next) {
                    childTail = childTail->next;
                }
                // Append the child list to the current list
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
 1---2---3---4---5---6---7
        |
        8---9---10
            |
            11---12
Output: 
1---2---8---9---11---12---3---4---5---6---7
```

## Key Takeaways
- Use a recursive approach to traverse the multilevel doubly linked list.
- Append the child list to the current list by updating the next and prev pointers of the nodes.
- Set the child pointer of the current node to nullptr after appending the child list.