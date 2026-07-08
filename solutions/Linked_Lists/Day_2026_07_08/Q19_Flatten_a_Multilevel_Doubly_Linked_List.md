# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a nested list. Your task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The nodes in the flattened list should be in the order of their appearance in the original list, with the nodes from the nested lists appearing after their parent nodes. For example, given the following multilevel doubly linked list:
```
 1---2---3---4---5---6
          |
          7---8---9
              |
              10
```
The flattened list should be:
```
1---2---3---7---8---10---4---5---6
```
The constraints are that the input list is non-empty and the nodes do not have any cycles.

## Approach
We will use a recursive approach to flatten the list, iterating through each node and appending the child list when encountered. We will keep track of the previous node to correctly set the next and previous pointers.

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
                
                // Connect the child list to the next node
                childTail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = childTail;
                }
                
                // Connect the current node to the child list
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
          7---8---9
              |
              10
Output: 
1---2---3---7---8---10---4---5---6
```

## Key Takeaways
- Use a recursive approach to handle nested lists of arbitrary depth.
- Keep track of the previous node to correctly set the next and previous pointers.
- Update the child pointer to nullptr after appending the child list to avoid infinite loops.