# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The list nodes are defined as `ListNode(val=0, next=None)`. For example, the input `l1 = [2,4,3]` and `l2 = [5,6,4]` represents the numbers 342 and 465, respectively. The output for this example should be `[7,0,8]`, which represents the number 807.

## Approach
The algorithm iterates through both linked lists simultaneously, adding corresponding nodes together along with any carry from the previous addition. A new linked list is created with the results of these additions.

## Complexity
- Time: O(max(m, n))
- Space: O(max(m, n))

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Initialize a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        // Iterate through both linked lists
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int sum = 0;
            // Add values from l1 and l2 if they exist
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            // Add the carry
            sum += carry;
            // Update the carry
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
- To handle the addition of two linked lists, we iterate through both lists simultaneously.
- We use a dummy node to simplify the code for creating a new linked list.
- The carry from one addition is used in the next iteration to ensure accurate results.