# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. Each node contains a single digit, and the nodes are stored in reverse order. For example, the input `2 -> 4 -> 3` represents the number `342`. The input `5 -> 6 -> 4` represents the number `465`. The output for these inputs should be `7 -> 0 -> 8`, which represents the number `807`.

## Approach
We will use a simple iterative approach to solve this problem, where we traverse both linked lists simultaneously, add the corresponding nodes, and handle the carry-over value. We will create a new linked list to store the result.

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
            int sum = carry;
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            
            // Update the carry value
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
- Always consider using a dummy node to simplify the code when working with linked lists.
- Don't forget to handle the carry-over value when adding numbers.
- The time complexity is O(max(m, n)), where m and n are the lengths of the input linked lists.