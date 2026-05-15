# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list and return the head of the new list. The linked list will have at least one node, and all nodes will have unique values except for duplicates. For example, given the list 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the function should return 1 -> 2 -> 3 -> 4 -> 5.

## Approach
The algorithm iterates over the linked list, comparing each node's value with the next node's value. If they are the same, it skips the next node. If they are different, it moves to the next node. This process continues until the end of the list is reached.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // Initialize the current node as the head of the list
        ListNode* current = head;
        
        // Traverse the list
        while (current != NULL && current->next != NULL) {
            // If the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // Remove the next node
                current->next = current->next->next;
            } else {
                // Move to the next node
                current = current->next;
            }
        }
        
        // Return the head of the modified list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
```

## Key Takeaways
- Use a two-pointer approach (current and next) to traverse the linked list.
- Compare the values of adjacent nodes to determine if a node should be removed.
- Update the next pointer of the current node to skip the duplicate node.