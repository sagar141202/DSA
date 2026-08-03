# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove all duplicates and return the head of the modified list. The list should remain sorted after removal. For example, given the list 1 -> 1 -> 2 -> 3 -> 3, the function should return 1 -> 2 -> 3. The function should only use O(1) extra space.

## Approach
The algorithm iterates through the linked list, comparing each node with its next node. If the values are the same, it skips the next node. If the values are different, it moves to the next node. This process continues until the end of the list is reached.

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
Input: 1 -> 1 -> 2 -> 3 -> 3
Output: 1 -> 2 -> 3
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- Use a two-pointer approach (current and next) to traverse the linked list.
- Compare the values of adjacent nodes to determine if a node should be removed.
- Update the next pointer of the current node to skip the duplicate node.