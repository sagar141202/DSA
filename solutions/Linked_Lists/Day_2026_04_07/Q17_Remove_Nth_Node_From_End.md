# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is at least 1 and at most 30. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then the resulting list should be 1 -> 2 -> 3 -> 5. You may assume that the data type of each node is int.

## Approach
We use two pointers to traverse the linked list, with one pointer ahead of the other by n nodes. When the leading pointer reaches the end of the list, the trailing pointer will be at the nth node from the end. We then remove this node from the list.

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
        // Create two pointers
        ListNode* leading = head;
        ListNode* trailing = head;
        
        // Move the leading pointer n nodes ahead
        for (int i = 0; i < n; i++) {
            leading = leading->next;
        }
        
        // If the leading pointer is nullptr, remove the head node
        if (leading == nullptr) {
            return head->next;
        }
        
        // Move both pointers until the leading pointer reaches the end
        while (leading->next != nullptr) {
            leading = leading->next;
            trailing = trailing->next;
        }
        
        // Remove the nth node from the end
        trailing->next = trailing->next->next;
        
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
- Use two pointers to traverse the linked list with a gap of n nodes between them.
- When the leading pointer reaches the end of the list, the trailing pointer will be at the nth node from the end.
- Remove the nth node from the end by updating the next pointer of the trailing node.