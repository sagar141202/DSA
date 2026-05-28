# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of another doubly linked list, which is a child list. The task is to flatten this multilevel linked list into a single-level doubly linked list. The nodes in the child list should be inserted after the node that has the child pointer. For example, given the following linked list:
```
 1---2---3---4---5---6---7---NULL
        |
        8---9---10---NULL
            |
            11---12---NULL
```
The flattened linked list should be:
```
1---2---8---9---11---12---10---3---4---5---6---7---NULL
```
Each node has a unique value, and the input linked list is non-empty.

## Approach
To solve this problem, we can use a recursive approach to flatten the linked list. We start by iterating through the linked list, and whenever we encounter a node with a child pointer, we recursively flatten the child list and insert it after the current node.

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
                // Find the last node in the child list
                Node* last = curr->child;
                while (last->next) {
                    last = last->next;
                }
                // Insert the child list after the current node
                last->next = curr->next;
                if (curr->next) {
                    curr->next->prev = last;
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
 1---2---3---4---5---6---7---NULL
        |
        8---9---10---NULL
            |
            11---12---NULL
Output: 
1---2---8---9---11---12---10---3---4---5---6---7---NULL
```

## Key Takeaways
- We use a recursive approach to flatten the linked list.
- We insert the child list after the current node by updating the next and prev pointers of the nodes.
- We use a while loop to find the last node in the child list.
- We update the child pointer of the current node to nullptr after inserting the child list.