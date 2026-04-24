# Smallest Range Covering Elements from K Lists

## Problem Statement
Given `k` sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as `[start, end]`, where `start` and `end` are integers. If there are multiple such ranges, return the one with the smallest length. If there are still multiple ranges with the same length, return the one with the smallest `start` value.

## Approach
We can use a priority queue to keep track of the smallest element from each list. We iterate through the lists, adding the smallest element from each list to the priority queue. We then remove the smallest element from the priority queue and add the next element from the same list. We keep track of the range with the smallest length.

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
        
        // Add the first element from each list to the priority queue
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        // Initialize the range
        int start = INT_MIN, end = INT_MAX;
        
        // Initialize the minimum range length
        int minRange = INT_MAX;
        
        // Initialize the current range
        int currStart = pq.top()[0], currEnd = INT_MIN;
        for (auto& num : nums) {
            currEnd = max(currEnd, num[0]);
        }
        
        // Iterate through the priority queue
        while (!pq.empty()) {
            // Get the smallest element from the priority queue
            auto temp = pq.top();
            pq.pop();
            
            // Update the current range
            currStart = temp[0];
            currEnd = INT_MIN;
            for (auto& num : nums) {
                if (num.size() > 0) {
                    currEnd = max(currEnd, num[0]);
                }
            }
            
            // Update the range if the current range is smaller
            if (currEnd - currStart < minRange) {
                minRange = currEnd - currStart;
                start = currStart;
                end = currEnd;
            }
            
            // Add the next element from the same list to the priority queue
            if (temp[2] + 1 < nums[temp[1]].size()) {
                pq.push({nums[temp[1]][temp[2] + 1], temp[1], temp[2] + 1});
            }
        }
        
        // Return the range
        return {start, end};
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Iterate through the lists, adding the smallest element from each list to the priority queue.
- Keep track of the range with the smallest length.