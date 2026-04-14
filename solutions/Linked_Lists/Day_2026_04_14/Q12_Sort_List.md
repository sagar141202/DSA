# Sort List

## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order. The linked list will have at least one node, but it may have up to 5000 nodes. The nodes will have values ranging from -5000 to 5000. For example, given the linked list `4 -> 2 -> 1 -> 3`, the output should be `1 -> 2 -> 3 -> 4`. The list is singly linked, meaning each node only points to the next node.

## Approach
To solve this problem, we can use the merge sort algorithm, which is suitable for linked lists. The algorithm works by recursively splitting the list into two halves until we have sublists with one node, and then merging these sublists in sorted order. We will use a recursive approach to implement the merge sort algorithm.

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
    
    // Function to get the middle of the linked list
    ListNode* getMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
    
    // Function to merge two sorted linked lists
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
Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4

Input: -1 -> 5 -> 3 -> 4 -> 0
Output: -1 -> 0 -> 3 -> 4 -> 5
```

## Key Takeaways
- The merge sort algorithm is suitable for sorting linked lists because it can be implemented recursively and efficiently.
- To implement merge sort on a linked list, we need to split the list into two halves, recursively sort the halves, and then merge the sorted halves.
- The time complexity of the merge sort algorithm is O(n log n), where n is the number of nodes in the linked list.