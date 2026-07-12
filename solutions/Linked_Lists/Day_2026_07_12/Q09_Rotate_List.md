# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, meaning the last node is connected to the first node. If k is greater than the length of the list, the rotation is done by k mod n, where n is the length of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
To solve this problem, we first need to find the length of the list and connect the last node to the first node. Then, we find the new tail node by moving (n - k % n - 1) steps from the head. We then break the list at the new tail node and move the new head to the next node of the new tail.

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
        // Base case: if the list is empty or only contains one node
        if (!head || !head->next) return head;

        // Find the length of the list and the last node
        ListNode* old_tail = head;
        int n = 1;
        while (old_tail->next) {
            old_tail = old_tail->next;
            n++;
        }

        // Connect the last node to the first node
        old_tail->next = head;

        // Find the new tail node
        ListNode* new_tail = head;
        for (int i = 0; i < (n - k % n - 1); i++) {
            new_tail = new_tail->next;
        }

        // Find the new head node
        ListNode* new_head = new_tail->next;

        // Break the list at the new tail node
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
- The key to solving this problem is to first connect the last node to the first node to form a circular list.
- We then find the new tail node by moving (n - k % n - 1) steps from the head.
- Finally, we break the list at the new tail node and return the new head node.