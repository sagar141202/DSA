# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The list nodes are defined as `ListNode(val=0, next=None)`. For example, the input `l1 = [2,4,3]` and `l2 = [5,6,4]` represents the numbers 342 and 465, respectively. The output should be `[7,0,8]`, which represents the number 807.

## Approach
The algorithm involves traversing both linked lists, adding corresponding nodes, and handling the carry-over value. We create a new linked list with the sum of the nodes from the input lists. If the sum exceeds 9, we carry over the excess to the next node.

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
        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        // Traverse both linked lists
        while (l1 || l2) {
            int x = (l1 != nullptr) ? l1->val : 0;
            int y = (l2 != nullptr) ? l2->val : 0;
            int sum = carry + x + y;
            
            // Update the carry-over value
            carry = sum / 10;
            
            // Create a new node with the sum
            current->next = new ListNode(sum % 10);
            current = current->next;
            
            // Move to the next nodes in the input lists
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        
        // Handle the remaining carry-over value
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
- Use a dummy node to simplify the code and avoid edge cases.
- Handle the carry-over value carefully to ensure accurate results.
- Traverse both linked lists simultaneously to add corresponding nodes.