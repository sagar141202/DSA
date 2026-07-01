# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. The relative order of the elements should be kept the same. For example, given a sorted linked list `1 -> 1 -> 2 -> 3 -> 3`, the function should return `1 -> 2 -> 3`. The linked list is sorted in ascending order, and all nodes are non-null.

## Approach
The algorithm iterates through the linked list, comparing each node with its next node. If the values are the same, it skips the duplicate node. This process continues until all nodes have been traversed. The function then returns the head of the modified linked list.

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
        // Initialize current node
        ListNode* current = head;
        
        // Traverse the linked list
        while (current && current->next) {
            // If current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // Skip the duplicate node
                current->next = current->next->next;
            } else {
                // Move to the next node
                current = current->next;
            }
        }
        
        // Return the head of the modified linked list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3
Output: 1 -> 2 -> 3
Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- We only need to compare each node with its next node to remove duplicates in a sorted linked list.
- The time complexity is linear because we are traversing the linked list once.
- The space complexity is constant because we are not using any additional data structures that scale with the input size.