# Add Two Numbers

## Problem Statement
Given the heads of two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of the two numbers should also be stored in reverse order in the result linked list. For example, if the input linked lists are 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8, because 342 + 465 = 807.

## Approach
We can solve this problem by iterating over the two linked lists simultaneously, adding corresponding nodes, and handling any carry-over value. We will create a new linked list to store the result. The algorithm will iterate through the input lists, adding corresponding nodes and handling any carry.

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

        // Iterate over the two linked lists
        while (l1 || l2 || carry) {
            int sum = carry;
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            // Update the carry
            carry = sum / 10;

            // Create a new node with the digit value
            current->next = new ListNode(sum % 10);
            current = current->next;
        }

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
- When dealing with linked lists, it's often helpful to create a dummy node to simplify the code.
- We need to handle the carry-over value when adding the numbers.
- The time complexity is O(max(m, n)), where m and n are the lengths of the input linked lists.