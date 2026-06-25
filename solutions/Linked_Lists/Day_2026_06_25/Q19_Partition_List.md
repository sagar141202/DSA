# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of nodes within each partition should be preserved. For example, given a linked list `1 -> 4 -> 3 -> 2 -> 5 -> 2` and `x = 3`, the partitioned list should be `1 -> 2 -> 2 -> 4 -> 3 -> 5`.

## Approach
We can solve this problem by maintaining two separate linked lists, one for values less than x and one for values greater than or equal to x. We then iterate through the original list, appending each node to the appropriate list. Finally, we concatenate the two lists to obtain the partitioned list.

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
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes for the two lists
        ListNode* before = new ListNode(0);
        ListNode* before_head = before;
        ListNode* after = new ListNode(0);
        ListNode* after_head = after;

        // Traverse the original list
        while (head) {
            // If the current node's value is less than x, append it to the before list
            if (head->val < x) {
                before->next = head;
                before = before->next;
            }
            // Otherwise, append it to the after list
            else {
                after->next = head;
                after = after->next;
            }
            // Move to the next node in the original list
            head = head->next;
        }

        // Set the next pointer of the last node in the after list to nullptr
        after->next = nullptr;
        // Concatenate the two lists
        before->next = after_head->next;
        // Return the head of the partitioned list
        return before_head->next;
    }
};
```

## Test Cases
```
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
Input: head = [2, 1], x = 2
Output: [1, 2]
```

## Key Takeaways
- We use two separate linked lists to store values less than x and values greater than or equal to x.
- We iterate through the original list and append each node to the appropriate list.
- We concatenate the two lists to obtain the partitioned list, preserving the relative order of nodes within each partition.