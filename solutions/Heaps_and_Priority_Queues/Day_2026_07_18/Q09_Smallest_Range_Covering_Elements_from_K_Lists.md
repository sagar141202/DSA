# Smallest Range Covering Elements from K Lists

## Problem Statement
Given `k` sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as `[min, max]`, where `min` and `max` are the minimum and maximum values in the range, respectively. The range should be as small as possible, i.e., `max - min` should be minimized. For example, given `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`, the smallest range covering elements from all lists is `[20, 24]`.

## Approach
The approach is to use a priority queue to keep track of the smallest element from each list. We start by pushing the first element from each list into the priority queue. Then, we keep popping the smallest element from the queue and pushing the next element from the same list until we find the smallest range that covers at least one element from each list.

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
        // Create a priority queue to store the elements
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        // Push the first element from each list into the priority queue
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the smallest range
        int minRange = INT_MAX;
        vector<int> result;
        
        // Initialize the maximum value in the current range
        int maxVal = INT_MIN;
        for (auto& x : nums) {
            maxVal = max(maxVal, x[0]);
        }
        
        while (!pq.empty()) {
            // Get the smallest element from the priority queue
            auto minVal = pq.top();
            pq.pop();
            
            // Update the smallest range if necessary
            if (maxVal - minVal[0] < minRange) {
                minRange = maxVal - minVal[0];
                result = {minVal[0], maxVal};
            }
            
            // Push the next element from the same list into the priority queue
            if (minVal[2] + 1 < nums[minVal[1]].size()) {
                int nextVal = nums[minVal[1]][minVal[2] + 1];
                pq.push({nextVal, minVal[1], minVal[2] + 1});
                maxVal = max(maxVal, nextVal);
            } else {
                // If we have reached the end of a list, break the loop
                break;
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- We use a priority queue to keep track of the smallest element from each list.
- We update the smallest range whenever we find a smaller range that covers at least one element from each list.
- The time complexity is O(N log k), where N is the total number of elements and k is the number of lists.