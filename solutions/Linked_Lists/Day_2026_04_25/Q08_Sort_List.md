# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but no more than 500 nodes, and all nodes will have unique values. The list is guaranteed to be non-empty, and the values of the nodes will be between 1 and 500. For example, if the input is `[4,2,1,3]`, the output should be `[1,2,3,4]`.

## Approach
We will use the merge sort algorithm to solve this problem. The merge sort algorithm is a divide-and-conquer algorithm that works by splitting the list into two halves, sorting each half, and then merging the two sorted halves. This approach ensures that the list is sorted in ascending order.

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
        // Base case: if the list is empty or has only one node, it is already sorted
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

    // Function to get the middle of the list
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
        if (l1) {
            current->next = l1;
        } else if (l2) {
            current->next = l2;
        }
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
- The merge sort algorithm is suitable for sorting linked lists because it has a time complexity of O(n log n) and a space complexity of O(log n).
- To implement the merge sort algorithm for linked lists, we need to split the list into two halves, sort each half recursively, and then merge the two sorted halves.
- The merge step is crucial in the merge sort algorithm, and it requires careful handling of the pointers to ensure that the merged list is correctly sorted.