# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The child pointer of a node is a pointer to the head of another linked list, and we need to flatten all these linked lists into one. The constraints are that we cannot use any extra space and we need to do it in-place.

## Approach
We will use a recursive approach to solve this problem, where we will recursively flatten the child linked lists and then merge them into the main linked list. We will keep track of the next node in the main linked list and the last node in the flattened child linked list.

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
                // Find the last node in the child linked list
                Node* last = curr->child;
                while (last->next) {
                    last = last->next;
                }
                
                // Merge the child linked list into the main linked list
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
1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
    |
    7 <-> 8 <-> 9 <-> 10

Output: 
1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 9 <-> 10 <-> 4 <-> 5 <-> 6

Input: 
1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6

Output: 
1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
```

## Key Takeaways
- We should always consider the base cases when solving recursive problems.
- We should be careful when dealing with linked lists, as they can be easily broken if not handled properly.
- The child pointer in the multilevel doubly linked list can point to the head of another linked list, which needs to be flattened and merged into the main linked list.