# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list would be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The approach is to create two separate linked lists, one for nodes with values less than x and another for nodes with values greater than or equal to x. Then, we concatenate these two lists to get the final partitioned list. We use two pointers to traverse the original list and append nodes to the appropriate lists.

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
        // Create two dummy nodes to simplify the code
        ListNode* before_dummy = new ListNode(0);
        ListNode* after_dummy = new ListNode(0);
        
        // Initialize pointers
        ListNode* before = before_dummy;
        ListNode* after = after_dummy;
        
        // Traverse the original list
        while (head) {
            if (head->val < x) {
                // Append node to the before list
                before->next = head;
                before = before->next;
            } else {
                // Append node to the after list
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }
        
        // Concatenate the two lists
        after->next = NULL;
        before->next = after_dummy->next;
        
        // Return the partitioned list
        return before_dummy->next;
    }
};
```

## Test Cases
```
Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

## Key Takeaways
- We use two dummy nodes to simplify the code and avoid edge cases.
- We use two pointers to traverse the original list and append nodes to the appropriate lists.
- We concatenate the two lists by setting the next pointer of the last node in the before list to the first node in the after list.