# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with a value less than x come before all nodes with a value greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm uses two separate linked lists to store nodes with values less than x and greater than or equal to x. It iterates over the original list, appending nodes to the appropriate list based on their value. Finally, it concatenates the two lists.

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
        // Create two dummy nodes to serve as the start of the two lists
        ListNode* before_head = new ListNode(0);
        ListNode* after_head = new ListNode(0);
        
        // Initialize pointers for the two lists
        ListNode* before = before_head;
        ListNode* after = after_head;
        
        // Iterate over the original list
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
        
        // Set the next pointer of the last node in the before list to the first node in the after list
        after->next = nullptr;
        before->next = after_head->next;
        
        // Return the start of the partitioned list
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
```

## Key Takeaways
- Use two separate linked lists to store nodes with values less than x and greater than or equal to x.
- Iterate over the original list, appending nodes to the appropriate list based on their value.
- Concatenate the two lists by setting the next pointer of the last node in the before list to the first node in the after list.