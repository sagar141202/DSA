# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with a value less than x come before all nodes with a value greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned linked list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm involves creating two separate linked lists, one for nodes with values less than x and one for nodes with values greater than or equal to x. We then concatenate these two linked lists to obtain the final partitioned linked list. This approach ensures that the relative order of nodes within each partition is maintained.

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
        // Create two separate linked lists
        ListNode* before = new ListNode(0);
        ListNode* beforeHead = before;
        ListNode* after = new ListNode(0);
        ListNode* afterHead = after;

        // Traverse the original linked list
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

        // Concatenate the two linked lists
        after->next = NULL;
        before->next = afterHead->next;
        return beforeHead->next;
    }
};
```

## Test Cases
```
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

## Key Takeaways
- We create two separate linked lists to maintain the relative order of nodes within each partition.
- The algorithm has a linear time complexity because we only traverse the original linked list once.
- The space complexity is constant because we only use a fixed amount of space to store the two separate linked lists.