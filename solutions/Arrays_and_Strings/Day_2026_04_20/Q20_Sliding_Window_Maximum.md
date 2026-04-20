# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should be fully contained within the array, and the maximum value should be returned in the order of the subarrays. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[3, 3, 5, 5, 6, 7]`.

## Approach
We can use a deque to store the indices of the elements in the current window, maintaining the maximum value at the front. When the window moves, we remove the elements that are out of the window and the elements that are smaller than the new element.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // Initialize the result vector and the deque
        vector<int> result;
        deque<int> dq;
        
        // Iterate over the array
        for (int i = 0; i < nums.size(); i++) {
            // Remove the elements that are out of the window
            while (!dq.empty() && dq.front() < i - k + 1) {
                dq.pop_front();
            }
            
            // Remove the elements that are smaller than the new element
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            
            // Add the new element to the deque
            dq.push_back(i);
            
            // Add the maximum value to the result vector
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Maintain the maximum value at the front of the deque.
- Remove the elements that are out of the window and the elements that are smaller than the new element.