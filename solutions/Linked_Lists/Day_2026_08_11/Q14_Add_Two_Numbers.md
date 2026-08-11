# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The digits in the result should also be stored in reverse order. For example, given the linked lists `2 -> 4 -> 3` and `5 -> 6 -> 4`, the result should be `7 -> 0 -> 8`, representing the sum `342 + 465 = 807`.

## Approach
We will use a simple iterative approach to solve this problem, where we initialize a dummy node and traverse both linked lists from left to right, adding corresponding nodes and handling any carry-over values. We will also keep track of the current node in the result linked list.

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
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        int carry = 0;
        
        // Traverse both linked lists
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
Input: l1 = [0], l2 = [0]
Output: [0]
Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid dealing with special cases for the head of the result linked list.
- Keep track of the carry-over value to handle cases where the sum of two digits is greater than 9.
- Traverse both linked lists simultaneously and add corresponding nodes to get the result.