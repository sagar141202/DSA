# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with a value less than x come before all nodes with a value greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm involves creating two separate linked lists, one for nodes with values less than x and one for nodes with values greater than or equal to x. Then, we append the second list to the first list to get the partitioned list. We iterate through the original list, appending each node to the appropriate list.

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
        ListNode* before = new ListNode(0);
        ListNode* before_head = before;
        ListNode* after = new ListNode(0);
        ListNode* after_head = after;

        // Traverse the original list
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

        // Set the next pointer of the last node in the before list to the first node in the after list
        after->next = NULL;  // To avoid infinite loop
        before->next = after_head->next;

        // Return the partitioned list
        return before_head->next;
    }
};
```

## Test Cases
```
Input: [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

## Key Takeaways
- We create two separate linked lists to store nodes with values less than and greater than or equal to x.
- We use dummy nodes to simplify the code and avoid edge cases.
- We traverse the original list and append each node to the appropriate list based on its value.