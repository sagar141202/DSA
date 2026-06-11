# Smallest Range Covering Elements from K Lists

## Problem Statement
Given `k` sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as `[start, end]`, where `start` is the smallest element and `end` is the largest element in the range. If there are multiple ranges with the same length, return the one with the smallest `start` value.

## Approach
The approach involves using a min-heap to keep track of the smallest element from each list. We initialize the heap with the first element from each list, along with the list index and element index. Then, we repeatedly pop the smallest element from the heap and push the next element from the same list until we find a range that covers at least one element from each list.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // Create a min-heap to store the elements
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Initialize the heap with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the range
        int start = INT_MIN, end = INT_MAX;
        int max_val = *max_element(nums[0].begin(), nums[0].end());
        
        for (int i = 1; i < nums.size(); i++) {
            max_val = max(max_val, *max_element(nums[i].begin(), nums[i].end()));
        }
        
        while (true) {
            // Get the smallest element from the heap
            auto curr = pq.top();
            pq.pop();
            
            // Update the range if the current element is smaller than the start
            if (curr[0] > end) {
                break;
            }
            
            // Update the range if the current element is larger than the max_val
            if (curr[0] > max_val) {
                start = max_val;
                end = curr[0];
            } else {
                start = curr[0];
                end = max_val;
            }
            
            // Push the next element from the same list into the heap
            if (curr[2] + 1 < nums[curr[1]].size()) {
                pq.push({nums[curr[1]][curr[2] + 1], curr[1], curr[2] + 1});
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
- Use a min-heap to keep track of the smallest element from each list.
- Initialize the heap with the first element from each list, along with the list index and element index.
- Repeatedly pop the smallest element from the heap and push the next element from the same list until we find a range that covers at least one element from each list.