# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, and sz is within the range [1, 30]. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then the resulting list should be 1 -> 2 -> 3 -> 5. The constraint is that we cannot modify the node's value and only have access to the node itself.

## Approach
We use two pointers, p1 and p2, to traverse the linked list. p1 is nth nodes ahead of p2. When p1 reaches the end of the list, p2 will be at the node right before the one we want to remove. We then remove the nth node from the end by updating the next pointer of p2.

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
        // Initialize two pointers, p1 and p2
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p1 nth nodes ahead of p2
        for (int i = 0; i < n; i++) {
            p1 = p1->next;
        }
        
        // If p1 is nullptr, it means we need to remove the head
        if (p1 == nullptr) {
            return head->next;
        }
        
        // Move both pointers until p1 reaches the end
        while (p1->next != nullptr) {
            p1 = p1->next;
            p2 = p2->next;
        }
        
        // Remove the nth node from the end
        p2->next = p2->next->next;
        
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
- Use two pointers to solve linked list problems involving removal or insertion of nodes.
- Always consider edge cases, such as removing the head or the last node of the list.
- Be careful with pointer updates to avoid losing track of nodes in the list.