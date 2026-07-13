# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The nodes of the linked list should also be in reverse order, and each node should contain a single digit. For example, given the linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the output should be 7 -> 0 -> 8, which represents the sum 342 + 465 = 807.

## Approach
The approach is to traverse both linked lists simultaneously, adding corresponding nodes and keeping track of the carry. We create a new linked list with the sum of the nodes and the carry. The algorithm iterates through the lists until all nodes have been processed.

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
            
            // Update the carry and create a new node
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
```

## Key Takeaways
- We use a dummy node to simplify the code and avoid edge cases.
- The time complexity is O(max(m, n)), where m and n are the lengths of the linked lists.
- The space complexity is O(max(m, n)) due to the creation of a new linked list.