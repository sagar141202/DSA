# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm will iterate through the linked list, maintaining two separate lists: one for nodes with values less than x and another for nodes with values greater than or equal to x. After iterating through the entire list, the two lists will be merged.

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
        // Create two dummy nodes to serve as the start of the two lists
        ListNode* before_head = new ListNode(0);
        ListNode* before = before_head;
        ListNode* after_head = new ListNode(0);
        ListNode* after = after_head;

        // Iterate through the linked list
        while (head) {
            // If the current node's value is less than x, add it to the before list
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } 
            // Otherwise, add it to the after list
            else {
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }

        // Merge the two lists
        after->next = NULL;
        before->next = after_head->next;

        // Return the start of the merged list
        ListNode* new_head = before_head->next;
        delete before_head;
        delete after_head;
        return new_head;
    }
};
```

## Test Cases
```
Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

## Key Takeaways
- Use two separate lists to store nodes with values less than and greater than or equal to x.
- Merge the two lists after iterating through the entire linked list.
- Don't forget to handle edge cases, such as an empty linked list or a list with only one node.