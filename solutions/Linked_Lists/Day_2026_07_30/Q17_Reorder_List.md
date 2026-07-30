# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the nodes are rearranged in the following way: the first node is followed by the last node, then the second node, then the second-to-last node, and so on. The reordering should be done in-place. The length of the list is in the range [1, 20000]. The nodes in the list have values in the range [0, 10000].

## Approach
We will first find the middle of the linked list, then reverse the second half of the list. Finally, we will merge the two halves by alternating nodes from each half.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        // base case: if the list is empty or only has one node, return
        if (!head || !head->next || !head->next->next) return;
        
        // find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // reverse the second half of the list
        ListNode* secondHalf = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (secondHalf) {
            ListNode* nextNode = secondHalf->next;
            secondHalf->next = prev;
            prev = secondHalf;
            secondHalf = nextNode;
        }
        
        // merge the two halves
        ListNode* firstHalf = head;
        secondHalf = prev;
        while (secondHalf) {
            ListNode* nextNode1 = firstHalf->next;
            ListNode* nextNode2 = secondHalf->next;
            firstHalf->next = secondHalf;
            secondHalf->next = nextNode1;
            firstHalf = nextNode1;
            secondHalf = nextNode2;
        }
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3
```

## Key Takeaways
- To solve this problem, we need to find the middle of the linked list.
- We then reverse the second half of the list and merge the two halves by alternating nodes from each half.
- The time complexity of this solution is O(n), where n is the number of nodes in the list.