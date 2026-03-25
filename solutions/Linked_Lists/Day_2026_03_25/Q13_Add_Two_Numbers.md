# Add Two Numbers

## Problem Statement
Given two non-empty linked lists representing two non-negative integers, where each node represents a digit and the digits are stored in reverse order. The task is to add the two numbers and return the sum as a linked list. Each node in the linked list has a value between 0 and 9, and the list is guaranteed to be non-empty. For example, given the linked lists 2 -> 4 -> 3 and 5 -> 6 -> 4, the sum would be 7 -> 0 -> 8, which corresponds to the number 807.

## Approach
The algorithm involves iterating through both linked lists simultaneously, adding corresponding nodes, and handling any carry-over values. We create a new linked list to store the sum of the two input lists. The iteration continues until all nodes in both lists have been processed.

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
        // Create a dummy node to simplify some corner cases
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
            
            // Update carry and create a new node with the digit value
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
- Use a dummy node to simplify corner cases such as when one list is longer than the other or when there's a carry-over after processing all nodes.
- Iterate through both linked lists simultaneously, adding corresponding nodes and handling any carry-over values.
- Create a new linked list to store the sum of the two input lists, and return the next node of the dummy node as the result.