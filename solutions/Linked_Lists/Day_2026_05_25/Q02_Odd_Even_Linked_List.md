# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, rearrange the nodes to alternate between the nodes that were originally at odd indices and the nodes that were originally at even indices. The rearranged list should still be a singly linked list, and the relative order of the nodes at odd and even indices should be preserved. For example, if the original list is 1 -> 2 -> 3 -> 4 -> 5, the rearranged list should be 1 -> 3 -> 2 -> 5 -> 4.

## Approach
The algorithm involves creating two separate linked lists, one for odd indices and one for even indices, and then merging them. We iterate through the original list, appending nodes to the odd and even lists based on their indices. Finally, we connect the last node of the odd list to the first node of the even list.

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
        if (!head) return head;
        
        // Initialize two pointers for the odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Iterate through the list, separating nodes into odd and even lists
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        
        // Connect the last node of the odd list to the first node of the even list
        odd->next = evenHead;
        
        return head;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: [1, 3, 2, 5, 4]
Input: [2, 1, 3, 5, 6, 4, 7]
Output: [2, 3, 1, 7, 5, 6, 4]
```

## Key Takeaways
- We can solve this problem by creating two separate linked lists for odd and even indices and then merging them.
- The time complexity is O(n), where n is the number of nodes in the linked list, because we only iterate through the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers.