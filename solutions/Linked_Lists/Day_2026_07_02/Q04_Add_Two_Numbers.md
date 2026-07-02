# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The nodes of the linked lists should still have a single digit, so if the sum of two digits is greater than 9, then the extra digit should be carried over to the next node. For example, given the linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8.

## Approach
We will create a new linked list to store the sum of the input linked lists. We'll iterate through both linked lists, adding corresponding nodes and keeping track of any carry-over value. The algorithm will handle cases where the linked lists are of different lengths.

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
        ListNode* dummy = new ListNode();
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
            
            // Update carry and create a new node
            carry = sum / 10;
            current->next = new ListNode(sum % 10);
            current = current->next;
        }
        
        // Handle remaining carry
        if (carry > 0) {
            current->next = new ListNode(carry);
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
- The algorithm handles linked lists of different lengths by checking for nullptr in the iteration loop.
- A dummy node simplifies the code by avoiding special cases for the head of the result linked list.
- The carry-over value is updated at each step to handle cases where the sum of two digits is greater than 9.