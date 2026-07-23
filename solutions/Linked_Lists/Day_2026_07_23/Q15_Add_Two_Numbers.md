# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of two numbers should also have its digits stored in reverse order, and each node should contain a single digit. For example, given the linked lists `2 -> 4 -> 3` and `5 -> 6 -> 4`, the output should be `7 -> 0 -> 8` because `342 + 465 = 807`.

## Approach
We can solve this problem by iterating over the two linked lists and adding corresponding nodes together. We'll also keep track of any carry-over value from the previous addition. This approach will allow us to efficiently calculate the sum of the two numbers represented by the linked lists.

## Complexity
- Time: O(max(m, n))
- Space: O(max(m, n))

## C++ Solution
```cpp
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

        // Iterate over the two linked lists
        while (l1 != NULL || l2 != NULL) {
            int x = (l1 != NULL) ? l1->val : 0;
            int y = (l2 != NULL) ? l2->val : 0;
            int sum = carry + x + y;
            carry = sum / 10;

            // Create a new node with the digit value
            current->next = new ListNode(sum % 10);
            current = current->next;

            // Move to the next nodes in the linked lists
            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next;
        }

        // Handle any remaining carry-over value
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
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special cases for the head of the result linked list.
- Keep track of the carry-over value from the previous addition to correctly calculate the sum of the two numbers.
- Create a new node for each digit in the result linked list to store the sum of the corresponding nodes from the input linked lists.