# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are 1-indexed. For example, if the input is `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the output should be `1 -> 3 -> 5 -> 2 -> 4 -> 6`. The relative order inside both the even and odd groups should remain as it was in the original list.

## Approach
The solution involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes, and then merging them. We iterate through the original list, appending nodes to the appropriate list based on their index. Finally, we connect the last node of the odd list to the first node of the even list.

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
        // Base case: if the list has 0 or 1 node, return it as it is
        if (!head || !head->next) return head;
        
        // Initialize two pointers for the odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Traverse the list
        while (even && even->next) {
            // Update the next pointer of the odd node to skip the even node
            odd->next = even->next;
            // Move the odd pointer two steps forward
            odd = odd->next;
            // Update the next pointer of the even node to skip the odd node
            even->next = odd->next;
            // Move the even pointer two steps forward
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
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 1 -> 3 -> 5 -> 2 -> 4 -> 6
Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

## Key Takeaways
- We use two pointers, `odd` and `even`, to traverse the list and separate the nodes into two lists.
- We update the `next` pointers of the nodes to connect them in the correct order.
- The time complexity is O(n), where n is the number of nodes in the list, because we make one pass through the list.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers.