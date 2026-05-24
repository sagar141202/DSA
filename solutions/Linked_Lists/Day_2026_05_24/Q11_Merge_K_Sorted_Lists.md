# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' linked lists, where each linked list is sorted in ascending order, merge all the linked lists into one sorted linked list. The function should take the array of linked lists as input and return the head of the merged linked list. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can solve this problem by using a priority queue to store the current smallest node from each linked list. We keep removing the smallest node from the queue and add it to the merged list, then add the next node from the same list to the queue. This approach ensures that the merged list is always sorted.

## Complexity
- Time: O(N log k)
- Space: O(k)

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

struct compare {
    bool operator()(const ListNode* a, const ListNode* b) {
        return a->val > b->val;
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compare> pq;
        // Add the head of each linked list to the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }
        
        // Create a dummy node to serve as the head of the merged list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the linked lists
        while (!pq.empty()) {
            ListNode* smallest = pq.top();
            pq.pop();
            current->next = smallest;
            current = current->next;
            if (smallest->next) {
                pq.push(smallest->next);
            }
        }
        
        return dummy->next;
    }
};
```

## Test Cases
```
Input: [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

## Key Takeaways
- Use a priority queue to efficiently merge the linked lists.
- Create a dummy node to simplify the code and avoid edge cases.
- Keep track of the current smallest node from each linked list in the priority queue.