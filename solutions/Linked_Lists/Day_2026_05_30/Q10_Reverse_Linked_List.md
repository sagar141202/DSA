# Reverse Linked List

## Problem Statement
Reverse a singly linked list. Given the head of a linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes will have values in the range [-5000, 5000]. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The algorithm will iterate through the linked list, keeping track of the current node and the previous node. It will then reverse the link of the current node to point to the previous node. This process will be repeated until the end of the linked list is reached. The new head of the reversed linked list will be the last node visited.

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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
};
```

## Test Cases
```
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: [1,2]
Output: [2,1]
Input: []
Output: []
```

## Key Takeaways
- Reversing a linked list can be done in-place, without using any extra space.
- The key to reversing a linked list is to keep track of the previous node and update the `next` pointer of the current node to point to the previous node.
- The time complexity of reversing a linked list is O(n), where n is the number of nodes in the list.