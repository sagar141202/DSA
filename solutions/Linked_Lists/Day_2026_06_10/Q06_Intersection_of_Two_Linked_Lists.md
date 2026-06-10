# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists start to overlap. If there is no intersection, return null. The lists are non-empty and each node has a unique value. The lists do not have cycles. For example, if listA is 4 -> 1 -> 8 -> 4 -> 5 and listB is 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
The algorithm uses a two-pointer technique to traverse both lists. It calculates the lengths of both lists and then moves the longer list's pointer forward by the difference in lengths. Then, it moves both pointers one step at a time and checks if they meet at the same node.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // Calculate the lengths of both lists
        int lenA = 0, lenB = 0;
        ListNode *tempA = headA, *tempB = headB;
        while (tempA) {
            lenA++;
            tempA = tempA->next;
        }
        while (tempB) {
            lenB++;
            tempB = tempB->next;
        }

        // Move the longer list's pointer forward
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }

        // Move both pointers one step at a time
        while (headA && headB) {
            if (headA == headB) {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }

        return NULL;
    }
};
```

## Test Cases
```
Input: listA = [4, 1, 8, 4, 5], listB = [5, 0, 1, 8, 4, 5]
Output: The node with value 8
```

## Key Takeaways
- The algorithm has a time complexity of O(m + n) where m and n are the lengths of the two lists.
- The space complexity is O(1) as it only uses a constant amount of space.
- This solution assumes that the lists do not have cycles and each node has a unique value.