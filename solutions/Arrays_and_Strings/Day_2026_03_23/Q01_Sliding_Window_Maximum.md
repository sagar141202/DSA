# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each subarray of size `k` using the sliding window technique. The subarray can be formed by moving the window one step at a time to the right. For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the output should be `[3, 3, 5, 5, 6, 7]`.

## Approach
The algorithm uses a deque to store the indices of the elements in the current window. It maintains the deque such that the front always contains the index of the maximum element in the current window. This is achieved by removing the elements from the back of the deque that are smaller than the current element and removing the elements from the front that are out of the current window.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    // Create a deque to store the indices of the elements in the current window
    deque<int> dq;
    vector<int> result;
    
    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // Remove the elements from the back of the deque that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        
        // Remove the elements from the front of the deque that are out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }
        
        // Add the current element to the deque
        dq.push_back(i);
        
        // Add the maximum element in the current window to the result
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    
    return result;
}
```

## Test Cases
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Maintain the deque such that the front always contains the index of the maximum element in the current window.
- Remove the elements from the back of the deque that are smaller than the current element and remove the elements from the front that are out of the current window.