# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, and 1 <= n <= sz. The solution should have a time complexity of O(L), where L is the length of the list, and a space complexity of O(1). For example, given the list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, the output should be 1 -> 2 -> 3 -> 5.

## Approach
We will use two pointers to traverse the linked list, maintaining a distance of n nodes between them. When the leading pointer reaches the end of the list, the trailing pointer will be at the node before the nth node from the end. We can then remove the nth node from the end by updating the next pointer of the trailing pointer.

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
        // Initialize two pointers, p1 and p2, to the head of the list
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p1 n steps ahead
        for (int i = 0; i < n; i++) {
            p1 = p1->next;
        }
        
        // If p1 is nullptr, it means we need to remove the head
        if (p1 == nullptr) {
            return head->next;
        }
        
        // Move both pointers until p1 reaches the end of the list
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
- Use two pointers to maintain a distance of n nodes and traverse the linked list.
- When the leading pointer reaches the end of the list, the trailing pointer will be at the node before the nth node from the end.
- Update the next pointer of the trailing pointer to remove the nth node from the end.