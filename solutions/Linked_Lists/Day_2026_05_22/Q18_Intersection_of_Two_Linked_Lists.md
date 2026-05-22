# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the node at which they intersect. The intersection node is the node where the two linked lists merge into a single linked list. If there is no intersection, return null. The lists are non-empty and may have different lengths. For example, given two linked lists a = [4,1,8,4,5] and b = [5,0,1,8,4,5], the intersection node is the node with value 8.

## Approach
We can solve this problem by calculating the lengths of both linked lists and then moving the longer list forward by the difference in lengths. Then, we can move both lists one step at a time and check if the current nodes are the same. If they are, we have found the intersection node.

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
        // calculate lengths of both lists
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

        // move longer list forward by difference in lengths
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }

        // move both lists one step at a time and check for intersection
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
Input: a = [4,1,8,4,5], b = [5,0,1,8,4,5]
Output: node with value 8
```

## Key Takeaways
- The time complexity of the solution is O(m + n), where m and n are the lengths of the two linked lists.
- The space complexity is O(1), as we only use a constant amount of space to store the lengths of the lists and the current nodes.
- This solution assumes that the lists do not have cycles and that the intersection node is the node where the two lists merge into a single list.