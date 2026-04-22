# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but it may have up to 5000 nodes. The nodes will have values ranging from -5000 to 5000. For example, if the input is [4,2,1,3], the output should be [1,2,3,4].

## Approach
We can solve this problem by using the merge sort algorithm, which is a divide-and-conquer algorithm that splits the linked list into two halves, recursively sorts them, and then merges them. This approach ensures that the list is sorted in ascending order. We will use a recursive function to divide the list and a helper function to merge the sorted lists.

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
        // Base case: if the list is empty or contains only one node, it is already sorted
        if (!head || !head->next) return head;

        // Find the middle of the list
        ListNode* mid = getMiddle(head);
        ListNode* midNext = mid->next;

        // Split the list into two halves
        mid->next = nullptr;

        // Recursively sort the two halves
        ListNode* left = sortList(head);
        ListNode* right = sortList(midNext);

        // Merge the sorted halves
        return merge(left, right);
    }

    // Helper function to find the middle of the list
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
- The merge sort algorithm is suitable for sorting linked lists because it has a time complexity of O(n log n) and only requires a recursive function call stack of size O(log n).
- To find the middle of the list, we can use the slow and fast pointer technique, where the fast pointer moves twice as fast as the slow pointer.
- The merge function is used to merge two sorted lists into one sorted list.