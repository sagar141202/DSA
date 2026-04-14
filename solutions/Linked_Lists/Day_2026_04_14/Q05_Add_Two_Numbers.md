# Add Two Numbers

## Problem Statement
Given two non-empty linked lists representing two non-negative integers, where each node represents a digit and the digits are stored in reverse order, add the two numbers and return the sum as a linked list. The digits are stored in reverse order, meaning the least significant digit is at the head of the list. For example, the number 123 would be represented as 3 -> 2 -> 1. The input linked lists will have a maximum of 100 nodes, and the values of the nodes will be between 0 and 9. The sum of the two numbers will not exceed 1000.

## Approach
We will iterate over the two linked lists simultaneously, adding corresponding nodes and keeping track of any carry-over value. We will use a dummy node to simplify the code and avoid special cases for the head of the list. The algorithm will run in linear time, proportional to the length of the input linked lists.

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
            // Update the carry and create a new node
            carry = sum / 10;
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
Explanation: 342 + 465 = 807
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special cases for the head of the list.
- Iterate over the two linked lists simultaneously, keeping track of any carry-over value.
- Use the modulo operator to extract the last digit of the sum and the division operator to update the carry.