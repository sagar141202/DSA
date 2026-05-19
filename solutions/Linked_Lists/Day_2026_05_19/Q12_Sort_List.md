# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but it may have up to 5000 nodes. The nodes will have values ranging from -5000 to 5000. For example, given the linked list 4 -> 2 -> 1 -> 3, the output should be 1 -> 2 -> 3 -> 4.

## Approach
The approach is to use the merge sort algorithm to sort the linked list. This involves recursively splitting the list into two halves until each sublist has one node, and then merging the sublists in sorted order. The merge step involves comparing the values of the nodes and rearranging the pointers to create a sorted list.

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
        // Base case: if the list is empty or has one node, it is already sorted
        if (!head || !head->next) {
            return head;
        }

        // Split the list into two halves
        ListNode* mid = getMiddle(head);
        ListNode* midNext = mid->next;
        mid->next = nullptr;

        // Recursively sort the two halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // Merge the two sorted halves
        return merge(left, right);
    }

    // Helper function to get the middle of the list
    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // Helper function to merge two sorted lists
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
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
Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4
Input: -1 -> 5 -> 3 -> 4 -> 0
Output: -1 -> 0 -> 3 -> 4 -> 5
```

## Key Takeaways
- The merge sort algorithm is suitable for sorting linked lists because it has a time complexity of O(n log n) and only requires a small amount of extra memory.
- The key to implementing merge sort on a linked list is to use a recursive approach to split the list into smaller sublists, and then merge the sublists in sorted order.
- It's essential to handle the base case where the list is empty or has one node, as this is the terminating condition for the recursion.