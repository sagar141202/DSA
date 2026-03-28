# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the node where they intersect. The intersection is defined as the node where the two lists merge and have the same nodes from that point onwards. If there is no intersection, return NULL. The lists are non-circular and may have different lengths. For example, given two linked lists: 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection node is 8.

## Approach
We can solve this problem by calculating the lengths of both linked lists, then moving the longer list forward by the difference in lengths, and finally moving both lists one step at a time until we find the intersection node or reach the end of both lists. This approach ensures that we can find the intersection node in a single pass.

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
        // calculate the lengths of both linked lists
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
        
        // move the longer list forward by the difference in lengths
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }
        
        // move both lists one step at a time until we find the intersection node or reach the end of both lists
        while (headA && headB) {
            if (headA == headB) {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        
        // if no intersection is found, return NULL
        return NULL;
    }
};
```

## Test Cases
```
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
Output: The node with value 8
Input: headA = [2,6,4], headB = [1,5]
Output: NULL
```

## Key Takeaways
- The time complexity of this solution is O(m + n), where m and n are the lengths of the two linked lists.
- The space complexity of this solution is O(1), as we only use a constant amount of space to store the lengths of the lists and the current nodes.
- This solution assumes that the lists do not have cycles and that the intersection is defined as the node where the two lists merge and have the same nodes from that point onwards.