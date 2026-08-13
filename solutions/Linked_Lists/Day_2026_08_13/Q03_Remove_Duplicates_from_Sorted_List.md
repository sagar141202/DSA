# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list. The function should return the head of the modified list. The list is sorted in ascending order, and all duplicate nodes should be removed. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output list should be 1 -> 2 -> 3 -> 4 -> 5.

## Approach
The approach is to iterate through the linked list and compare each node with its next node. If the values are the same, we skip the duplicate node by updating the next pointer of the current node. This process continues until we reach the end of the list.

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
        
        // Traverse the list until we reach the end
        while (current != NULL && current->next != NULL) {
            // If the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // Remove the duplicate node by updating the next pointer
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

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5

Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- We only need to traverse the list once to remove duplicates.
- We update the next pointer of the current node to remove duplicates.
- The time complexity is linear because we only traverse the list once.