# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove duplicates from the list and return the head of the modified list. The list should remain sorted after removing duplicates. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4, the output should be 1 -> 2 -> 3 -> 4. The list is singly linked, and each node has a value and a pointer to the next node.

## Approach
We will use a two-pointer approach to traverse the list, skipping duplicates by comparing adjacent nodes. If the values are the same, we skip the current node; otherwise, we move both pointers forward.

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
        // if the list is empty, return head (which is nullptr)
        if (!head) return head;
        
        // initialize two pointers
        ListNode* current = head;
        while (current->next) {
            // if the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // skip the next node
                current->next = current->next->next;
            } else {
                // move the current pointer forward
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
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- We only need to compare adjacent nodes in a sorted list to remove duplicates.
- The two-pointer approach allows us to traverse the list while modifying it.
- The time complexity is linear because we only traverse the list once.