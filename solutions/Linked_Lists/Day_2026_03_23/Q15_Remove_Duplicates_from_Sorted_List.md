# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list and return the head of the modified list. The linked list is sorted in ascending order, and all nodes with duplicate values should be removed. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output should be 1 -> 2 -> 3 -> 4 -> 5.

## Approach
We will iterate through the linked list, checking each node's value with its next node's value. If the values are the same, we will skip the current node. If the values are different, we will keep the current node and move to the next one. This approach ensures that all duplicate values are removed from the sorted list.

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
        // Initialize the current node
        ListNode* current = head;
        
        // Traverse the linked list
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
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- We only need to traverse the linked list once to remove all duplicates.
- The time complexity is O(n), where n is the number of nodes in the linked list.
- The space complexity is O(1), as we are not using any extra space that scales with the input size.