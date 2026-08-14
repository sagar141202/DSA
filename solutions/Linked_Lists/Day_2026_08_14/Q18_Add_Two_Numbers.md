# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers should also be stored in reverse order, and each node should contain a single digit. For example, if the input is `l1 = [2,4,3]` and `l2 = [5,6,4]`, the output should be `[7,0,8]` because `342 + 465 = 807`. The input linked lists can have different lengths, and it is guaranteed that the sum of the two numbers will not have more than 1000 digits.

## Approach
We will use a simple iterative approach, traversing both linked lists at the same time and adding corresponding nodes. We will also keep track of the carry from the previous addition.

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
        // Create a dummy node to simplify some corner cases
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        // Traverse both linked lists
        while (l1 || l2 || carry) {
            int sum = carry;
            // Add values from l1 and l2 if they exist
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            // Update carry and current node's value
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
- We can use a dummy node to simplify the code and avoid dealing with special cases for the head of the list.
- It's essential to keep track of the carry from the previous addition to ensure accurate results.
- The time complexity is O(max(m, n)), where m and n are the lengths of the input linked lists, because we only traverse each list once.