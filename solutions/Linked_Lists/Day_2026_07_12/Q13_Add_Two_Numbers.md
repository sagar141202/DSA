# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers should also be in reverse order. For example, given linked lists `2 -> 4 -> 3` and `5 -> 6 -> 4`, the sum would be `7 -> 0 -> 8` because `342 + 465 = 807`. The input linked lists will have a maximum of 100 nodes, and each node's value will be between 0 and 9.

## Approach
We can iterate over the two linked lists, adding corresponding nodes and keeping track of any carry-over value. This approach ensures that we correctly calculate the sum of the two numbers represented by the linked lists. We'll create a new linked list to store the result.

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

        // Iterate over the two linked lists
        while (l1 != NULL || l2 != NULL || carry != 0) {
            int sum = carry;
            if (l1 != NULL) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                sum += l2->val;
                l2 = l2->next;
            }

            // Update the carry and create a new node
            carry = sum / 10;
            current->next = new ListNode(sum % 10);
            current = current->next;
        }

        // Return the result (excluding the dummy node)
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
- Use a dummy node to simplify the code and avoid special cases for the head of the result linked list.
- Keep track of the carry-over value to correctly calculate the sum of the two numbers.
- Create a new linked list to store the result, rather than modifying the input linked lists.