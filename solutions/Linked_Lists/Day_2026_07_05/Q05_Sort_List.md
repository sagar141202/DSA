# Sort List

## Problem Statement
Given the head of a linked list, sort it in ascending order and return the sorted list's head. The linked list will have at least one node, but it may have up to 5000 nodes. The values of the nodes will be between -5000 and 5000. For example, if the input is [4,2,1,3], the output should be [1,2,3,4]. If the input is [-1,5,3,4,0], the output should be [-1,0,3,4,5].

## Approach
We will use the merge sort algorithm to sort the linked list. This algorithm works by recursively dividing the list into two halves until we have sublists of size one, and then merging these sublists in sorted order. The merge step will compare nodes from the two sublists and add the smaller one to the result list.

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

        // If there are remaining nodes in either list, append them to the result
        if (l1) current->next = l1;
        if (l2) current->next = l2;

        return dummy->next;
    }
};
```

## Test Cases
```
Input: [4,2,1,3]
Output: [1,2,3,4]
Input: [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

## Key Takeaways
- The merge sort algorithm is suitable for sorting linked lists because it only requires sequential access to the nodes.
- The time complexity of merge sort is O(n log n) because the list is recursively divided in half until we have sublists of size one, and then merged in sorted order.
- The space complexity of merge sort is O(log n) because the recursive calls to sort the two halves of the list require a stack of maximum depth log n.