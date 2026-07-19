# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but it may have up to 5000 nodes. Each node has a unique value ranging from -5000 to 5000. The list is not guaranteed to be sorted, and it may contain duplicates.

## Approach
We will use the merge sort algorithm to sort the linked list, as it is a stable and efficient sorting algorithm for linked lists. The merge sort algorithm works by recursively dividing the list into two halves until we have sublists of size one, and then merging the sublists back together in sorted order.

## Complexity
- Time: O(n log n)
- Space: O(log n)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4
Input: -1 -> 5 -> 3 -> 4 -> 0
Output: -1 -> 0 -> 3 -> 4 -> 5
```

## Key Takeaways
- The merge sort algorithm is a good choice for sorting linked lists because it is stable and efficient.
- The key to implementing merge sort for linked lists is to split the list into two halves and then merge the two sorted halves back together.
- The time complexity of merge sort for linked lists is O(n log n), where n is the number of nodes in the list.