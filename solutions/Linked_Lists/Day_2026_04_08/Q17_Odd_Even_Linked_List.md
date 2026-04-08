# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The first node is considered odd, and the second node is even, and so on. Note that the relative order inside both the even and odd groups should remain as it was in the original list. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5 -> 6, the output should be 1 -> 3 -> 5 -> 2 -> 4 -> 6. The input linked list will have at most 20000 nodes.

## Approach
We can solve this problem by maintaining two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We then connect the tail of the odd list to the head of the even list. This approach ensures that the relative order inside both the even and odd groups remains as it was in the original list.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
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

        // Initialize two pointers
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the linked list
        while (even != NULL && even->next != NULL) {
            // Update odd pointer
            odd->next = even->next;
            odd = odd->next;

            // Update even pointer
            even->next = odd->next;
            even = even->next;
        }

        // Connect the tail of the odd list to the head of the even list
        odd->next = evenHead;

        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 1 -> 3 -> 5 -> 2 -> 4 -> 6
Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7 -> 8 -> 9
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4 -> 8 -> 9
```

## Key Takeaways
- The problem can be solved in O(n) time complexity where n is the number of nodes in the linked list.
- We need to maintain two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes, to solve this problem efficiently.
- The relative order inside both the even and odd groups should remain as it was in the original list.