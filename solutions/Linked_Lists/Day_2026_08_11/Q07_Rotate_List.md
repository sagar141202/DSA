# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered to be a circular list, so if k is greater than the length of the list, we can take the modulus of k with the length of the list to get the effective number of rotations. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list will be 4 -> 5 -> 1 -> 2 -> 3.

## Approach
We can solve this problem by first finding the length of the list and the last node of the list. Then, we connect the last node to the head to form a circular list. We calculate the effective number of rotations by taking the modulus of k with the length of the list. We then find the new last node and the new head of the rotated list.

## Complexity
- Time: O(n)
- Space: O(1)

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
    ListNode* rotateRight(ListNode* head, int k) {
        // Base cases
        if (!head || !head->next || k == 0) {
            return head;
        }

        // Find the length of the list and the last node
        ListNode* current = head;
        int length = 1;
        while (current->next) {
            current = current->next;
            length++;
        }

        // Connect the last node to the head to form a circular list
        current->next = head;

        // Calculate the effective number of rotations
        k = k % length;

        // Find the new last node and the new head of the rotated list
        ListNode* newLast = head;
        for (int i = 0; i < length - k - 1; i++) {
            newLast = newLast->next;
        }

        // Find the new head of the rotated list
        ListNode* newHead = newLast->next;

        // Break the circular list at the new last node
        newLast->next = nullptr;

        return newHead;
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
- The key to solving this problem is to first find the length of the list and the last node, and then connect the last node to the head to form a circular list.
- We can calculate the effective number of rotations by taking the modulus of k with the length of the list.
- We can find the new last node and the new head of the rotated list by traversing the circular list.