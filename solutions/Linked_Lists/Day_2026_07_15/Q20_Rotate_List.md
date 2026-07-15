# Rotate List

## Problem Statement
Given the head of a list and an integer k, rotate the list to the right by k places. The list is considered rotated if each element is shifted k places to the right, with the last k elements wrapping around to the beginning of the list. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and k = 2, the rotated list should be 4 -> 5 -> 1 -> 2 -> 3. The list can have up to 5000 nodes, and k can range from 0 to 5000.

## Approach
To rotate the list, we can first find the length of the list and connect the last node to the head to form a circular list. Then, we can find the new tail node by moving (length - k % length - 1) steps from the head. Finally, we can break the circular list at the new tail node to get the rotated list.

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
        // base case: if the list is empty or only has one node, return the head
        if (!head || !head->next) return head;
        
        // find the length of the list and the last node
        ListNode* last = head;
        int length = 1;
        while (last->next) {
            last = last->next;
            length++;
        }
        
        // connect the last node to the head to form a circular list
        last->next = head;
        
        // find the new tail node
        int newTailIndex = length - k % length - 1;
        ListNode* newTail = head;
        for (int i = 0; i < newTailIndex; i++) {
            newTail = newTail->next;
        }
        
        // find the new head node
        ListNode* newHead = newTail->next;
        
        // break the circular list at the new tail node
        newTail->next = nullptr;
        
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
- We can use a circular list to simplify the rotation process.
- The new tail node is (length - k % length - 1) steps away from the head.
- We need to break the circular list at the new tail node to get the rotated list.