# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers should also be stored in reverse order, and each node should contain a single digit. For example, if the input linked lists are 2 -> 4 -> 3 and 5 -> 6 -> 4, the output linked list should be 7 -> 0 -> 8, which represents the sum 342 + 465 = 807.

## Approach
We can solve this problem by iterating through both linked lists simultaneously, adding corresponding nodes, and handling any carry-over values. We will create a new linked list to store the sum of the two input linked lists.

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
        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        // Iterate through both linked lists
        while (l1 != nullptr || l2 != nullptr) {
            int sum = carry;
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            
            // Update the carry and create a new node
            carry = sum / 10;
            current->next = new ListNode(sum % 10);
            current = current->next;
        }
        
        // Handle any remaining carry
        if (carry > 0) {
            current->next = new ListNode(carry);
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
- Use a dummy node to simplify the code and avoid edge cases.
- Iterate through both linked lists simultaneously to add corresponding nodes.
- Handle any carry-over values by updating the carry and creating new nodes.