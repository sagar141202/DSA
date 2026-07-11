# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max], where min and max are the minimum and maximum values in the range, respectively. The size of the range is max - min. If there are multiple ranges with the same size, return the one with the smallest min value. For example, given the lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24] with a size of 4.

## Approach
We can use a priority queue to keep track of the smallest element from each list. We start by adding the first element from each list to the priority queue. Then, we repeatedly remove the smallest element from the queue and add the next element from the same list until we find a range that covers at least one element from each list. The range with the smallest size is the answer.

## Complexity
- Time: O(N log K)
- Space: O(K)

## C++ Solution
```cpp
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // Create a min-heap to store the current smallest element from each list
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> minHeap;
        
        // Initialize the min-heap with the first element from each list
        for (int i = 0; i < nums.size(); i++) {
            minHeap.push({nums[i][0], i, 0});
        }
        
        // Initialize the range with the smallest possible values
        int rangeMin = INT_MIN;
        int rangeMax = INT_MAX;
        
        // Initialize the current maximum value in the range
        int currMax = INT_MIN;
        for (auto& num : nums) {
            currMax = max(currMax, num[0]);
        }
        
        // Loop until we find a range that covers at least one element from each list
        while (!minHeap.empty()) {
            // Get the smallest element from the min-heap
            auto smallest = minHeap.top();
            minHeap.pop();
            
            // Update the range if the current range is smaller
            if (currMax - smallest[0] < rangeMax - rangeMin) {
                rangeMin = smallest[0];
                rangeMax = currMax;
            }
            
            // Add the next element from the same list to the min-heap
            if (smallest[2] + 1 < nums[smallest[1]].size()) {
                minHeap.push({nums[smallest[1]][smallest[2] + 1], smallest[1], smallest[2] + 1});
                currMax = max(currMax, nums[smallest[1]][smallest[2] + 1]);
            } else {
                // If we reach the end of a list, break the loop
                break;
            }
        }
        
        return {rangeMin, rangeMax};
    }
};
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- Use a priority queue to keep track of the smallest element from each list.
- Repeatedly remove the smallest element from the queue and add the next element from the same list until we find a range that covers at least one element from each list.
- Update the range if the current range is smaller.