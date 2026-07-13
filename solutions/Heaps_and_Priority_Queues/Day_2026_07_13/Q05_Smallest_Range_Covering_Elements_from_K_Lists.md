# Smallest Range Covering Elements from K Lists

## Problem Statement
Given `k` sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as `[start, end]`, where `start` and `end` are integers. If there are multiple such ranges, return the one with the smallest length. The input lists are non-empty, and the total number of elements across all lists is `n`. The elements in each list are distinct, and the lists are sorted in ascending order.

## Approach
The algorithm uses a priority queue to keep track of the smallest element from each list. It iterates over the lists, updating the queue and the range as necessary. The intuition is to maintain a sliding window of elements, where the window is expanded or contracted based on the smallest element in the queue.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // Create a min-heap to store elements from each list
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Initialize the heap with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the range
        int start = INT_MIN, end = INT_MAX;
        int max_val = *max_element(nums[0].begin(), nums[0].end());
        for (auto& list : nums) {
            max_val = max(max_val, *max_element(list.begin(), list.end()));
        }
        
        // Iterate over the heap
        while (!pq.empty()) {
            // Get the smallest element from the heap
            auto curr = pq.top();
            pq.pop();
            
            // Update the range if necessary
            if (max_val - curr[0] < end - start) {
                start = curr[0];
                end = max_val;
            }
            
            // Add the next element from the current list to the heap
            if (curr[2] + 1 < nums[curr[1]].size()) {
                pq.push({nums[curr[1]][curr[2] + 1], curr[1], curr[2] + 1});
                max_val = max(max_val, nums[curr[1]][curr[2] + 1]);
            } else {
                break;
            }
        }
        
        return {start, end};
    }
};
```

## Test Cases
```
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- Using a priority queue to keep track of the smallest element from each list is an efficient approach to this problem.
- The time complexity is O(n log k) due to the use of the priority queue, where n is the total number of elements and k is the number of lists.
- The space complexity is O(k) because we need to store k elements in the priority queue.