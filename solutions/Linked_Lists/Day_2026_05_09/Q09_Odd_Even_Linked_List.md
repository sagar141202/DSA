# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are **0-indexed**. For example, if the input is `1 -> 2 -> 3 -> 4 -> 5`, then the output should be `1 -> 3 -> 5 -> 2 -> 4`. If the input is `2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7`, then the output should be `2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4`.

## Approach
The approach to solve this problem involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We then merge these two lists to get the final result. We use two pointers to keep track of the current nodes in the odd and even lists.

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
        // Base cases
        if (!head || !head->next || !head->next->next) {
            return head;
        }
        
        // Initialize two pointers
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
        
        // Merge the two lists
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
- We use two pointers to keep track of the current nodes in the odd and even lists.
- We merge the two lists by updating the `next` pointer of the last node in the odd list to the head of the even list.
- The time complexity is O(n) because we are traversing the linked list once, and the space complexity is O(1) because we are not using any extra space.