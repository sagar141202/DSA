# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are 1-indexed. For example, given the linked list `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the modified list would be `1 -> 3 -> 5 -> 2 -> 4 -> 6`. The relative order inside both the even and odd groups should remain as it was in the original list.

## Approach
The solution involves creating two separate linked lists: one for odd-indexed nodes and one for even-indexed nodes. We then append the even list to the end of the odd list. This approach ensures that the odd-indexed nodes come first, followed by the even-indexed nodes.

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
        
        // Initialize two pointers
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Traverse the list
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        
        // Append the even list to the end of the odd list
        odd->next = evenHead;
        
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 1 -> 3 -> 5 -> 2 -> 4 -> 6

Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

## Key Takeaways
- We need to handle edge cases where the list is empty or has only one node.
- We use two pointers, `odd` and `even`, to traverse the list and group the nodes accordingly.
- The `evenHead` pointer is used to keep track of the start of the even list, which is then appended to the end of the odd list.