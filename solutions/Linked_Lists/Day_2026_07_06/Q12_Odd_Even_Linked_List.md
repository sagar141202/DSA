# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, separate the nodes into two lists: one containing the nodes from the odd positions (1-indexed) and the other containing the nodes from the even positions (1-indexed). Then, combine these two lists to form a new linked list, with the nodes from the odd list first, followed by the nodes from the even list. The resulting linked list should be returned.

## Approach
The algorithm involves initializing two pointers to keep track of the odd and even lists. It iterates through the original list, separating the nodes into two lists based on their positions. Finally, it combines the two lists.

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
    ListNode* oddEvenList(ListNode* head) {
        // Handle edge cases
        if (!head) return head;
        if (!head->next) return head;
        if (!head->next->next) return head;
        
        // Initialize pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Traverse the linked list
        while (even && even->next) {
            // Update odd pointer
            odd->next = even->next;
            odd = odd->next;
            
            // Update even pointer
            even->next = odd->next;
            even = even->next;
        }
        
        // Combine the odd and even lists
        odd->next = evenHead;
        
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 5 -> 2 -> 4
Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

## Key Takeaways
- Use two pointers to separate the nodes into odd and even lists.
- Combine the two lists by updating the next pointer of the last node in the odd list.
- The time complexity is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) since we only use a constant amount of space.