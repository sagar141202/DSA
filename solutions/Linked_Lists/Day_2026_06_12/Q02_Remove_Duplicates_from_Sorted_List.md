# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list and return the head of the modified list. The list is sorted in non-decreasing order. For example, given the list 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the function should return the head of the list 1 -> 2 -> 3 -> 4 -> 5.

## Approach
The approach is to traverse the linked list and compare each node's value with the next node's value. If the values are the same, we skip the next node by updating the current node's next pointer. This process continues until the end of the list is reached.

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
        // if the list is empty, return nullptr
        if (!head) return nullptr;
        
        // initialize the current node
        ListNode* current = head;
        
        // traverse the list
        while (current->next) {
            // if the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // skip the next node by updating the current node's next pointer
                current->next = current->next->next;
            } else {
                // move to the next node
                current = current->next;
            }
        }
        
        // return the head of the modified list
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
- The function assumes that the input list is sorted in non-decreasing order.
- The time complexity is O(n), where n is the number of nodes in the list, because we only traverse the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the current node.