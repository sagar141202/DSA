# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove duplicates and return the modified list. The linked list should be sorted in ascending order. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output list should be 1 -> 2 -> 3 -> 4 -> 5. The function should take the head of the list as input and return the head of the modified list.

## Approach
We will use a two-pointer approach to traverse the list and remove duplicates. The algorithm will iterate through the list, comparing adjacent nodes and removing duplicates. This approach ensures that the list remains sorted.

## Complexity
- Time: O(n)
- Space: O(1)

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
    ListNode* deleteDuplicates(ListNode* head) {
        // If the list is empty, return nullptr
        if (!head) return nullptr;
        
        // Initialize two pointers, current and next
        ListNode* current = head;
        
        // Traverse the list
        while (current->next) {
            // If the current node's value is equal to the next node's value, remove the next node
            if (current->val == current->next->val) {
                current->next = current->next->next;
            } 
            // Otherwise, move to the next node
            else {
                current = current->next;
            }
        }
        
        // Return the head of the modified list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- We can remove duplicates from a sorted linked list in O(n) time complexity.
- The space complexity is O(1) since we only use a constant amount of space to store the pointers.
- This solution modifies the original list and does not create a new list.