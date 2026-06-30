# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but it may have up to 5000 nodes. The nodes will have values ranging from -5000 to 5000. For example, given the linked list `4 -> 2 -> 1 -> 3`, the function should return the sorted linked list `1 -> 2 -> 3 -> 4`.

## Approach
The approach to solve this problem is to use the merge sort algorithm, which is a divide-and-conquer algorithm that splits the linked list into two halves, recursively sorts each half, and then merges the two sorted halves. This algorithm is suitable for linked lists because it only requires sequential access to the nodes.

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
        // base case: if the list is empty or only has one node, it is already sorted
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // find the middle of the list
        ListNode* mid = getMiddle(head);

        // split the list into two halves
        ListNode* midNext = mid->next;
        mid->next = nullptr;

        // recursively sort each half
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // merge the two sorted halves
        return merge(left, right);
    }

    // helper function to find the middle of the list
    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // helper function to merge two sorted lists
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val < l2->val) {
                curr->next = l1;
                l1 = l1->next;
            } else {
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;
        }
        if (l1 != nullptr) {
            curr->next = l1;
        } else if (l2 != nullptr) {
            curr->next = l2;
        }
        return dummy->next;
    }
};
```

## Test Cases
```
Input: [4, 2, 1, 3]
Output: [1, 2, 3, 4]
Input: [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]
```

## Key Takeaways
- The merge sort algorithm is a suitable choice for sorting linked lists because it only requires sequential access to the nodes.
- The time complexity of the merge sort algorithm is O(n log n), making it efficient for large lists.
- The space complexity of the merge sort algorithm is O(log n), which is relatively low compared to other sorting algorithms.