# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list, and return the head of the modified list. The list is sorted in ascending order, and all duplicates should be removed. For example, given the list 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the function should return the head of the list 1 -> 2 -> 3 -> 4 -> 5.

## Approach
The algorithm iterates through the sorted linked list, comparing each node's value with the next node's value. If the values are the same, it skips the next node. If the values are different, it moves to the next node. This process continues until the end of the list is reached.

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
        
        // Iterate through the list
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
- The function assumes that the input list is sorted in ascending order.
- The function has a time complexity of O(n), where n is the number of nodes in the list, because it only iterates through the list once.
- The function has a space complexity of O(1) because it only uses a constant amount of space to store the current node.