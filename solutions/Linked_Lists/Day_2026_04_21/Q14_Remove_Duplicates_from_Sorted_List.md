# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list. The function should return the head of the modified list. The list is sorted in ascending order, and each node has a unique identifier. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4, the output list should be 1 -> 2 -> 3 -> 4.

## Approach
The algorithm iterates over the list, comparing each node with its next node. If the values are the same, it skips the next node. This process continues until all duplicates are removed from the list. The function uses a two-pointer technique to keep track of the current node and its next node.

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
        // If the list is empty, return NULL
        if (!head) return head;

        // Initialize two pointers
        ListNode* current = head;
        while (current->next) {
            // If the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // Remove the next node
                current->next = current->next->next;
            } else {
                // Move to the next node
                current = current->next;
            }
        }
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4
Output: 1 -> 2 -> 3 -> 4

Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1

Input: NULL
Output: NULL
```

## Key Takeaways
- Use a two-pointer technique to keep track of the current node and its next node.
- Compare the values of the current node and its next node to determine if a duplicate exists.
- Remove the next node if it is a duplicate by updating the current node's next pointer.