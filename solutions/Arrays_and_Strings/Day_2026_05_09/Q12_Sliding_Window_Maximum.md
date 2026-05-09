# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray of `nums`. The subarray should be considered as a sliding window, i.e., it can start at any index in `nums` and end at any index `k-1` positions later. The function should return a vector of integers representing the maximum values in each `k`-sized subarray.

## Approach
We will use a deque to store the indices of the elements in the current window. The deque will be maintained in such a way that the front always contains the index of the maximum element in the current window. We will iterate over the array and update the deque accordingly.

## Complexity
- Time: O(n)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    // Initialize the result vector and the deque
    vector<int> result;
    deque<int> dq;

    // Iterate over the array
    for (int i = 0; i < nums.size(); i++) {
        // Remove the elements from the back of the deque that are out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // Remove the elements from the back of the deque that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Add the current element to the deque
        dq.push_back(i);

        // Add the maximum element of the current window to the result vector
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }

    return result;
}
```

## Test Cases
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

## Key Takeaways
- Use a deque to store the indices of the elements in the current window.
- Maintain the deque in such a way that the front always contains the index of the maximum element in the current window.
- Remove the elements from the deque that are out of the current window or smaller than the current element.