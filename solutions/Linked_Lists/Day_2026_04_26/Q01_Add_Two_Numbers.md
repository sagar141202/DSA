# Add Two Numbers

## Problem Statement
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The sum of the two numbers should also be stored in reverse order. For example, given the input `l1 = [2,4,3]` and `l2 = [5,6,4]`, the output should be `[7,0,8]` because `342 + 465 = 807`. The input linked lists are guaranteed to be non-empty and the sum will not exceed the maximum limit of the integer.

## Approach
The solution involves iterating through both linked lists, adding corresponding nodes, and handling any carry-over values. We create a new linked list with the calculated sum and return it. This process continues until we have traversed both input linked lists. 

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
        // Initialize a dummy node to simplify the code and a carry variable
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;

        // Traverse both linked lists
        while (l1 || l2 || carry) {
            int sum = carry;
            // Add the current nodes' values if they exist
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            // Update the carry and create a new node with the sum
            carry = sum / 10;
            current->next = new ListNode(sum % 10);
            current = current->next;
        }

        // Return the next of the dummy node as the result
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
```

## Key Takeaways
- We use a dummy node to simplify the code and avoid dealing with special cases for the head of the result linked list.
- The time complexity is O(max(m, n)) where m and n are the lengths of the input linked lists, because we process each node once.
- The space complexity is also O(max(m, n)) for storing the result linked list.