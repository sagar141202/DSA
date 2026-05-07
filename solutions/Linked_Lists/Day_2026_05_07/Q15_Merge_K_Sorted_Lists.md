# Merge K Sorted Lists

## Problem Statement
Merge k sorted linked lists into one sorted linked list. The lists are non-empty and each node has a unique value. The problem can be solved using a priority queue to keep track of the smallest node from each list at any given time. The constraints are that the input lists are non-empty and each node has a unique value. For example, given lists [[1,4,5],[1,3,4],[2,6]], the output should be [1,1,2,3,4,4,5,6].

## Approach
The algorithm uses a min-heap to store the current smallest node from each list. It repeatedly extracts the smallest node from the heap and adds it to the result list, then inserts the next node from the same list into the heap. This process continues until all nodes have been processed.

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
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Input: [[1,2,3],[4,5,6]]
Output: [1,2,3,4,5,6]
```

## Key Takeaways
- Use a min-heap to keep track of the smallest node from each list.
- Repeatedly extract the smallest node from the heap and add it to the result list.
- Insert the next node from the same list into the heap to maintain the heap property.