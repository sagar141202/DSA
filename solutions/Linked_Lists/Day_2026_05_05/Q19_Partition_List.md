# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm uses two separate linked lists to store nodes with values less than x and nodes with values greater than or equal to x. It then merges these two lists to form the final partitioned list. The algorithm iterates over the original list, appending nodes to the appropriate list based on their value relative to x.

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
        // Create two dummy nodes to serve as the heads of the two lists
        ListNode* before_head = new ListNode(0);
        ListNode* after_head = new ListNode(0);
        
        // Initialize pointers to the current nodes in the two lists
        ListNode* before = before_head;
        ListNode* after = after_head;
        
        // Iterate over the original list
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
        
        // Merge the two lists
        after->next = nullptr;
        before->next = after_head->next;
        
        // Return the head of the partitioned list
        ListNode* result = before_head->next;
        delete before_head;
        delete after_head;
        return result;
    }
};
```

## Test Cases
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Input: head = [2,1], x = 2
Output: [1,2]
```

## Key Takeaways
- Use two separate linked lists to store nodes with values less than x and nodes with values greater than or equal to x.
- Iterate over the original list, appending nodes to the appropriate list based on their value relative to x.
- Merge the two lists to form the final partitioned list.