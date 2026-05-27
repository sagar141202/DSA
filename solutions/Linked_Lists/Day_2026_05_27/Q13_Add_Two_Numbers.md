# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The input linked lists are guaranteed to be non-empty and the sum of the two numbers will not exceed 1000. For example, given the linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8, which represents the sum 342 + 465 = 807.

## Approach
The algorithm involves iterating through both linked lists simultaneously, adding corresponding nodes, and handling any carry-over values. We create a new linked list to store the sum. The process continues until all nodes in both lists have been processed.

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
        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;

        // Iterate through both linked lists
        while (l1 || l2 || carry) {
            // Calculate the sum of the current nodes and the carry
            int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;

            // Update the carry
            carry = sum / 10;

            // Create a new node with the digit value
            current->next = new ListNode(sum % 10);
            current = current->next;

            // Move to the next nodes in the linked lists
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        // Return the next node of the dummy node
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Input: l1 = [0], l2 = [0]
Output: [0]
Input: l1 = [9, 9], l2 = [1]
Output: [0, 0, 1]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special handling for the head node.
- Iterate through both linked lists simultaneously and handle the carry-over value.
- Create a new linked list to store the sum, and return the next node of the dummy node.