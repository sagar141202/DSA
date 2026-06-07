# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a nested list, which can also have its own child pointer. Your task is to flatten this multilevel doubly linked list into a singly linked list, where each node only has a next pointer. The nodes should be ordered in a way that the nodes from the original list come first, followed by the nodes from the nested lists. For example, if we have a list 1 -> 2 -> 3 -> 4, where 2 has a child 5 -> 6, and 6 has a child 7 -> 8, the flattened list should be 1 -> 2 -> 5 -> 6 -> 7 -> 8 -> 3 -> 4.

## Approach
The approach to solve this problem is to use a recursive function that traverses the list and its child pointers, appending the nodes from the child lists to the main list. We will use a recursive helper function to handle the nested lists.

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
                // Update the pointers of the current node
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
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Input: 1 -> 2 -> 3 -> 4, where 2 has a child 5 -> 6
Output: 1 -> 2 -> 5 -> 6 -> 3 -> 4
```

## Key Takeaways
- The key to solving this problem is to use a recursive approach to handle the nested lists.
- We need to update the pointers of the nodes carefully to ensure that the lists are connected correctly.
- The time complexity is O(N), where N is the total number of nodes in the list and its child lists.