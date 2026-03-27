# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The first node is considered odd, and the second node is even. The relative order inside both the even and odd groups should remain as it was in the original list. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The algorithm involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes, and then combining them. We initialize two dummy nodes, one for the odd list and one for the even list, to simplify the code and avoid edge cases. We then iterate through the original list, appending nodes to the odd or even list based on their index.

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
        
        // Initialize dummy nodes for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Iterate through the original list
        while (even && even->next) {
            // Update odd node's next pointer to skip even node
            odd->next = even->next;
            // Move odd pointer two steps forward
            odd = odd->next;
            // Update even node's next pointer to skip odd node
            even->next = odd->next;
            // Move even pointer two steps forward
            even = even->next;
        }
        
        // Combine odd and even lists
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
- We use two dummy nodes to simplify the code and avoid edge cases.
- We iterate through the original list, appending nodes to the odd or even list based on their index.
- We combine the odd and even lists by updating the next pointer of the last odd node to the first even node.