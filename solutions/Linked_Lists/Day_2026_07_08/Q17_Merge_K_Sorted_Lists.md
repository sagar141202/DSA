# Merge K Sorted Lists

## Problem Statement
Given an array of `k` linked lists, where each linked list is sorted in ascending order, merge all the linked lists into one sorted linked list. The input linked lists are non-empty and each node has a unique value. The head of each linked list is given as an array of `ListNode*` pointers. The merged linked list should also be sorted in ascending order. For example, if we have three linked lists: `1 -> 4 -> 5`, `1 -> 3 -> 4`, and `2 -> 6`, the merged linked list should be `1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`.

## Approach
We can use a priority queue to store the current smallest node from each linked list. We then pop the smallest node from the queue, add it to the merged list, and push the next node from the same list into the queue. This process continues until all nodes have been processed. The time complexity of this approach is O(N log k), where N is the total number of nodes and k is the number of linked lists.

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
    struct Compare {
        bool operator()(const ListNode* a, const ListNode* b) {
            return a->val > b->val;
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> queue;
        for (auto list : lists) {
            if (list) {
                queue.push(list);
            }
        }

        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;

        while (!queue.empty()) {
            ListNode* node = queue.top();
            queue.pop();
            tail->next = node;
            tail = tail->next;
            if (node->next) {
                queue.push(node->next);
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
- Use a priority queue to efficiently select the smallest node from the linked lists.
- Process each node only once to avoid duplicate nodes in the merged list.
- Use a dummy node to simplify the code and avoid edge cases.