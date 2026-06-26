# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The child pointer points to the head of a nested list. Your task is to flatten the list so that all nodes are at the same level. The resulting list should be a doubly linked list, where each node has a value, a next pointer, and a prev pointer. For example, given the following multilevel doubly linked list:
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
The constraints are:
- The number of nodes in the list is between 1 and 10^5.
- The value of each node is between 1 and 10^5.

## Approach
The algorithm involves recursively flattening the nested lists and then appending them to the main list. We will use a recursive approach to traverse the list and flatten the nested lists. The key idea is to keep track of the current node and its next pointer, and then update the next pointer to point to the head of the flattened nested list.

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
            // If the current node has a child, flatten the child list
            if (curr->child) {
                // Find the tail of the child list
                Node* childTail = curr->child;
                while (childTail->next) {
                    childTail = childTail->next;
                }
                // Connect the tail of the child list to the next node in the main list
                childTail->next = curr->next;
                if (curr->next) {
                    curr->next->prev = childTail;
                }
                // Connect the current node to the head of the child list
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
          7---8---9---10
              |
              11---12
Output: 
1---2---3---7---8---11---12---9---10---4---5---6
```

## Key Takeaways
- The key to solving this problem is to keep track of the current node and its next pointer, and then update the next pointer to point to the head of the flattened nested list.
- The recursive approach allows us to traverse the list and flatten the nested lists efficiently.
- The time complexity is O(N) because we visit each node once, and the space complexity is O(N) because we need to store the recursive call stack.