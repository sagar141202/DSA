# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers should also be stored in reverse order. For example, given the linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the sum would be 7 -> 0 -> 8, which corresponds to the number 807.

## Approach
We will iterate through both linked lists simultaneously, adding corresponding nodes and keeping track of any carry-over value. We will create a new linked list with the sum of the nodes and the carry-over value.

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
        // Initialize a dummy node
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        // Iterate through both linked lists
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
            
            // Update carry and create a new node
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
- Use a dummy node to simplify the code and avoid edge cases.
- Keep track of the carry-over value to handle cases where the sum of two nodes is greater than 9.
- Create a new linked list with the sum of the nodes and the carry-over value.