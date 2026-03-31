# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned linked list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The solution involves creating two separate linked lists, one for nodes with values less than x and another for nodes with values greater than or equal to x. We then connect the two lists to form the partitioned list. This approach preserves the relative order of nodes within each partition.

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
        ListNode* before_head = new ListNode(0);
        ListNode* before = before_head;
        ListNode* after_head = new ListNode(0);
        ListNode* after = after_head;
        
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
        
        // Connect the two lists and return the result
        after->next = NULL;
        before->next = after_head->next;
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
- We use two dummy nodes to simplify the code and avoid dealing with NULL pointer exceptions.
- The time complexity is O(n) because we only traverse the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the dummy nodes and other variables.