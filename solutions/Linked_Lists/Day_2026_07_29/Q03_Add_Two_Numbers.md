# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of the two numbers should also be stored in reverse order. For example, given the linked lists `2 -> 4 -> 3` and `5 -> 6 -> 4`, the output should be `7 -> 0 -> 8`, which represents the sum `807`.

## Approach
The algorithm involves traversing the linked lists, adding corresponding nodes, and handling any carry-over values. We create a new linked list with the sum of the nodes and any carry-over value. The algorithm continues until all nodes have been processed.

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

        // Traverse the linked lists
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

            // Update the carry and the current node's value
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
Input: l1 = [9, 9], l2 = [1]
Output: [0, 0, 1]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special handling for the head node.
- Traverse the linked lists and add corresponding nodes, handling any carry-over values.
- Create a new linked list with the sum of the nodes and any carry-over value.