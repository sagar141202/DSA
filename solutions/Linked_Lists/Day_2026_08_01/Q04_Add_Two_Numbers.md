# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers can be computed by iterating through the linked lists and adding corresponding nodes. If the sum of two nodes is greater than 9, then we need to carry the extra digit to the next node. For example, given two linked lists, 2 -> 4 -> 3 and 5 -> 6 -> 4, the sum of these two linked lists is 7 -> 0 -> 8.

## Approach
The approach is to traverse both linked lists simultaneously, adding corresponding nodes and handling any carry-over values. We will create a new linked list with the sum of the corresponding nodes from the input linked lists.

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
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Input: l1 = [0], l2 = [0]
Output: [0]
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Key Takeaways
- Always initialize a dummy node to simplify the code and avoid edge cases.
- Traverse both linked lists simultaneously, adding corresponding nodes and handling any carry-over values.
- Create a new linked list with the sum of the corresponding nodes from the input linked lists.