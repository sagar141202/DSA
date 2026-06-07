# Smallest Range Covering Elements from K Lists

## Problem Statement
Given `k` sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as `[start, end]`, where `start` and `end` are integers. If there are multiple such ranges, return the one with the smallest length. If there are still multiple ranges with the same length, return the one with the smallest `start` value.

## Approach
We can use a priority queue to keep track of the smallest element from each list. We start by adding the first element from each list to the priority queue. Then, we keep track of the maximum element in the priority queue and the smallest range seen so far. We keep removing the smallest element from the priority queue and adding the next element from the same list until we find a range that covers all lists.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
#include <vector>
using namespace std;

struct Node {
    int val, row, col;
    Node(int v, int r, int c) : val(v), row(r), col(c) {}
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.val > b.val;
    }
};

vector<int> smallestRange(vector<vector<int>>& nums) {
    priority_queue<Node, vector<Node>, Compare> pq;
    int maxVal = INT_MIN, range = INT_MAX, start = 0, end = 0;
    
    // Add first element from each list to the priority queue
    for (int i = 0; i < nums.size(); i++) {
        pq.push(Node(nums[i][0], i, 0));
        maxVal = max(maxVal, nums[i][0]);
    }
    
    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();
        
        // Update range if current range is smaller
        if (maxVal - node.val < range) {
            range = maxVal - node.val;
            start = node.val;
            end = maxVal;
        }
        
        // Add next element from the same list to the priority queue
        if (node.col + 1 < nums[node.row].size()) {
            pq.push(Node(nums[node.row][node.col + 1], node.row, node.col + 1));
            maxVal = max(maxVal, nums[node.row][node.col + 1]);
        } else {
            // If we have reached the end of a list, break the loop
            break;
        }
    }
    
    return {start, end};
}
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- We use a priority queue to keep track of the smallest element from each list.
- We keep track of the maximum element in the priority queue and the smallest range seen so far.
- We use a struct `Node` to store the value, row, and column of each element in the priority queue.