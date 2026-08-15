# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. The list should be modified in-place.

## Approach
The approach involves creating two separate linked lists, one for nodes with values less than x and another for nodes with values greater than or equal to x. Then, we concatenate these two lists to form the final partitioned list. We use two dummy nodes to simplify the code and avoid edge cases.

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
        ListNode* beforeHead = new ListNode(0);
        ListNode* afterHead = new ListNode(0);
        
        // Initialize pointers
        ListNode* before = beforeHead;
        ListNode* after = afterHead;
        
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
        
        // Connect the before list and the after list
        after->next = NULL;
        before->next = afterHead->next;
        
        // Return the partitioned list
        return beforeHead->next;
    }
};
```

## Test Cases
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

## Key Takeaways
- We use two dummy nodes to simplify the code and avoid edge cases.
- The time complexity is O(n), where n is the number of nodes in the linked list.
- The space complexity is O(1), as we only use a constant amount of space to store the dummy nodes and pointers.