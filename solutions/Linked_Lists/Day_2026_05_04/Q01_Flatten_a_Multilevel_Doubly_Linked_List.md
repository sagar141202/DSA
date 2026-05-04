# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a new linked list, which is also a multilevel doubly linked list. Your task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The nodes should be connected in the order they appear in the original list, and the child pointers should be ignored. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5 -> 6, and node 3 has a child node 7 -> 8 -> 9, the output list should be 1 -> 2 -> 3 -> 7 -> 8 -> 9 -> 4 -> 5 -> 6.

## Approach
We can solve this problem by using a recursive approach, where we traverse the list and whenever we encounter a node with a child, we recursively flatten the child list and append it to the current node. We then remove the child pointer and continue with the rest of the list.

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
                while (childTail->next) childTail = childTail->next;
                
                // Connect the child list to the rest of the list
                childTail->next = curr->next;
                if (curr->next) curr->next->prev = childTail;
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
1 -> 2 -> 3 -> 4 -> 5 -> 6
Node 3 has a child node 7 -> 8 -> 9

Output: 
1 -> 2 -> 3 -> 7 -> 8 -> 9 -> 4 -> 5 -> 6
```

## Key Takeaways
- We use a recursive approach to flatten the multilevel doubly linked list.
- We keep track of the current node and its child node to connect them properly.
- We remove the child pointer after connecting the child list to the rest of the list.