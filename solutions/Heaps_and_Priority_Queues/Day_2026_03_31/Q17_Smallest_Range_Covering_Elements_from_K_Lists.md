# Smallest Range Covering Elements from K Lists

## Problem Statement
Given `k` sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as `[min, max]`, where `min` and `max` are the minimum and maximum values in the range, respectively. If there are multiple smallest ranges, return any of them. For example, given `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`, the output should be `[20, 24]`.

## Approach
We will use a priority queue to keep track of the smallest element from each list. The algorithm starts by adding the first element from each list into the priority queue. Then, we keep removing the smallest element from the priority queue and add the next element from the same list until we find the smallest range that covers at least one element from each list.

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
        // Create a priority queue to store the current smallest element from each list
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Add the first element from each list into the priority queue
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the smallest range
        int minRange = INT_MAX;
        int maxRange = INT_MIN;
        vector<int> result;
        
        // Keep removing the smallest element from the priority queue
        while (!pq.empty()) {
            // Get the smallest element from the priority queue
            auto curr = pq.top();
            pq.pop();
            
            // Update the smallest range
            minRange = min(minRange, curr[0]);
            maxRange = max(maxRange, curr[0]);
            
            // If the current range is the smallest, update the result
            if (maxRange - minRange < result[1] - result[0] || result.empty()) {
                result = {minRange, maxRange};
            }
            
            // Add the next element from the same list into the priority queue
            if (curr[2] + 1 < nums[curr[1]].size()) {
                pq.push({nums[curr[1]][curr[2] + 1], curr[1], curr[2] + 1});
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Keep removing the smallest element from the priority queue and add the next element from the same list until we find the smallest range that covers at least one element from each list.
- Update the smallest range whenever we find a smaller range.