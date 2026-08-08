# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a new linked list, which can also have child pointers. The task is to flatten this multilevel linked list into a single-level doubly linked list. The constraints are that the input linked list is non-empty, and all node values are unique. For example, given the following multilevel linked list: 
1---2---3---4---5---6
where 3 has a child 7---8---9 and 8 has a child 10---11, the flattened linked list should be: 1---2---3---7---8---10---11---9---4---5---6.

## Approach
To solve this problem, we will use a recursive approach to traverse the multilevel linked list. We will iterate over each node in the list, and if a node has a child, we will recursively flatten the child list and connect it to the current node. The key idea is to keep track of the tail of the flattened child list and connect it to the next node in the original list.

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
                Node* tail = curr->child;
                while (tail->next) {
                    tail = tail->next;
                }
                // Connect the tail of the child list to the next node in the original list
                tail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = tail;
                }
                // Connect the child list to the current node
                curr->next = curr->child;
                curr->child->prev = curr;
                // Remove the child pointer
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
Input: 1---2---3---4---5---6
       where 3 has a child 7---8---9 and 8 has a child 10---11
Output: 1---2---3---7---8---10---11---9---4---5---6
```

## Key Takeaways
- The problem can be solved using a recursive approach to traverse the multilevel linked list.
- We need to keep track of the tail of the flattened child list to connect it to the next node in the original list.
- The time complexity is O(N), where N is the total number of nodes in the multilevel linked list.