# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should contain `k` elements and the maximum value should be the maximum of all elements in the subarray. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`.

## Approach
We use a deque to store the indices of the elements in the current window, with the front of the deque containing the index of the maximum element. We remove elements from the back of the deque that are smaller than the current element and remove elements from the front of the deque that are out of the current window.

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
            // Remove elements from the back of the deque that are smaller than the current element
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            
            // Add the current element to the back of the deque
            dq.push_back(i);
            
            // Remove elements from the front of the deque that are out of the current window
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }
            
            // Add the maximum element to the result vector
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
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Input: nums = [1], k = 1
Output: [1]
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Remove elements from the back of the deque that are smaller than the current element to ensure the front of the deque contains the index of the maximum element.
- Remove elements from the front of the deque that are out of the current window to ensure the deque only contains elements in the current window.