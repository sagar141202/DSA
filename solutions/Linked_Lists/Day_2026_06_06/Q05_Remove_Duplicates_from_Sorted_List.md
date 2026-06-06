# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list and return the head of the modified list. The list should remain sorted after the removal of duplicates. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output should be 1 -> 2 -> 3 -> 4 -> 5.

## Approach
The approach is to traverse the linked list and compare each node with its next node. If the values are the same, we skip the next node. We use a pointer to keep track of the last non-duplicate node.

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
        // If the list is empty, return nullptr
        if (head == nullptr) return head;
        
        // Initialize two pointers
        ListNode* current = head;
        
        // Traverse the list
        while (current->next != nullptr) {
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
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
Input: nullptr
Output: nullptr
```

## Key Takeaways
- We can solve this problem by using a two-pointer approach, where one pointer is used to traverse the list and the other pointer is used to keep track of the last non-duplicate node.
- The time complexity is O(n) because we only traverse the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers.