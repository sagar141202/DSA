# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The approach is to create two separate linked lists, one for nodes with values less than x and one for nodes with values greater than or equal to x. Then, we concatenate these two lists to get the final partitioned list. We use two dummy nodes to simplify the code.

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
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes
        ListNode* before = new ListNode(0);
        ListNode* before_head = before;
        ListNode* after = new ListNode(0);
        ListNode* after_head = after;

        // Partition the list
        while (head) {
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } else {
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }

        // Concatenate the two lists
        after->next = NULL;
        before->next = after_head->next;

        // Return the partitioned list
        return before_head->next;
    }
};
```

## Test Cases
```
Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

## Key Takeaways
- Use two dummy nodes to simplify the code and avoid edge cases.
- Partition the list into two separate lists based on the given condition.
- Concatenate the two lists to get the final partitioned list.