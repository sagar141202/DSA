# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm uses two separate linked lists to store nodes with values less than x and nodes with values greater than or equal to x. It iterates through the original list, appending nodes to the appropriate list based on their value. Finally, it combines the two lists.

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
        ListNode* after_head = new ListNode(0);
        
        // Initialize pointers for the two lists
        ListNode* before = before_head;
        ListNode* after = after_head;
        
        // Traverse the original list
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
        
        // Combine the two lists
        after->next = NULL;
        before->next = after_head->next;
        
        // Return the new head of the combined list
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
Input: 2 -> 1, x = 2
Output: 1 -> 2
```

## Key Takeaways
- We can use two separate linked lists to partition the original list based on a given value.
- The relative order of nodes with values less than the given value and the relative order of nodes with values greater than or equal to the given value are maintained.
- The solution has a time complexity of O(n), where n is the number of nodes in the linked list, and a space complexity of O(1), excluding the space needed for the output.