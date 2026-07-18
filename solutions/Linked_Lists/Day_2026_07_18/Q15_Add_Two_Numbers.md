# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The list should also be in reverse order, with each node containing a single digit. For example, if the input is 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8, which represents the sum 342 + 465 = 807.

## Approach
We can solve this problem by iterating through the two linked lists, adding corresponding nodes, and handling any carry-over values. We will create a new linked list to store the result. The algorithm will terminate when we have processed all nodes in both lists.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Initialize a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;

        // Iterate through the two linked lists
        while (l1 != nullptr || l2 != nullptr) {
            int x = (l1 != nullptr) ? l1->val : 0;
            int y = (l2 != nullptr) ? l2->val : 0;
            int sum = carry + x + y;
            carry = sum / 10;

            // Create a new node with the sum
            current->next = new ListNode(sum % 10);
            current = current->next;

            // Move to the next nodes in the lists
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
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
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Input: l1 = [0], l2 = [0]
Output: [0]
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Key Takeaways
- We can use a dummy node to simplify the code and avoid special cases for the head of the result list.
- We should handle any remaining carry-over value after iterating through the lists.
- The time complexity is O(max(m, n)), where m and n are the lengths of the input linked lists.