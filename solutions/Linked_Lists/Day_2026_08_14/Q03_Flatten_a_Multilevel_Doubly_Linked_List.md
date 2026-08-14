# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a new list, which can be a multilevel doubly linked list itself. Your task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The nodes in the flattened list should be in the order of their appearance in the original list. For example, if we have a list with the following structure:
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
- The number of nodes in the list will not exceed 1000.
- The values of the nodes will be between 1 and 1000.

## Approach
We can solve this problem by using a recursive approach to traverse the multilevel linked list and append the child lists to the main list. We will use a depth-first search strategy to flatten the list.

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
1---2---3---7---8---11---12---9---10---4---5---6
```

## Key Takeaways
- Use a depth-first search strategy to traverse the multilevel linked list.
- Connect the child lists to the main list by updating the next and previous pointers.
- Remove the child pointer after connecting the child list to the main list.