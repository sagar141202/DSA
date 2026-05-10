# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= Node.val <= 100. 0 <= k <= 105. It is guaranteed that the number of nodes in the list is in the range [0, 100]. 

## Approach
To solve this problem, we can first find the length of the linked list and connect the tail to the head to form a circular linked list. Then, we can find the new tail of the rotated list by moving (length - k % length - 1) steps from the head. Finally, we can break the circular linked list at the new tail and return the new head.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        // base cases
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // find the length of the linked list and the tail
        ListNode* tail = head;
        int length = 1;
        while (tail->next) {
            tail = tail->next;
            length++;
        }
        
        // connect the tail to the head to form a circular linked list
        tail->next = head;
        
        // find the new tail of the rotated list
        int newTailIndex = length - k % length - 1;
        ListNode* newTail = head;
        for (int i = 0; i < newTailIndex; i++) {
            newTail = newTail->next;
        }
        
        // find the new head of the rotated list
        ListNode* newHead = newTail->next;
        
        // break the circular linked list at the new tail
        newTail->next = nullptr;
        
        return newHead;
    }
};
```

## Test Cases
```
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
```

## Key Takeaways
- The key to solving this problem is to first find the length of the linked list and connect the tail to the head to form a circular linked list.
- By doing so, we can avoid dealing with edge cases such as when k is larger than the length of the linked list.
- The new tail of the rotated list can be found by moving (length - k % length - 1) steps from the head.