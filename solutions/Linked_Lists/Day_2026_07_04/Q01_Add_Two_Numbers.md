# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The list is in reverse order, and each node contains a single digit. For example, given the linked lists `2 -> 4 -> 3` and `5 -> 6 -> 4`, the output should be `7 -> 0 -> 8`, which represents the sum `342 + 465 = 807`.

## Approach
The algorithm iterates through both linked lists, adding corresponding nodes and handling any carry-over values. This process continues until all nodes in both lists have been processed, and any remaining carry-over value is appended as a new node.

## Complexity
- Time: O(max(m, n))
- Space: O(max(m, n))

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Initialize a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;

        // Iterate through both linked lists
        while (l1 != NULL || l2 != NULL) {
            int x = (l1 != NULL) ? l1->val : 0;
            int y = (l2 != NULL) ? l2->val : 0;

            // Calculate the sum and update the carry
            int sum = carry + x + y;
            carry = sum / 10;

            // Create a new node with the digit value
            current->next = new ListNode(sum % 10);
            current = current->next;

            // Move to the next nodes in both lists
            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next;
        }

        // Handle any remaining carry-over value
        if (carry > 0) {
            current->next = new ListNode(carry);
        }

        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
```

## Key Takeaways
- The algorithm handles linked lists of varying lengths by using a while loop that continues until all nodes in both lists have been processed.
- The use of a dummy node simplifies the code by avoiding special cases for the head of the result list.
- The solution has a time complexity of O(max(m, n)), where m and n are the lengths of the input linked lists, since it only requires a single pass through both lists.