# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at most 5000 nodes. The nodes will have unique values. The list should be sorted in-place, and the original nodes should be used to form the new sorted list.

## Approach
We can use the merge sort algorithm to sort the linked list. The algorithm works by recursively dividing the list into two halves until we have lists of size one, and then merging the lists back together in sorted order. This approach ensures that the list is sorted in ascending order.

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
        // Base case: if the list has 0 or 1 nodes, it is already sorted
        if (!head || !head->next) {
            return head;
        }

        // Find the middle of the list
        ListNode* mid = getMiddle(head);

        // Split the list into two halves
        ListNode* midNext = mid->next;
        mid->next = nullptr;

        // Recursively sort the two halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // Merge the two sorted halves
        return merge(left, right);
    }

    // Function to find the middle of the list
    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // Function to merge two sorted lists
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
        current->next = l1 ? l1 : l2;
        return dummy->next;
    }
};
```

## Test Cases
```
Input: [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

## Key Takeaways
- The merge sort algorithm is suitable for sorting linked lists because it can be implemented in-place and has a time complexity of O(n log n).
- The key to the merge sort algorithm is the merge step, where two sorted lists are merged into a single sorted list.
- The `getMiddle` function is used to find the middle of the list, and the `merge` function is used to merge two sorted lists.