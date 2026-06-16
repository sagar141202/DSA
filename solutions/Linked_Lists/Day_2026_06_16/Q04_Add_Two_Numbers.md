# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The input linked lists may have different lengths, and you should handle cases where the sum of two digits is greater than 9. For example, given linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8, representing the sum 342 + 465 = 807.

## Approach
The solution involves traversing both linked lists simultaneously, adding corresponding nodes, and handling any carry-over values. We create a new linked list with the sum of the nodes and any carry. This approach ensures that we correctly handle cases where the sum of two digits is greater than 9.

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

        // Traverse both linked lists
        while (l1 || l2 || carry) {
            int x = (l1 != NULL) ? l1->val : 0;
            int y = (l2 != NULL) ? l2->val : 0;

            // Calculate the sum and carry
            int sum = carry + x + y;
            carry = sum / 10;

            // Create a new node with the sum
            current->next = new ListNode(sum % 10);
            current = current->next;

            // Move to the next nodes
            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next;
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
Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]
```

## Key Takeaways
- We use a dummy node to simplify the code and avoid special handling for the head of the result linked list.
- We traverse both linked lists simultaneously, adding corresponding nodes and handling any carry-over values.
- The time complexity is O(max(m, n)), where m and n are the lengths of the input linked lists, and the space complexity is O(max(m, n)) for the result linked list.