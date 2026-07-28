# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The original relative order of the nodes in each of the two partitions should be preserved. The function should return the head of the partitioned list. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm uses two separate linked lists to store nodes with values less than x and nodes with values greater than or equal to x. It iterates through the original list, appending nodes to the correct partition list based on their values. Finally, it concatenates the two partition lists.

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
        ListNode* beforeHead = new ListNode(0);
        ListNode* afterHead = new ListNode(0);
        
        // Initialize pointers for the two partition lists
        ListNode* before = beforeHead;
        ListNode* after = afterHead;
        
        // Iterate through the original list
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
        
        // Set the next pointer of the last node in the after list to NULL
        after->next = NULL;
        
        // Concatenate the two partition lists
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
- Use two separate linked lists to store nodes with values less than x and nodes with values greater than or equal to x.
- Iterate through the original list, appending nodes to the correct partition list based on their values.
- Concatenate the two partition lists to obtain the final partitioned list.