# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list, and return the head of the modified list. The input list is sorted in ascending order, and all nodes in the list have unique values except for the duplicates. For example, given the list 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the function should return the head of the list 1 -> 2 -> 3 -> 4 -> 5.

## Approach
The algorithm iterates over the linked list, comparing each node with its next node. If the values are equal, the next node is skipped by updating the next pointer of the current node to the node after the duplicate. This process continues until the end of the list is reached, effectively removing all duplicates.

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
        // If the list is empty, return the head
        if (head == NULL) return head;
        
        // Initialize the current node
        ListNode* current = head;
        
        // Iterate over the list
        while (current->next != NULL) {
            // If the current node's value is equal to the next node's value
            if (current->val == current->next->val) {
                // Remove the next node by updating the current node's next pointer
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
- The function only removes duplicates from a sorted list.
- The algorithm has a time complexity of O(n) where n is the number of nodes in the list.
- The algorithm has a space complexity of O(1) since it only uses a constant amount of space.