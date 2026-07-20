# Merge K Sorted Lists

## Problem Statement
You are given an array of 'k' linked lists, each of which is sorted in ascending order. Merge these linked lists into one sorted linked list. The head of each linked list is given as an array of ListNode objects, where each ListNode object contains an integer value and a pointer to the next node in the list. The merged linked list should also be sorted in ascending order. For example, if you have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We will use a priority queue to store the current smallest node from each linked list. The priority queue will be ordered based on the value of the nodes. We will keep removing the smallest node from the queue, add it to our result, and insert the next node from the same list into the queue. This process will continue until all nodes have been processed.

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
        
        // Push the head of each list into the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }
        
        // Create a dummy node to serve as the head of our result
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Process nodes in the priority queue
        while (!pq.empty()) {
            // Remove the smallest node from the queue
            ListNode* smallest = pq.top();
            pq.pop();
            
            // Add the smallest node to our result
            current->next = smallest;
            current = current->next;
            
            // Insert the next node from the same list into the queue
            if (smallest->next) {
                pq.push(smallest->next);
            }
        }
        
        // Return the next node of the dummy node, which is the head of our result
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
Input: [[]]
Output: []
```

## Key Takeaways
- We use a priority queue to efficiently select the smallest node from the current nodes of the linked lists.
- The time complexity is O(N log k) because we perform a heap operation for each node, where N is the total number of nodes and k is the number of linked lists.
- The space complexity is O(k) because in the worst case, the priority queue will store one node from each linked list.