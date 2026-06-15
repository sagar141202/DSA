# Flatten a Multilevel Doubly Linked List

## Problem Statement
We are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The child pointer points to the head of a new linked list, which is also a multilevel doubly linked list. The task is to flatten this multilevel doubly linked list into a single-level doubly linked list, where all nodes are at the same level. The nodes in the resulting linked list should be in the order of their appearance in the original linked list. For example, if we have a node with value 1, and its child is a node with value 2, and the next node of the node with value 1 is a node with value 3, then the resulting linked list should be 1 -> 2 -> 3.

## Approach
The algorithm involves recursively traversing the linked list, and whenever we encounter a node with a child, we append the child's linked list to the current node's next pointer. We keep track of the last node in the current linked list to update its next pointer correctly. The recursion unwinds by updating the next and prev pointers of the nodes.

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
                // Update the next pointer of the last node in the child linked list
                last->next = curr->next;
                // Update the prev pointer of the next node
                if (curr->next) {
                    curr->next->prev = last;
                }
                // Update the next and child pointers of the current node
                curr->next = curr->child;
                curr->child->prev = curr;
                curr->child = NULL;
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
1 -> 2 -> 3 -> 4 -> 5 -> 6, where 3 has a child 7 -> 8 -> 9, and 8 has a child 10 -> 11
Output: 1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6
```

## Key Takeaways
- Recursion is not necessary for this problem; we can solve it iteratively.
- We need to keep track of the last node in the current linked list to update its next pointer correctly.
- The time complexity is O(N), where N is the total number of nodes in the multilevel linked list.