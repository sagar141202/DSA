# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of another doubly linked list, which can also have child pointers. The task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The nodes in the resulting list should be in the order of their appearance in the original list, with the nodes from the child lists inserted between their parent nodes. For example, given the following multilevel doubly linked list:
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
The constraints are that the input list is not empty and the nodes have unique values.

## Approach
We can solve this problem by iterating over the nodes in the list and recursively flattening the child lists. When a child list is encountered, we insert its nodes between the current node and the next node in the list.

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
                
                // Insert the child list between curr and curr->next
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
- The key to solving this problem is to recursively flatten the child lists and insert them between the current node and the next node in the list.
- We need to update the next and previous pointers of the nodes in the child list and the main list to maintain the correct order.
- The time complexity of this solution is O(N), where N is the total number of nodes in the multilevel doubly linked list.