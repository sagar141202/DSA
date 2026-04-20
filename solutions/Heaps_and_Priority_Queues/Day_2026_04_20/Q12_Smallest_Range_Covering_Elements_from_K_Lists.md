# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. If there are multiple such ranges, return the one with the smallest length. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20,24].

## Approach
We can use a priority queue to keep track of the smallest element from each list. The algorithm starts by pushing the first element of each list into the priority queue. Then, it repeatedly pops the smallest element from the queue and pushes the next element from the same list until all lists are exhausted. The smallest range is updated whenever a new element is pushed into the queue.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // Create a min-heap to store elements from all lists
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> minHeap;
        
        // Push the first element of each list into the min-heap
        for (int i = 0; i < nums.size(); i++) {
            minHeap.push({nums[i][0], i, 0});
        }
        
        // Initialize the smallest range
        int minRange = INT_MAX;
        vector<int> result;
        
        // Initialize the maximum value in the current range
        int maxVal = INT_MIN;
        for (auto& num : nums) {
            maxVal = max(maxVal, num[0]);
        }
        
        while (!minHeap.empty()) {
            // Get the smallest element from the min-heap
            auto minVal = minHeap.top();
            minHeap.pop();
            
            // Update the smallest range if the current range is smaller
            if (maxVal - minVal[0] < minRange) {
                minRange = maxVal - minVal[0];
                result = {minVal[0], maxVal};
            }
            
            // Push the next element from the same list into the min-heap
            if (minVal[2] + 1 < nums[minVal[1]].size()) {
                int nextVal = nums[minVal[1]][minVal[2] + 1];
                minHeap.push({nextVal, minVal[1], minVal[2] + 1});
                maxVal = max(maxVal, nextVal);
            } else {
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
Output: [20,24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Update the smallest range whenever a new element is pushed into the queue.
- The algorithm has a time complexity of O(N log K) where N is the total number of elements and K is the number of lists.