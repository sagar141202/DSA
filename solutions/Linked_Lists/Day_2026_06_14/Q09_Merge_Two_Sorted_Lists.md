# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the task is to create a new sorted list containing all elements from both lists. The function should take the heads of the two linked lists as input and return the head of the merged linked list. For example, given two lists 1 -> 3 -> 5 and 2 -> 4 -> 6, the merged list should be 1 -> 2 -> 3 -> 4 -> 5 -> 6. The lists can be of different lengths, and the function should handle cases where one or both lists are empty.

## Approach
The algorithm involves recursively comparing the current nodes of both lists and adding the smaller value to the merged list. If one list is exhausted, the remaining nodes from the other list are appended to the merged list. This approach ensures the resulting list is sorted in ascending order. The function uses a recursive approach to simplify the code and improve readability. The base cases handle empty lists and the recursive case merges the lists.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a new dummy node to serve as the head of the merged list
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        
        // While both lists have nodes
        while (l1 && l2) {
            // If the current node in l1 has a smaller value, add it to the merged list
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } 
            // Otherwise, add the current node from l2 to the merged list
            else {
                current->next = l2;
                l2 = l2->next;
            }
            // Move to the next node in the merged list
            current = current->next;
        }
        
        // If l1 has remaining nodes, append them to the merged list
        if (l1) {
            current->next = l1;
        } 
        // If l2 has remaining nodes, append them to the merged list
        else if (l2) {
            current->next = l2;
        }
        
        // Return the head of the merged list (which is the next node of the dummy node)
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Input: l1 = [], l2 = []
Output: []
Input: l1 = [], l2 = [0]
Output: [0]
```

## Key Takeaways
- The function handles cases where one or both input lists are empty.
- The function uses a dummy node to simplify the code and avoid special cases for the head of the merged list.
- The time complexity is O(n + m), where n and m are the lengths of the input lists, because each node is visited once.