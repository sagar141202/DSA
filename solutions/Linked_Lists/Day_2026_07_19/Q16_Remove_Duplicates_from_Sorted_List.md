# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list. The list should remain sorted after the removal of duplicates. For example, if the input is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output should be 1 -> 2 -> 3 -> 4 -> 5. The function should take the head of the linked list as input and return the head of the modified linked list.

## Approach
The approach is to traverse the linked list and check if the current node's value is equal to the next node's value. If they are equal, we remove the next node. We continue this process until we reach the end of the list. This way, we ensure that all duplicates are removed from the sorted list.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // If the list is empty, return the head
        if (!head) return head;
        
        // Initialize the current node
        ListNode* current = head;
        
        // Traverse the list
        while (current->next) {
            // If the current node's value is equal to the next node's value, remove the next node
            if (current->val == current->next->val) {
                current->next = current->next->next;
            } else {
                // Otherwise, move to the next node
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
- We only need to traverse the list once to remove all duplicates.
- We do not need any extra space to store the unique elements, making the space complexity O(1).
- The function modifies the original list and returns the head of the modified list.