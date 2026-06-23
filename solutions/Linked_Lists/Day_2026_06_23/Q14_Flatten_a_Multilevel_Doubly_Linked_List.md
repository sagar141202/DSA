# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of another linked list, which is also a multilevel doubly linked list. The task is to flatten this multilevel linked list into a single-level doubly linked list. The constraints are that the input linked list is non-empty and the node values are unique. For example, given the following multilevel linked list:
```
 1---2---3---4---5---6
          |
          7---8---9
              |
              10---11
```
The output should be:
```
1---2---3---7---8---10---11---4---5---6
```

## Approach
We will use a recursive approach to flatten the linked list. We will traverse the linked list and whenever we encounter a node with a child, we will recursively flatten the child linked list and then merge it with the current linked list.

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
                while (childTail->next) {
                    childTail = childTail->next;
                }
                // Merge the child list with the current list
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
 1---2---3---4---5---6
          |
          7---8---9
              |
              10---11
Output: 
1---2---3---7---8---10---11---4---5---6
```

## Key Takeaways
- Recursion can be used to solve problems with nested structures.
- Merging two linked lists can be done by updating the next and previous pointers of the nodes.
- It's essential to handle edge cases, such as an empty linked list or a node with no child.