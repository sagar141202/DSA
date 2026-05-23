# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers should also be stored in reverse order, and each node should contain a single digit. For example, if the first linked list is 2 -> 4 -> 3 and the second linked list is 5 -> 6 -> 4, then the sum should be 7 -> 0 -> 8.

## Approach
The approach is to traverse the two linked lists and add corresponding nodes together, handling any carry-over values. We can create a new linked list to store the sum of the two numbers.

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

        // Traverse the two linked lists
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

            // Calculate the carry and the current node's value
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
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Input: l1 = [0], l2 = [0]
Output: [0]
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Key Takeaways
- Always consider edge cases, such as when one linked list is longer than the other.
- Use a dummy node to simplify the code and avoid dealing with special cases for the head of the list.
- Be careful when calculating the carry and the current node's value to avoid integer overflow.