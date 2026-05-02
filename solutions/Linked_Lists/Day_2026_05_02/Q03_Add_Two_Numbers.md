# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of the two numbers should also be stored in reverse order, with each node containing a single digit. For example, if the input linked lists are 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8, representing the sum 342 + 465 = 807.

## Approach
We will use a simple iterative approach to add the two numbers. We will traverse both linked lists simultaneously, adding corresponding nodes and keeping track of any carry-over value. We will use a dummy node to simplify the code and avoid special cases for the head of the result list.

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
            int sum = 0;
            // Add the values of the current nodes
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            // Add the carry-over value
            sum += carry;
            // Update the carry-over value
            carry = sum / 10;
            // Create a new node with the digit value
            current->next = new ListNode(sum % 10);
            current = current->next;
        }
        // Return the result list (excluding the dummy node)
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
- Use a dummy node to simplify the code and avoid special cases for the head of the result list.
- Traverse both linked lists simultaneously to add corresponding nodes.
- Keep track of any carry-over value to ensure accurate results.