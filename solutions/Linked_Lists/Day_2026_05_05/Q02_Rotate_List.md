# Rotate List

## Problem Statement
Given the head of a linked list, rotate the list to the right by k places. The number of nodes in the list is in the range [0, 100]. 0 <= k <= 105. It is guaranteed that the number of nodes in the list is in the range [0, 100], so there's no risk of an overflow when calculating the actual number of places to rotate (i.e., k % n, where n is the number of nodes). For example, if we have a list 1->2->3->4->5 and k = 2, the rotated list should be 4->5->1->2->3.

## Approach
To solve this problem, we first calculate the length of the linked list. Then we connect the last node to the head to form a circular linked list. We calculate the new tail's position by subtracting k % n from the length of the list, where n is the length of the list. The new head will be the node next to the new tail.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
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
    ListNode* rotateRight(ListNode* head, int k) {
        // base cases
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        // calculate the length of the list
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n += 1;
        }
        
        // connect the list to form a ring
        old_tail->next = head;
        
        // find new tail : (n - k % n - 1)th node
        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++) {
            new_tail = new_tail->next;
        }
        
        // find new head : (n - k % n)th node
        ListNode* new_head = new_tail->next;
        
        // break the ring at the new tail
        new_tail->next = nullptr;
        
        return new_head;
    }
};
```

## Test Cases
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Input: head = [1,2,3,4,5], k = 5
Output: [1,2,3,4,5]
```

## Key Takeaways
- To rotate a linked list to the right by k places, we can connect the list to form a ring and then find the new head and tail.
- The new tail is the (n - k % n - 1)th node, where n is the length of the list.
- The new head is the (n - k % n)th node.