# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a nested list. Your task is to flatten this multilevel list into a single-level doubly linked list. The nodes in the flattened list should be in the order of their appearance in the original list. For example, given the following multilevel list:
```
 1---2---3---4---5---6
          |
          7---8---9
            |
            10---11
```
The flattened list should be:
```
1---2---3---7---8---10---11---4---5---6
```
The constraints are that the input list is a valid multilevel doubly linked list, and the output should be a single-level doubly linked list.

## Approach
We will use a recursive approach to solve this problem, where we traverse the list and when we encounter a node with a child, we recursively flatten the child list and then append it to the current list.

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
                
                // Append the child list to the current list
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
- Use a recursive approach to solve this problem.
- When encountering a node with a child, recursively flatten the child list and then append it to the current list.
- Keep track of the tail of the child list to append it to the current list.