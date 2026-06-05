# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list should be sorted using the merge sort algorithm. The number of nodes in the list is in the range [0, 5 * 10^4]. The nodes have values in the range [-10^5, 10^5]. The list is guaranteed to be non-empty.

## Approach
The approach is to use the merge sort algorithm to sort the linked list. This involves splitting the list into two halves, recursively sorting each half, and then merging the sorted halves. The merge step involves comparing nodes from each half and adding the smaller one to the result list.

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
        // Base case: if the list is empty or only has one node, it is already sorted
        if (!head || !head->next) return head;

        // Split the list into two halves
        ListNode* mid = getMiddle(head);
        ListNode* midNext = mid->next;

        // Split the list at the middle node
        mid->next = nullptr;

        // Recursively sort the two halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // Merge the sorted halves
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
        // If there are remaining nodes in either list, append them to the result
        curr->next = l1 ? l1 : l2;
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
- The merge sort algorithm is suitable for sorting linked lists because it can be implemented recursively and only requires a small amount of extra memory for the recursive call stack.
- The merge step is the key to the merge sort algorithm, and it involves comparing nodes from each half of the list and adding the smaller one to the result list.
- The time complexity of the merge sort algorithm is O(n log n), making it efficient for large lists.