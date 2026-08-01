# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 1-indexed. For example, if the input is `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the output should be `1 -> 3 -> 5 -> 2 -> 4 -> 6`. The relative order inside both the even and odd groups should remain as it was in the original list.

## Approach
The approach involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We then append the even list to the end of the odd list. We use two pointers to track the current nodes in both lists.

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
        if (!head->next->next) return head;

        // Initialize two pointers
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the list
        while (even && even->next) {
            // Update odd pointer
            odd->next = even->next;
            odd = odd->next;

            // Update even pointer
            even->next = odd->next;
            even = even->next;
        }

        // Append even list to the end of odd list
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
- We use two pointers to track the current nodes in the odd and even lists.
- We append the even list to the end of the odd list to get the final result.
- The time complexity is O(n), where n is the number of nodes in the linked list, because we traverse the list once.