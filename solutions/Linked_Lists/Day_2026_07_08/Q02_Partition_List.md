# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned linked list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
We will use two dummy nodes to create two separate lists: one for nodes with values less than x and one for nodes with values greater than or equal to x. We will then concatenate these two lists to get the final partitioned list. The algorithm will iterate through the original list, appending nodes to the correct list based on their value.

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
        // Create two dummy nodes
        ListNode* before = new ListNode(0);
        ListNode* before_head = before;
        ListNode* after = new ListNode(0);
        ListNode* after_head = after;

        // Partition the list
        while (head) {
            if (head->val < x) {
                // Add node to the before list
                before->next = head;
                before = before->next;
            } else {
                // Add node to the after list
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }

        // Concatenate the two lists
        after->next = nullptr;
        before->next = after_head->next;

        // Return the partitioned list
        return before_head->next;
    }
};
```

## Test Cases
```
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

## Key Takeaways
- Use two dummy nodes to create two separate lists for nodes with values less than x and nodes with values greater than or equal to x.
- Iterate through the original list, appending nodes to the correct list based on their value.
- Concatenate the two lists to get the final partitioned list.