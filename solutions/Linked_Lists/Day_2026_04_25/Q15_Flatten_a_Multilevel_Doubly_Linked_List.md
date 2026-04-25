# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The task is to flatten this multilevel linked list into a single-level doubly linked list. The list should be flattened in a way that all nodes at a given level are before all nodes at the next level. The child pointers should be ignored after flattening. For example, given the following multilevel linked list:
```
      1---2---3---4---5---6
          |
          7---8---9---10
              |
              11---12
```
The flattened linked list should be:
```
1---2---7---8---11---12---9---10---3---4---5---6
```
The constraints are:
- The number of nodes in the linked list is between 1 and 10^5.
- The value of each node is between 1 and 10^5.

## Approach
We will use a recursive approach to flatten the linked list. We will traverse the linked list and whenever we encounter a node with a child, we will recursively flatten the child list and then append it to the current node.

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
                // find the tail of the child list
                Node* tail = curr->child;
                while (tail->next) {
                    tail = tail->next;
                }
                // append the child list to the current node
                tail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = tail;
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
1---2---7---8---11---12---9---10---3---4---5---6
```

## Key Takeaways
- The key to solving this problem is to understand how to recursively flatten the child lists and append them to the current node.
- We need to keep track of the tail of the child list to append it to the current node.
- We need to update the prev and next pointers of the nodes in the child list and the current node after appending the child list.