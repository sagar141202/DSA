# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each linked list is sorted in ascending order. The merged list should also be sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can solve this problem by using a min-heap to store the current smallest node from each linked list. We then extract the smallest node from the heap, add it to the result list, and insert the next node from the same list into the heap. This process continues until all nodes are processed.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
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
        for (auto list : lists) {
            if (list) pq.push(list);
        }
        
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        
        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            curr->next = node;
            curr = curr->next;
            if (node->next) pq.push(node->next);
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
- Use a min-heap to efficiently select the smallest node from the linked lists.
- Process each node only once to avoid duplicates in the result list.
- Utilize a dummy node to simplify the code and avoid edge cases.