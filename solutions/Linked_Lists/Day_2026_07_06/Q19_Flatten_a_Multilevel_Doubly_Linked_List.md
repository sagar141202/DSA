# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a new linked list. Your task is to flatten this multilevel linked list into a single-level doubly linked list. The constraints are that the input list is non-empty, and the nodes are non-null. For example, given a list with the following structure:
```
 1---2---3---4---5---6---7
        |
        8---9---10
            |
            11---12
```
The output should be:
```
1---2---3---8---9---11---12---4---5---6---7
```

## Approach
The approach to solve this problem is to perform a depth-first traversal of the linked list, and whenever we encounter a node with a child, we recursively flatten the child list and then merge it with the current list.

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
                Node* last = curr->child;
                while (last->next) {
                    last = last->next;
                }
                // Merge the child list with the current list
                last->next = curr->next;
                if (curr->next) {
                    curr->next->prev = last;
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
 1---2---3---4---5---6---7
        |
        8---9---10
            |
            11---12
Output: 
1---2---3---8---9---11---12---4---5---6---7
```

## Key Takeaways
- We can solve this problem using a depth-first traversal approach.
- We need to handle the child pointer of each node carefully to avoid losing any nodes during the flattening process.
- The time complexity of this solution is linear, and the space complexity is also linear due to the recursive call stack.