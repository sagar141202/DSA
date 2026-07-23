# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has two pointers: `next` and `child`. The `next` pointer points to the next node in the list, and the `child` pointer points to the first node of a child list. The task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The resulting list should have all the nodes from the original list, in the correct order, with no child pointers. For example, given the following multilevel doubly linked list: 
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
The constraints are: the number of nodes in the list is between 1 and 1000, and the number of levels in the list is between 1 and 1000.

## Approach
To solve this problem, we can use a recursive approach, where we recursively flatten each child list and then append it to the current node's next pointer. We also need to update the child pointer of each node to null after flattening its child list.

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
                // Find the last node of the child list
                Node* tail = curr->child;
                while (tail->next) {
                    tail = tail->next;
                }
                // Connect the last node of the child list to the next node of the current node
                tail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = tail;
                }
                // Connect the current node to the first node of the child list
                curr->next = curr->child;
                curr->child->prev = curr;
                // Set the child pointer to null
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
- We use a recursive approach to flatten each child list and then append it to the current node's next pointer.
- We update the child pointer of each node to null after flattening its child list.
- The time complexity is O(N), where N is the total number of nodes in the list, and the space complexity is O(N) due to the recursive call stack.