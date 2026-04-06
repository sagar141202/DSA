# Merge K Sorted Lists

## Problem Statement
Given an array of 'k' sorted linked lists, merge them into one sorted linked list. Each node in the linked list has a value and a pointer to the next node. The input linked lists are sorted in ascending order. For example, if we have three linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, and 2 -> 6, the merged linked list should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

## Approach
We can use a priority queue to store the current smallest node from each linked list. The priority queue will be ordered based on the node values. We will keep removing the smallest node from the priority queue and add it to our result linked list, then add the next node from the same linked list to the priority queue.

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
        // Create a priority queue to store the current smallest node from each linked list
        priority_queue<ListNode*, vector<ListNode*>, compare> pq;
        
        // Add the head of each linked list to the priority queue
        for (auto list : lists) {
            if (list) {
                pq.push(list);
            }
        }
        
        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge the linked lists
        while (!pq.empty()) {
            // Remove the smallest node from the priority queue
            ListNode* smallest = pq.top();
            pq.pop();
            
            // Add the smallest node to the result linked list
            current->next = smallest;
            current = current->next;
            
            // Add the next node from the same linked list to the priority queue
            if (smallest->next) {
                pq.push(smallest->next);
            }
        }
        
        // Return the result linked list
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
- We use a priority queue to efficiently find the smallest node from each linked list.
- The time complexity is O(N log k) because we perform a heap operation for each node in the linked lists, and each heap operation takes O(log k) time.
- The space complexity is O(k) because we store the current smallest node from each linked list in the priority queue.