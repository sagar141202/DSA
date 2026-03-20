# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. The lists are non-empty, and each node has a unique value. The first node of each linked list is given, and each node has a 'next' pointer and a 'val' attribute. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can solve this problem by using a priority queue to store the current smallest node from each linked list. We then repeatedly pop the smallest node from the queue and add it to the result list, and push the next node from the same list into the queue. This ensures that the resulting list is sorted.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
#include <vector>

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

    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        std::priority_queue<ListNode*, std::vector<ListNode*>, compare> pq;
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }

        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;

        while (!pq.empty()) {
            ListNode* node = pq.top();
            pq.pop();
            curr->next = node;
            curr = curr->next;
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
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Input: []
Output: []
Input: [[1]]
Output: [1]
```

## Key Takeaways
- Use a priority queue to efficiently select the smallest node from the linked lists.
- Create a dummy node to simplify the code for the result list.
- Iterate through the priority queue to construct the merged linked list.