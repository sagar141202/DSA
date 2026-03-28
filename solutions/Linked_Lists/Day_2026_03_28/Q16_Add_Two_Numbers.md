# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The input linked lists can have different lengths, and you should handle the case where one list is longer than the other. For example, given the input `l1 = [2,4,3]` and `l2 = [5,6,4]`, the output should be `[7,0,8]`, which represents the sum of the two numbers.

## Approach
We will create a new linked list where each node is the sum of the corresponding nodes in the input lists. We will handle the carry-over value by adding it to the sum of the next pair of nodes. This approach ensures that we can efficiently add the two numbers represented by the linked lists.

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
        // Initialize a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;

        // Iterate over the linked lists
        while (l1 || l2 || carry) {
            // Calculate the sum of the current nodes
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

        // Return the next node of the dummy node
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
- We use a dummy node to simplify the code and avoid special cases for the head of the result list.
- We iterate over the linked lists and calculate the sum of the current nodes, handling the carry-over value.
- We create a new node for each sum and update the carry for the next iteration.