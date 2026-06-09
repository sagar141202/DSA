# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indexes in this list are 1-indexed. For example, if the input is `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the output will be `1 -> 3 -> 5 -> 2 -> 4 -> 6`. The relative order inside both the even and odd groups should remain as it was in the original list.

## Approach
The algorithm involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We then merge these two lists to get the final result. This approach ensures that the nodes are rearranged according to their indices while maintaining their relative order within their respective groups.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
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
        
        // Initialize pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Traverse the list and separate nodes into odd and even lists
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        
        // Connect the odd list to the even list
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
- We use two pointers, `odd` and `even`, to keep track of the current nodes in the odd and even lists.
- The `evenHead` pointer is used to keep track of the head of the even list, which will be connected to the end of the odd list at the end.
- The algorithm has a time complexity of O(n), where n is the number of nodes in the list, since we only traverse the list once. The space complexity is O(1) since we only use a constant amount of space to store the pointers.