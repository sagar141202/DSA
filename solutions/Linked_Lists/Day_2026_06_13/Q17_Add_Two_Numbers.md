# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The input linked lists may have different lengths, and the sum of the two numbers may be larger than the maximum value that can be represented by a single linked list node. For example, given the linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8, representing the sum 342 + 465 = 807.

## Approach
The algorithm involves iterating over both linked lists, adding corresponding nodes, and handling the carry-over value. We will use a dummy node to simplify the code and avoid special cases for the head of the result list. The addition is performed from right to left, as the digits are stored in reverse order.

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
        
        // Iterate over both linked lists
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
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Input: l1 = [0], l2 = [0]
Output: [0]
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special cases for the head of the result list.
- Iterate over both linked lists and add corresponding nodes, handling the carry-over value.
- Create a new node with the digit value and update the carry-over value for the next iteration.