# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a new linked list, which is also a multilevel doubly linked list. Your task is to flatten this multilevel linked list into a single-level doubly linked list. The constraints are that the input linked list is non-empty, and the nodes have unique values. For example, given the following multilevel linked list: 
1---2---3---4---5---6
        |
        7---8---9
            |
            10
The output should be: 
1---2---3---7---8---10---4---5---6

## Approach
We can solve this problem by using a recursive approach to flatten the linked list. We start at the head of the list and iterate through each node. If a node has a child, we recursively flatten the child list and then append it to the current node.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* prev;
    Node* child;
};

class Solution {
public:
    Node* flatten(Node* head) {
        Node* curr = head;
        while (curr) {
            // If the current node has a child, we need to flatten the child list
            if (curr->child) {
                // Find the tail of the child list
                Node* childTail = curr->child;
                while (childTail->next) {
                    childTail = childTail->next;
                }
                // Connect the child list to the next node in the main list
                childTail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = childTail;
                }
                // Connect the current node to the child list
                curr->next = curr->child;
                curr->child->prev = curr;
                // Remove the child pointer
                curr->child = nullptr;
            }
            // Move to the next node
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
- Use a recursive approach to flatten the linked list.
- Keep track of the tail of the child list to connect it to the next node in the main list.
- Remove the child pointer after connecting the child list to the main list.