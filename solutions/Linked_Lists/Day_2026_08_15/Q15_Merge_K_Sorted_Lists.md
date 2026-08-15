# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The merged linked list should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can use a priority queue to store the current smallest node from each linked list. The priority queue will automatically sort the nodes based on their values. We can then pop the smallest node from the priority queue, add it to the merged linked list, and push the next node from the same linked list into the priority queue.

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

class Solution {
public:
    struct compare {
        bool operator()(const ListNode* a, const ListNode* b) {
            return a->val > b->val;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compare> pq;
        
        // push the head of each linked list into the priority queue
        for (ListNode* node : lists) {
            if (node) {
                pq.push(node);
            }
        }
        
        // create a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // merge the linked lists
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            current->next = node;
            current = current->next;
            
            // push the next node into the priority queue
            if (node->next) {
                pq.push(node->next);
            }
        }
        
        return dummy->next;
    }
};
```

## Test Cases
```
Input: [
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

## Key Takeaways
- We can use a priority queue to efficiently merge sorted linked lists.
- The time complexity is O(N log k) because we are pushing and popping nodes from the priority queue N times, and each push and pop operation takes O(log k) time.
- The space complexity is O(k) because we are storing k nodes in the priority queue.