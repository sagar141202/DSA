# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list should be sorted using the merge sort algorithm. The number of nodes in the list is in the range [0, 5 * 10^4]. The nodes have values in the range [-10^5, 10^5].

## Approach
We can solve this problem by implementing the merge sort algorithm, a divide-and-conquer technique that splits the linked list into two halves, recursively sorts them, and merges them back together in sorted order. This approach ensures a time complexity of O(n log n). The merge step involves comparing nodes from the two sorted halves and appending the smaller one to the result list.

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
        // Base case: if the list has 0 or 1 node, it's already sorted
        if (!head || !head->next) return head;

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

    // Helper function to find the middle of the linked list
    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // Helper function to merge two sorted linked lists
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
        // Append the remaining nodes, if any
        current->next = l1 ? l1 : l2;
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
- The merge sort algorithm is suitable for sorting linked lists because it has a time complexity of O(n log n) and only requires a small amount of extra memory for the recursive calls.
- The key to implementing merge sort for linked lists is to split the list into two halves, recursively sort them, and merge them back together in sorted order.
- The merge step involves comparing nodes from the two sorted halves and appending the smaller one to the result list.