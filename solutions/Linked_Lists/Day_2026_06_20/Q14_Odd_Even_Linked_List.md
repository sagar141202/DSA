# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 1-indexed. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 3 -> 5 -> 2 -> 4. The relative order inside both the even and odd groups should remain as it was in the original list.

## Approach
The algorithm involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes, then concatenating them. We use two pointers to track the current nodes in the odd and even lists.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // Handle edge cases
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        // Initialize pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Traverse the list
        while (even != NULL && even->next != NULL) {
            // Update odd list
            odd->next = even->next;
            odd = odd->next;
            
            // Update even list
            even->next = odd->next;
            even = even->next;
        }
        
        // Concatenate odd and even lists
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
- We use two pointers, `odd` and `even`, to track the current nodes in the odd and even lists.
- The `evenHead` pointer is used to keep track of the head of the even list, which is used to concatenate the odd and even lists at the end.
- The time complexity is O(n), where n is the number of nodes in the linked list, because we traverse the list once.