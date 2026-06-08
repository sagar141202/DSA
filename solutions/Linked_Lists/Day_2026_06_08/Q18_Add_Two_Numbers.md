# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers should also be in reverse order, with each node containing a single digit. The input linked lists may have different lengths, and it is guaranteed that the sum of the two numbers will not have more than 1000 digits. For example, given two linked lists `2 -> 4 -> 3` and `5 -> 6 -> 4`, the sum would be `7 -> 0 -> 8`, which corresponds to 342 + 465 = 807.

## Approach
The algorithm involves traversing both linked lists simultaneously, adding corresponding nodes, and handling any carry-over values. We create a new linked list with the sum of the nodes, taking into account any carry from the previous addition. The process continues until all nodes in both lists have been processed.

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
            int x = (l1) ? l1->val : 0;
            int y = (l2) ? l2->val : 0;
            int sum = carry + x + y;
            
            // Update carry and create a new node with the sum
            carry = sum / 10;
            current->next = new ListNode(sum % 10);
            current = current->next;
            
            // Move to the next nodes in both lists
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        
        // Return the next node of the dummy node
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
- Traverse both linked lists simultaneously, adding corresponding nodes and handling any carry-over values.
- Create a new linked list with the sum of the nodes, taking into account any carry from the previous addition.