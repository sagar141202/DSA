# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a new linked list, which can also have child pointers. The task is to flatten this multilevel linked list into a single-level doubly linked list, where all nodes are connected in the order they appear in the original list. The constraints are that the input list is non-empty and all nodes have unique values.

## Approach
The algorithm involves recursively traversing the linked list and appending the child list to the main list when a child pointer is encountered. We use a recursive function to flatten the child lists and then connect them to the main list.

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
                
                // Connect the child list to the main list
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
1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
        |
        7 <-> 8 <-> 9 <-> 10

Output: 
1 <-> 2 <-> 7 <-> 8 <-> 9 <-> 10 <-> 3 <-> 4 <-> 5 <-> 6
```

## Key Takeaways
- Recursively traverse the linked list to handle child pointers.
- Connect the child list to the main list by updating the next and previous pointers.
- Remove the child pointer after connecting the child list to the main list.