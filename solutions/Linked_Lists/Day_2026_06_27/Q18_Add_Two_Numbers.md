# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The input linked lists may have different lengths, and it is guaranteed that the sum of the two numbers will not exceed the maximum limit of the integer data type. For example, given the linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the sum is 7 -> 0 -> 8, which corresponds to the integer 807.

## Approach
We can solve this problem by iterating through both linked lists simultaneously, adding corresponding nodes, and handling any carry-over values. We will create a new linked list to store the sum.

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
            int sum = carry;
            // Add the values of the current nodes
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
Input: l1 = [9, 9], l2 = [1]
Output: [0, 0, 1]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid edge cases.
- Iterate through both linked lists simultaneously and handle any carry-over values.
- Create a new linked list to store the sum, and update the nodes accordingly.