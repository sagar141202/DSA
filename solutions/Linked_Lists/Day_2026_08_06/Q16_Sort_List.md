# Sort List

## Problem Statement
Given the head of a linked list, sort it in ascending order and return the sorted list's head. The linked list will have at least one node, but it may have up to 5000 nodes. The nodes' values will range from -5000 to 5000. For example, if the input list is 4 -> 2 -> 1 -> 3, the output should be 1 -> 2 -> 3 -> 4.

## Approach
We will use the merge sort algorithm to sort the linked list, as it is a stable sorting algorithm that works well with linked lists. The list is divided into two halves, each half is sorted recursively, and then the two sorted halves are merged. This approach ensures that the list is sorted in ascending order.

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
        // Base case: if the list has 0 or 1 node, it is already sorted
        if (!head || !head->next) {
            return head;
        }

        // Split the list into two halves
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* second = slow->next;
        slow->next = nullptr;

        // Recursively sort the two halves
        ListNode* first = sortList(head);
        second = sortList(second);

        // Merge the two sorted halves
        return merge(first, second);
    }

    ListNode* merge(ListNode* first, ListNode* second) {
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        while (first && second) {
            if (first->val < second->val) {
                current->next = first;
                first = first->next;
            } else {
                current->next = second;
                second = second->next;
            }
            current = current->next;
        }
        if (first) {
            current->next = first;
        } else {
            current->next = second;
        }
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};
```

## Test Cases
```
Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4
```

## Key Takeaways
- Merge sort is a suitable algorithm for sorting linked lists.
- The key to implementing merge sort on linked lists is to correctly split the list into two halves and merge the sorted halves.
- The recursive approach allows for efficient sorting of large linked lists.