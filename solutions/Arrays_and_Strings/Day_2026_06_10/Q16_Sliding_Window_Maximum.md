# Sliding Window Maximum

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the maximum value in each `k`-sized subarray. The subarray should be fully contained within the array. For example, given `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]`. The constraints are `1 <= nums.length <= 10^5` and `1 <= k <= nums.length`.

## Approach
The algorithm uses a deque to store the indices of the maximum elements in the current window. It iterates over the array, removing elements that are out of the window and smaller than the current element. The maximum element in the window is added to the result.

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
        // Remove elements that are out of the window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }

        // Remove elements that are smaller than the current element
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        // Add the current element to the deque
        dq.push_back(i);

        // Add the maximum element to the result
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
Input: nums = [1], k = 1
Output: [1]
```

## Key Takeaways
- Use a deque to store the indices of the maximum elements in the current window.
- Remove elements that are out of the window and smaller than the current element.
- The maximum element in the window is always at the front of the deque.