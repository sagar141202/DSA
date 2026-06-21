# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each node in the linked list has a value and a pointer to the next node. The input linked lists are non-empty, and each node has a unique value. The task is to return the head of the merged linked list. For example, if we have three sorted linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
The approach to solve this problem is to use a priority queue to keep track of the current smallest node in the linked lists. We start by pushing the head of each linked list into the priority queue. Then, we keep popping the smallest node from the queue, add it to the merged list, and push the next node from the same linked list into the queue. This process continues until all nodes are merged.

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
        for (ListNode* node : lists) {
            if (node) {
                pq.push(node);
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
Input: [
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Input: []
Output: null

Input: [
  1 -> 2 -> 3
]
Output: 1 -> 2 -> 3
```

## Key Takeaways
- Use a priority queue to efficiently select the smallest node from the linked lists.
- Create a dummy node to simplify the code and avoid special cases for the head of the merged list.
- The time complexity is O(N log k) because we perform a heap operation for each node, where N is the total number of nodes and k is the number of linked lists.