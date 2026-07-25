# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are non-empty and each node has a unique integer value. The function should return the head of the merged linked list. For example, given two lists `1 -> 2 -> 4` and `1 -> 3 -> 4`, the merged list should be `1 -> 1 -> 2 -> 3 -> 4 -> 4`. The input lists are guaranteed to be sorted in non-decreasing order.

## Approach
The algorithm iterates through both lists simultaneously, comparing node values and adding the smaller one to the merged list. This process continues until all nodes from both lists are incorporated into the merged list. The function utilizes a dummy node to simplify the merging process.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a dummy node to simplify the merging process
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Iterate through both lists simultaneously
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                // Add the smaller node to the merged list
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Append any remaining nodes from either list
        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list (excluding the dummy node)
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Input: l1 = [], l2 = [0]
Output: [0]
Input: l1 = [0], l2 = []
Output: [0]
```

## Key Takeaways
- Use a dummy node to simplify the merging process and avoid special handling for the head of the merged list.
- Compare node values and add the smaller one to the merged list to maintain sorted order.
- Append any remaining nodes from either list to ensure all elements are included in the merged list.