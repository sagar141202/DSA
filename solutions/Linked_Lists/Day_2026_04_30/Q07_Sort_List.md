# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at most 2 * 10^5 nodes, and each node's value will be between -10^5 and 10^5. The list is guaranteed to be non-empty. For example, given the list 4 -> 2 -> 1 -> 3, the sorted list would be 1 -> 2 -> 3 -> 4.

## Approach
We will use the merge sort algorithm to sort the linked list. This involves dividing the list into two halves, sorting each half, and then merging the sorted halves. The merge step involves creating a new list that contains the nodes from the two sorted halves in sorted order.

## Complexity
- Time: O(n log n)
- Space: O(log n)

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
    ListNode* sortList(ListNode* head) {
        // base case: if the list has 0 or 1 nodes, it is already sorted
        if (!head || !head->next) return head;

        // divide the list into two halves
        ListNode* mid = getMiddle(head);
        ListNode* midNext = mid->next;

        // break the list at the middle node
        mid->next = nullptr;

        // recursively sort the two halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // merge the sorted halves
        return merge(left, right);
    }

    // function to get the middle of the linked list
    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // function to merge two sorted linked lists
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                curr->next = l1;
                l1 = l1->next;
            } else {
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;
        }
        // append the remaining nodes, if any
        if (l1) curr->next = l1;
        if (l2) curr->next = l2;
        return dummy->next;
    }
};
```

## Test Cases
```
Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4

Input: -1 -> 5 -> 3 -> 4 -> 0
Output: -1 -> 0 -> 3 -> 4 -> 5
```

## Key Takeaways
- The merge sort algorithm is well-suited for sorting linked lists because it has a time complexity of O(n log n) and can be implemented recursively.
- The key to implementing merge sort on a linked list is to divide the list into two halves and then merge the sorted halves.
- The merge step involves creating a new list that contains the nodes from the two sorted halves in sorted order.