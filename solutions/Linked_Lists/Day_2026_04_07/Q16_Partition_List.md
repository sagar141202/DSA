# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with a value less than x come before all nodes with a value greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. For example, given the list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm involves creating two separate linked lists, one for nodes with values less than x and another for nodes with values greater than or equal to x. We then concatenate these two lists to obtain the final partitioned list. This approach ensures that the relative order of nodes within each partition is maintained.

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
        // Create two dummy nodes for the two lists
        ListNode* before_head = new ListNode(0);
        ListNode* after_head = new ListNode(0);
        
        // Initialize the tails of the two lists
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
        
        // Connect the two lists and set the next of the last node to NULL
        after->next = NULL;
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
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

## Key Takeaways
- We use two dummy nodes to simplify the code and avoid special handling for the head of the lists.
- The time complexity is O(n) because we only traverse the original list once.
- The space complexity is O(1) because we only use a constant amount of space to store the dummy nodes and the tails of the two lists.