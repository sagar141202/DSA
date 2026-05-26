# Smallest Range Covering Elements from K Lists

## Problem Statement
Given K sorted lists of integers, find the smallest range that covers at least one element from each list. The range is defined as [min, max] where min and max are the minimum and maximum values in the range. The range should be as small as possible. For example, given lists [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], the smallest range covering elements from all lists is [20, 24].

## Approach
We use a priority queue to store the current smallest element from each list along with its list index and element index. We keep track of the maximum element seen so far and the minimum range found. We update the maximum element and the minimum range whenever we find a smaller range.

## Complexity
- Time: O(N log K) where N is the total number of elements across all lists and K is the number of lists
- Space: O(K) for storing the priority queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        int n = nums.size();
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        
        // initialize the priority queue with the first element from each list
        for (int i = 0; i < n; i++) {
            pq.push({nums[i][0], i, 0});
        }
        
        int max_val = INT_MIN;
        for (auto& vec : nums) {
            max_val = max(max_val, vec[0]);
        }
        
        int min_range = INT_MAX;
        int min_start = 0;
        int min_end = 0;
        
        while (!pq.empty()) {
            auto [val, list_idx, elem_idx] = pq.top();
            pq.pop();
            
            // update the maximum value
            max_val = max(max_val, nums[list_idx][elem_idx]);
            
            // update the minimum range if a smaller range is found
            if (max_val - val < min_range) {
                min_range = max_val - val;
                min_start = val;
                min_end = max_val;
            }
            
            // move to the next element in the current list
            if (elem_idx + 1 < nums[list_idx].size()) {
                pq.push({nums[list_idx][elem_idx + 1], list_idx, elem_idx + 1});
            } else {
                break;
            }
        }
        
        return {min_start, min_end};
    }
};

int main() {
    Solution solution;
    vector<vector<int>> nums = {{4,10,15,24,26},{0,9,12,20},{5,18,22,30}};
    vector<int> result = solution.smallestRange(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
```

## Test Cases
```
Input: [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20, 24]
```

## Key Takeaways
- Use a priority queue to store the current smallest element from each list
- Keep track of the maximum element seen so far and the minimum range found
- Update the maximum element and the minimum range whenever a smaller range is found