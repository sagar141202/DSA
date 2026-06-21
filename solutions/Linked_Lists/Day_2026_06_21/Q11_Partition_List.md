# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm involves creating two separate linked lists: one for nodes with values less than x and another for nodes with values greater than or equal to x. Then, it connects the two lists to form the partitioned list. We use two dummy nodes to simplify the code and avoid special cases for the head of the lists.

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
        
        // Connect the two lists and set the next of the last node in the after list to NULL
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
Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

## Key Takeaways
- We use two dummy nodes to simplify the code and avoid special cases for the head of the lists.
- The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x are maintained.
- The time complexity is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1), excluding the space needed for the output.