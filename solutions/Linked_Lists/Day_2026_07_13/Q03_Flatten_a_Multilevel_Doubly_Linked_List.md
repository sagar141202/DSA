# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a nested list. Your task is to flatten this multilevel linked list into a single-level doubly linked list. The nodes in the flattened list should be in the order of their appearance in the original list, with the nodes from the child lists appearing after their parent node. For example, if we have a node with value 1 and a child node with value 2, the resulting list should have the order 1, 2. The constraints are that the input list is non-empty and the nodes have unique values.

## Approach
We will use a recursive approach to solve this problem. We will start by iterating over the nodes in the list and if a node has a child, we will recursively flatten the child list and then merge it with the current list.

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
                // Find the last node in the child list
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
1 -> 2 -> 3 -> 4 -> 5 -> 6
where 3 has a child 7 -> 8 -> 9
and 8 has a child 10 -> 11
Output: 
1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6
```

## Key Takeaways
- The key to solving this problem is to recognize that we need to recursively flatten the child lists and then merge them with the current list.
- We need to update the next and previous pointers of the nodes when merging the lists.
- The time complexity of the solution is O(N) where N is the total number of nodes in the list.