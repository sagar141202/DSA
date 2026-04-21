# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The merged list should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can use a min-heap to keep track of the smallest node from each linked list. The node with the smallest value will be popped from the heap and added to the result list. We then push the next node from the same linked list into the heap. This process continues until all nodes from all linked lists have been processed.

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
        
        // Push the head of each linked list into the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }
        
        // Create a dummy node to serve as the head of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the linked lists
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            current->next = node;
            current = current->next;
            
            // Push the next node from the same linked list into the priority queue
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
- Use a min-heap to efficiently select the smallest node from each linked list.
- Create a dummy node to simplify the code and avoid special cases for the head of the result list.
- Push the next node from the same linked list into the priority queue to ensure all nodes are processed.