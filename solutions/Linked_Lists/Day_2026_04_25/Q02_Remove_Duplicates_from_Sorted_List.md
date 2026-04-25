# Remove Duplicates from Sorted List

## Problem Statement
Given a sorted linked list, remove duplicates from the list and return the modified list. The list should remain sorted after removal of duplicates. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output list should be 1 -> 2 -> 3 -> 4 -> 5. The list can contain any number of nodes and the nodes can have any integer value.

## Approach
We can solve this problem by traversing the linked list and checking each node's value with its next node's value. If the values are the same, we skip the next node. We use a pointer to keep track of the previous node to update its next pointer.

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
        // Initialize a pointer to the head of the list
        ListNode* current = head;
        
        // Traverse the list
        while (current != NULL && current->next != NULL) {
            // If the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // Skip the next node
                current->next = current->next->next;
            } else {
                // Move to the next node
                current = current->next;
            }
        }
        
        // Return the modified list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5

Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- We use a two-pointer approach to traverse the linked list and skip duplicate nodes.
- We only update the next pointer of the previous node when we encounter a duplicate node.
- The time complexity is O(n) where n is the number of nodes in the linked list, and the space complexity is O(1) as we only use a constant amount of space.