# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove duplicates from the list and return the head of the modified list. The list should remain sorted after the removal of duplicates. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output list should be 1 -> 2 -> 3 -> 4 -> 5. The list nodes are defined as public class ListNode { int val; ListNode next; ListNode() {} ListNode(int val) { this.val = val; } ListNode(int val, ListNode next) { this.val = val; this.next = next; } }.

## Approach
The algorithm iterates through the linked list, comparing each node's value with the next node's value. If the values are the same, it removes the next node. This process continues until all duplicates are removed. The function returns the head of the modified list.

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
        // Initialize current node as head
        ListNode* current = head;
        
        // Traverse the list
        while (current != nullptr && current->next != nullptr) {
            // If current node's value is the same as the next node's value
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
- The algorithm has a time complexity of O(n) where n is the number of nodes in the list.
- The algorithm has a space complexity of O(1) as it only uses a constant amount of space to store the current node.
- The function modifies the original list by removing duplicates and returns the head of the modified list.