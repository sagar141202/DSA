# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list, such that each element appears only once. The relative order of the elements should be kept the same. The list should be modified in-place. For example, given the sorted linked list `1 -> 1 -> 2 -> 3 -> 3`, the function should return `1 -> 2 -> 3`. The function should handle cases where the list is empty or contains only one node.

## Approach
The algorithm iterates over the linked list, comparing each node's value with the next node's value. If the values are the same, the next node is removed. This process continues until the end of the list is reached. The function uses a pointer to keep track of the current node and another pointer to keep track of the next node.

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
        // Initialize a pointer to the head of the list
        ListNode* current = head;
        
        // Traverse the list
        while (current != nullptr && current->next != nullptr) {
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
Input: 1 -> 1 -> 2 -> 3 -> 3
Output: 1 -> 2 -> 3

Input: 1 -> 2 -> 3
Output: 1 -> 2 -> 3

Input: 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- The function modifies the list in-place, meaning it does not create a new list.
- The function handles cases where the list is empty or contains only one node.
- The time complexity is O(n), where n is the number of nodes in the list, because we are traversing the list once.