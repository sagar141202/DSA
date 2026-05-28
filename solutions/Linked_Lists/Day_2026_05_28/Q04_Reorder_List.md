# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node, then the second to last node, and so on. The reordering should be done in-place, meaning that only the existing nodes can be used and no new nodes can be allocated. For example, if the input list is 1 -> 2 -> 3 -> 4, the output should be 1 -> 4 -> 2 -> 3. If the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 5 -> 2 -> 4 -> 3.

## Approach
The approach to solve this problem involves finding the middle of the linked list, reversing the second half of the list, and then merging the two halves. This can be achieved by using three pointers to track the current node, the next node, and the previous node.

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
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        // find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse the second half of the list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* next = second->next;
            second->next = prev;
            prev = second;
            second = next;
        }

        // merge the two halves
        ListNode* first = head;
        while (prev) {
            ListNode* nextFirst = first->next;
            ListNode* nextPrev = prev->next;
            first->next = prev;
            prev->next = nextFirst;
            first = nextFirst;
            prev = nextPrev;
        }
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
```

## Key Takeaways
- To solve this problem, we need to find the middle of the linked list.
- We then reverse the second half of the list and merge it with the first half.
- The time complexity of this solution is O(n), where n is the number of nodes in the list, and the space complexity is O(1) as we only use a constant amount of space.