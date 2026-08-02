# Sort List

## Problem Statement
Given the head of a linked list, sort it in ascending order and return the sorted list. The linked list will have at least one node, but it may have up to 5000 nodes. The nodes will have values ranging from -5000 to 5000.

## Approach
We will use the merge sort algorithm to sort the linked list. This algorithm works by recursively splitting the list into two halves until each half has only one node, and then merging these halves back together in sorted order.

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
        if (!head || !head->next) return head;

        // Split the list into two halves
        ListNode* mid = getMiddle(head);
        ListNode* midNext = mid->next;

        // Split the list at the middle node
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
- Merge sort is a suitable algorithm for sorting linked lists because it has a time complexity of O(n log n) and can be implemented recursively.
- To implement merge sort on a linked list, we need to split the list into two halves, recursively sort each half, and then merge the two sorted halves back together.
- The merge step is the key to the merge sort algorithm, and it can be implemented using a simple iterative approach.