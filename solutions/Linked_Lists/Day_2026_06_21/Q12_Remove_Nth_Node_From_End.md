# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is at least n. sz and n are both integers, and 1 <= n <= sz. The problem requires finding and removing the nth node from the end of the linked list. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5 and n = 2, the output should be 1 -> 2 -> 3 -> 5.

## Approach
The approach is to use two pointers, both starting at the head of the list. The first pointer moves n steps ahead, and then both pointers move one step at a time until the first pointer reaches the end of the list. At this point, the second pointer is at the node right before the nth node from the end, allowing us to remove the nth node.

## Complexity
- Time: O(L)
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Initialize two pointers, both at the head
        ListNode* first = head;
        ListNode* second = head;
        
        // Move the first pointer n steps ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If the first pointer is nullptr, it means we need to remove the head
        if (first == nullptr) {
            return head->next;
        }
        
        // Move both pointers one step at a time until the first pointer reaches the end
        while (first->next != nullptr) {
            first = first->next;
            second = second->next;
        }
        
        // Remove the nth node from the end
        second->next = second->next->next;
        
        return head;
    }
};
```

## Test Cases
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Input: head = [1], n = 1
Output: []
Input: head = [1,2], n = 1
Output: [1]
```

## Key Takeaways
- We can use two pointers to solve this problem efficiently, with one pointer moving n steps ahead of the other.
- The time complexity is O(L), where L is the length of the linked list, because we only traverse the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the two pointers.