# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but it may have up to 5000 nodes. Each node has a unique value ranging from -5000 to 5000. The list is singly linked, meaning each node only points to the next node.

## Approach
We will use the merge sort algorithm to sort the linked list. This involves dividing the list into two halves, recursively sorting each half, and then merging the sorted halves. The merge step involves comparing the values of the nodes in the two halves and rearranging them in ascending order.

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
        // base case: if the list has 0 or 1 node, it is already sorted
        if (!head || !head->next) return head;

        // find the middle of the list
        ListNode* mid = getMiddle(head);

        // split the list into two halves
        ListNode* midNext = mid->next;
        mid->next = nullptr;

        // recursively sort the two halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // merge the sorted halves
        return merge(left, right);
    }

    // function to find the middle of the list
    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // function to merge two sorted lists
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        if (l1) current->next = l1;
        if (l2) current->next = l2;
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
- The merge sort algorithm is suitable for sorting linked lists because it can be implemented recursively and has a time complexity of O(n log n).
- The getMiddle function is used to find the middle of the list, which is necessary for splitting the list into two halves.
- The merge function is used to merge two sorted lists into one sorted list.