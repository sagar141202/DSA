# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but it may have up to 5000 nodes. Each node has a unique value ranging from -5000 to 5000. For example, if we have a linked list 4 -> 2 -> 1 -> 3, the sorted list should be 1 -> 2 -> 3 -> 4.

## Approach
The approach to solve this problem is to use the merge sort algorithm, which is a divide-and-conquer algorithm that splits the list into two halves, recursively sorts them, and then merges them. We will use a recursive function to split the list and a helper function to merge the sorted lists.

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
        if (!head || !head->next) return head;
        
        // Split the list into two halves
        ListNode* mid = getMiddle(head);
        ListNode* midNext = mid->next;
        
        // Break the list at the middle node
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
        
        // If there are remaining nodes in either list, append them
        if (l1) current->next = l1;
        if (l2) current->next = l2;
        
        return dummy->next;
    }
};
```

## Test Cases
```
Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4
```

## Key Takeaways
- Merge sort is an efficient algorithm for sorting linked lists.
- The key to solving this problem is to correctly split the list into two halves and merge the sorted halves.
- The time complexity of this solution is O(n log n), where n is the number of nodes in the list.