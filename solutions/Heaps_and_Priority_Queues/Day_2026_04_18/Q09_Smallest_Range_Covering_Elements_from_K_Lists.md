# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [start, end], where start and end are integers. If multiple ranges have the same smallest size, return any of them. For example, given lists `[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`, the smallest range covering elements from all lists is `[20, 24]`.

## Approach
We use a priority queue to keep track of the smallest element from each list. The priority queue stores pairs of the current element and its list index. We keep expanding the range by removing the smallest element from the queue and adding the next element from the same list until we cover all lists. The smallest range is updated whenever we find a smaller range that covers all lists.

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
        // Create a priority queue to store the current element and its list index
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        int mx = INT_MIN;
        
        // Initialize the priority queue with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
            mx = max(mx, nums[i][0]);
        }
        
        int ans = INT_MAX;
        vector<int> res = {-1, -1};
        
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            
            // If the current range is smaller than the smallest range found so far, update the smallest range
            if (mx - curr[0] < ans) {
                ans = mx - curr[0];
                res = {curr[0], mx};
            }
            
            // If we have not reached the end of the current list, add the next element to the priority queue
            if (curr[2] + 1 < nums[curr[1]].size()) {
                pq.push({nums[curr[1]][curr[2] + 1], curr[1], curr[2] + 1});
                mx = max(mx, nums[curr[1]][curr[2] + 1]);
            } else {
                // If we have reached the end of the current list, break the loop
                break;
            }
        }
        
        return res;
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- Use a priority queue to efficiently select the smallest element from each list.
- Keep track of the maximum element in the current range to update the smallest range.
- Break the loop when we reach the end of any list, as we cannot find a smaller range.