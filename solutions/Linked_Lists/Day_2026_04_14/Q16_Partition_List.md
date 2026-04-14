# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The original relative order of the nodes in each group should be preserved. For example, given a linked list with the values 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the output should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm uses two dummy nodes to create two separate lists: one for values less than x and one for values greater than or equal to x. It iterates over the original list, appending each node to the appropriate list. Finally, it connects the two lists.

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
        
        // Initialize pointers for the two lists
        ListNode* before = beforeHead;
        ListNode* after = afterHead;
        
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
            head = head->next;
        }
        
        // Connect the two lists and set the next of the last node in the after list to NULL
        after->next = NULL;
        before->next = afterHead->next;
        
        // Return the head of the partitioned list
        ListNode* result = beforeHead->next;
        delete beforeHead;
        delete afterHead;
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
- Use two dummy nodes to simplify the code and avoid edge cases.
- Iterate over the original list and append each node to the appropriate list.
- Connect the two lists and set the next of the last node in the after list to NULL to avoid cycles.