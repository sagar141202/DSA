# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the node where they intersect. The intersection is defined as the node where the two lists merge and have the same nodes until the end. If there is no intersection, return NULL. The lists are non-cyclic and may have different lengths. For example, given two linked lists `4 -> 1 -> 8 -> 4 -> 5` and `5 -> 0 -> 1 -> 8 -> 4 -> 5`, the intersection node is `8`.

## Approach
We can solve this problem by calculating the length of both linked lists and then moving the longer list forward by the difference in lengths. Then, we can move both lists one step at a time and check if the nodes are the same. If they are, we have found the intersection node. This approach ensures that we only need to traverse the lists once.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
        
        // move both lists one step at a time and check if the nodes are the same
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
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
Output: Intersection node is 8
Input: headA = [2,6,4], headB = [1,5]
Output: NULL
```

## Key Takeaways
- The time complexity is O(m + n) where m and n are the lengths of the two linked lists.
- The space complexity is O(1) as we only use a constant amount of space.
- This solution assumes that the lists are non-cyclic and may have different lengths.